"""Runtime injection of the active lens's prompts into LLM context.

A Bab-ilu vault activates exactly one lens at a time by materializing a copy
of `.agent/lenses/<chosen>/` under `.agent/lenses/active/`. The lens's
`prompts.md` — freeform judgment rules, traps, and tone hints — must be
woven into every command's LLM context at runtime (PRD v2.1 §4.2, §6.2).

This module is the canonical reader. It is deliberately tiny:

    from tools.lens_context import load_active_prompts, active_lens_preamble

    text      = load_active_prompts()       # raw file contents, or ""
    preamble  = active_lens_preamble()      # <lens-context>…</lens-context>, or ""

Design choices:

1. **Cache in-process, invalidate by mtime.** A single vault session
   hammers `/taste`, `/gap`, `/prompt` etc. many times; re-reading the
   same file is wasted I/O. Cache keyed by (resolved path, mtime_ns);
   if the file is rewritten (e.g. `/genesis` re-activates a different
   lens), the next call transparently refreshes.

2. **Env var override via `BABILU_LENS_PROMPTS_PATH`.** Lets tests point
   at fixtures and lets power users experiment with alternate prompt
   packs without disturbing `.agent/lenses/active/`.

3. **Missing file is a soft condition.** Before any lens is activated
   the vault is still usable — commands should proceed with an empty
   preamble rather than crash. A single warning is emitted per process
   to surface the issue without spamming the log.
"""

from __future__ import annotations

import logging
import os
import threading
from pathlib import Path
from typing import Optional

__all__ = [
    "DEFAULT_ACTIVE_PROMPTS_PATH",
    "ENV_OVERRIDE_KEY",
    "active_lens_preamble",
    "clear_cache",
    "load_active_prompts",
]

DEFAULT_ACTIVE_PROMPTS_PATH = Path(".agent/lenses/active/prompts.md")
ENV_OVERRIDE_KEY = "BABILU_LENS_PROMPTS_PATH"

_logger = logging.getLogger("babilu.lens_context")

_cache_lock = threading.Lock()
_cache: dict[tuple[Path, int], str] = {}
_missing_warned: set[Path] = set()


def _resolve_target(explicit: Optional[Path] = None) -> Path:
    """Pick the path to read, in precedence order: explicit arg > env > default.

    The resolved path is always absolute. Long-running hosts or tests that
    switch cwd between calls would otherwise produce inconsistent cache
    keys — e.g. ``Path(".agent/lenses/active/prompts.md")`` resolves to a
    different real file after ``chdir``, but compares equal to any key
    inserted under the old cwd, causing wrong-file cache hits.
    Resolving once up front sidesteps the entire class of bug.
    """
    if explicit is not None:
        raw = explicit
    else:
        env_val = os.environ.get(ENV_OVERRIDE_KEY)
        raw = Path(env_val) if env_val else DEFAULT_ACTIVE_PROMPTS_PATH
    # ``Path.resolve(strict=False)`` is documented to succeed on missing
    # targets since 3.6, so the pre-genesis "no active lens" path still
    # returns a usable Path instead of raising.
    return raw.resolve(strict=False)


def clear_cache() -> None:
    """Drop the in-process cache and warn-once state.

    Public entry point — called by tests between fixtures and by long-running
    hosts that want to force a reload without touching the filesystem.
    """
    with _cache_lock:
        _cache.clear()
        _missing_warned.clear()


def _warn_missing_once(path: Path) -> None:
    """Emit the once-per-process missing-file warning.

    MUST be called with ``_cache_lock`` held. ``_missing_warned`` is a
    set shared across threads; the `in`-then-`add` sequence is a
    classic check-then-act race without the lock. ``clear_cache`` also
    mutates this set under the lock, so readers and writers must agree.
    """
    if path in _missing_warned:
        return
    _missing_warned.add(path)
    _logger.warning(
        "active lens prompts not found at %s — commands will run without "
        "lens-specific context. Run /genesis to activate a lens.",
        path,
    )


def load_active_prompts(path: Optional[Path] = None) -> str:
    """Return the contents of the active lens's `prompts.md`.

    Args:
        path: explicit override (mainly for tests). Beats env + default.

    Returns:
        File contents as UTF-8 text, or an empty string if the file is
        missing. Never raises — a missing active lens is a normal
        pre-`/genesis` state.

    Caching:
        Cache key is `(resolved_path, mtime_ns)`. Repeated calls on an
        unchanged file hit the cache. Rewriting the file (new mtime)
        transparently invalidates the entry.
    """
    target = _resolve_target(path)

    try:
        stat = target.stat()
    except FileNotFoundError:
        with _cache_lock:
            _warn_missing_once(target)
        return ""
    except OSError as exc:
        _logger.warning("failed to stat %s: %s", target, exc)
        return ""

    cache_key = (target, stat.st_mtime_ns)

    with _cache_lock:
        cached = _cache.get(cache_key)
    if cached is not None:
        return cached

    # NOTE: a TOCTOU window exists between the ``stat()`` above and the
    # ``read_text()`` below — an atomic replace in between will pair the
    # NEW content with the OLD mtime key. This is inherent to any
    # stat-then-read design. For the lens-activation use case (where the
    # file is rewritten infrequently by /genesis), the window is tiny
    # and the worst outcome is one extra call returning the fresh
    # content under the previous mtime key until the next reader
    # observes the new mtime and refreshes. Acceptable trade-off versus
    # taking the lock across a filesystem read.
    try:
        content = target.read_text(encoding="utf-8")
    except OSError as exc:
        _logger.warning("failed to read %s: %s", target, exc)
        return ""

    with _cache_lock:
        # Drop any stale entries for this path before inserting the fresh one
        # so the cache never grows unboundedly over a long session.
        for key in [k for k in _cache if k[0] == target and k != cache_key]:
            _cache.pop(key, None)
        _cache[cache_key] = content

    return content


def active_lens_preamble(path: Optional[Path] = None) -> str:
    """Return the prompts wrapped in a `<lens-context>` envelope.

    Slash-skills inject this at the top of their LLM context so the model
    reads the lens's judgment rules before it sees the user's task.
    Empty string when no active lens is configured — callers can
    unconditionally concatenate.
    """
    body = load_active_prompts(path)
    if not body.strip():
        return ""
    return f"<lens-context>\n{body.rstrip()}\n</lens-context>"


if __name__ == "__main__":  # pragma: no cover
    # Tiny CLI: `python -m tools.lens_context` prints the preamble to stdout.
    # Skills that cannot import Python can shell out to this entrypoint at
    # session start and embed the output verbatim.
    import sys

    out = active_lens_preamble()
    if not out:
        sys.exit(0)
    print(out)
