"""Observer — the "second pair of eyes" that watches user behavior.

Append-only event capture + running digest. Never listens to user
declarations (e.g. "I want to study X"); only records what the user
*does* (ingests, queries, accepts, rejects, names).

Per PRD §0.5.3 principle 5 (practice over rules) and §0.5.3 principle 1
(late binding): the observer itself does NOT infer theories. Its job is
to accumulate a clean, searchable behavioral record + lightweight
aggregates. The actual theory-matching happens at matcher time, when
an LLM reads this digest and does the abstracting. Keeping the
accumulator dumb avoids baking any theory-guessing heuristic into
the core.

State files (vault-scoped):

  <vault>/.agent/state/lens_observer.jsonl
    Append-only event log. One JSON per line. Events never rewritten.

  <vault>/.agent/state/lens_hypotheses.json
    Running digest maintained for efficient LLM access at matcher time.
    Lightweight aggregates (recent entity names, query phrases, ingest
    types) + any hypotheses users have accepted/rejected before (so
    the matcher doesn't re-propose them).

Integration points (current + future):

  - tools/ask_runner.py write_synthesis → record synthesis_accepted
  - tools/ask_runner.py run_ask → record ask_query
  - tools/ingest_runner.py (existing) → record ingest events
  - tools/lens_evolution/evolver.py → record accept / reject decisions

The observer's hooks are deliberately NON-mandatory — if a caller
forgets to invoke record_event, the system degrades gracefully
(matcher just sees fewer events; no crash). This is "clean-loop-first"
(principle 3) — a never-crashing background layer.
"""

from __future__ import annotations

import fcntl
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

__all__ = [
    "EVENT_LOG_PATH",
    "DIGEST_PATH",
    "BehavioralEvent",
    "ObserverDigest",
    "record_event",
    "load_digest",
    "clear_state",
]

EVENT_LOG_PATH = Path(".agent/state/lens_observer.jsonl")
DIGEST_PATH = Path(".agent/state/lens_hypotheses.json")

# How many of each aggregate we keep in the digest. Values tuned to fit
# a single LLM context window for the matcher pass (~50-100 items × ~30
# tokens each = ~3k tokens of behavioral signal per aggregate).
_RECENT_ENTITY_NAMES_CAP = 100
_RECENT_QUERIES_CAP = 50
_RECENT_INGEST_TYPES_CAP = 100
_WIKILINK_EDGES_CAP = 200
# Open-bucket cap for unknown event types — principle 4 channel for
# new behavioral hooks we haven't enumerated yet.
_RECENT_OTHER_EVENTS_CAP = 80

# Event types accepted. Kept open (the log can carry any string), but
# well-known names are enumerated for discoverability by downstream tools.
KNOWN_EVENT_TYPES = frozenset({
    "ingest",            # user ran /ingest on a raw source
    "ask_query",         # user ran /ask with a query string
    "synthesis_accepted", # user archived /ask answer as synthesis
    "taste_accept",      # user accepted a /taste proposal
    "taste_reject",      # user rejected a /taste proposal
    "entity_named",      # new entity page created with a title
    "wikilink_created",  # wikilink edge added between entities
    "lens_evolution_accept",  # user accepted a LENS EVOLUTION candidate
    "lens_evolution_reject",  # user rejected a LENS EVOLUTION candidate
})


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass(frozen=True)
class BehavioralEvent:
    """One recorded observation of user behavior.

    `data` is a free-form dict per event type. Known shapes:
      ingest            → {"slug": str, "raw_type": str, "source_path": str}
      ask_query         → {"query": str, "winning_step": str, "cited_count": int}
      synthesis_accepted → {"slug": str, "question": str, "title": str}
      taste_accept      → {"slug": str, "proposal_type": str}
      taste_reject      → {"slug": str, "reason": str | None}
      entity_named      → {"slug": str, "title": str, "tier": str}
      wikilink_created  → {"from": str, "to": str}
      lens_evolution_*  → {"theory": str, "citation_ref": str, ...}
    """
    ts: str
    type: str
    lens: str
    data: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {"ts": self.ts, "type": self.type,
                "lens": self.lens, "data": self.data}


@dataclass
class ObserverDigest:
    """Running, LLM-friendly summary of the behavioral log.

    Rebuilt from the event log each time `record_event` runs, so the
    event log is authoritative and the digest is a cache. If the digest
    file is ever lost, `rebuild_digest_from_log` reconstitutes it.

    `accepted_hypotheses` and `rejected_hypotheses` carry user feedback
    from the evolver — surfacing to the matcher as "do not re-propose"
    context on the next pass.

    `recent_other_events` is an open bucket — it carries any event type
    not enumerated above, so that when the system gains new behavioral
    hooks (e.g. `/taste accept` in Sprint 5, `/ingest` in Track G2) the
    matcher prompt sees the new signal without requiring a code change.
    This is principle 4 (Ashby variety matching) realized at the digest
    boundary: the matcher's variety channel stays open-ended.
    """
    recent_entity_names: list[str] = field(default_factory=list)
    recent_queries: list[str] = field(default_factory=list)
    recent_ingest_types: list[str] = field(default_factory=list)
    wikilink_edges: list[list[str]] = field(default_factory=list)
    accepted_hypotheses: list[dict[str, Any]] = field(default_factory=list)
    rejected_hypotheses: list[dict[str, Any]] = field(default_factory=list)
    recent_other_events: list[dict[str, Any]] = field(default_factory=list)
    total_events: int = 0
    first_event_ts: Optional[str] = None
    last_event_ts: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "recent_entity_names": self.recent_entity_names,
            "recent_queries": self.recent_queries,
            "recent_ingest_types": self.recent_ingest_types,
            "wikilink_edges": self.wikilink_edges,
            "accepted_hypotheses": self.accepted_hypotheses,
            "rejected_hypotheses": self.rejected_hypotheses,
            "recent_other_events": self.recent_other_events,
            "total_events": self.total_events,
            "first_event_ts": self.first_event_ts,
            "last_event_ts": self.last_event_ts,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> ObserverDigest:
        return cls(
            recent_entity_names=list(d.get("recent_entity_names") or []),
            recent_queries=list(d.get("recent_queries") or []),
            recent_ingest_types=list(d.get("recent_ingest_types") or []),
            wikilink_edges=[list(e) for e in d.get("wikilink_edges") or []],
            accepted_hypotheses=list(d.get("accepted_hypotheses") or []),
            rejected_hypotheses=list(d.get("rejected_hypotheses") or []),
            recent_other_events=list(d.get("recent_other_events") or []),
            total_events=int(d.get("total_events") or 0),
            first_event_ts=d.get("first_event_ts"),
            last_event_ts=d.get("last_event_ts"),
        )


def record_event(
    vault: Path,
    event_type: str,
    lens: str,
    data: dict[str, Any],
    *,
    ts: Optional[str] = None,
) -> BehavioralEvent:
    """Append one behavioral event and refresh the digest.

    Swallows IO errors silently beyond the event-append step — a
    corrupted digest file is rebuilt on the next call rather than
    crashing the caller (principle 3: never let background observation
    break the foreground loop).

    The concurrency guard: event-log writes take a POSIX advisory lock
    so two simultaneous /ingest invocations can't produce torn JSONL
    lines. The digest refresh is not locked; concurrent digest writes
    race but both see a well-formed event log, so the last-writer-wins
    outcome is consistent with the log.
    """
    event = BehavioralEvent(
        ts=ts or _now_iso(),
        type=event_type,
        lens=lens,
        data=dict(data),
    )
    vault = Path(vault).resolve()
    log_path = vault / EVENT_LOG_PATH
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        f.write(json.dumps(event.to_dict(), ensure_ascii=False) + "\n")
    try:
        digest = rebuild_digest_from_log(vault)
        _save_digest(vault, digest)
    except Exception:  # pragma: no cover — never break foreground
        pass
    return event


def _save_digest(vault: Path, digest: ObserverDigest) -> None:
    path = vault / DIGEST_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(digest.to_dict(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    tmp.replace(path)


def load_digest(vault: Path) -> ObserverDigest:
    """Return the current digest. If missing/corrupt, rebuild from log.

    This is the public read path for the matcher. Empty state (no
    events yet) returns a fresh ObserverDigest — callers never have
    to null-check.
    """
    vault = Path(vault).resolve()
    path = vault / DIGEST_PATH
    if path.exists():
        try:
            return ObserverDigest.from_dict(
                json.loads(path.read_text(encoding="utf-8"))
            )
        except (json.JSONDecodeError, TypeError, ValueError):
            # fall through to rebuild
            pass
    return rebuild_digest_from_log(vault)


def rebuild_digest_from_log(vault: Path) -> ObserverDigest:
    """Rebuild the digest by replaying the event log.

    Fast enough at expected scale (~1000 events) to run on every record;
    if it becomes a bottleneck we can introduce incremental updates,
    but YAGNI for now — §0.5 principle 1 (late binding).
    """
    vault = Path(vault).resolve()
    log_path = vault / EVENT_LOG_PATH
    digest = ObserverDigest()
    if not log_path.exists():
        return digest

    entity_names: list[str] = []
    queries: list[str] = []
    ingest_types: list[str] = []
    edges: list[list[str]] = []
    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    # Principle 4 (Ashby variety): unknown event types do not get dropped;
    # they land here, preserving an open variety channel to the matcher.
    other_events: list[dict[str, Any]] = []

    for raw_line in log_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue  # tolerate corrupted line; skip
        etype = rec.get("type")
        data = rec.get("data") or {}
        ts = rec.get("ts")

        digest.total_events += 1
        if digest.first_event_ts is None:
            digest.first_event_ts = ts
        digest.last_event_ts = ts

        if etype == "entity_named":
            title = data.get("title") or data.get("slug")
            if isinstance(title, str) and title:
                entity_names.append(title)
        elif etype == "ask_query":
            q = data.get("query")
            if isinstance(q, str) and q:
                queries.append(q)
        elif etype == "ingest":
            raw_type = data.get("raw_type")
            if isinstance(raw_type, str) and raw_type:
                ingest_types.append(raw_type)
        elif etype == "wikilink_created":
            fr, to = data.get("from"), data.get("to")
            if isinstance(fr, str) and isinstance(to, str):
                edges.append([fr, to])
        elif etype == "lens_evolution_accept":
            accepted.append({
                "theory": data.get("theory", ""),
                "citation_ref": data.get("citation_ref", ""),
                "ts": ts,
            })
        elif etype == "lens_evolution_reject":
            rejected.append({
                "theory": data.get("theory", ""),
                "citation_ref": data.get("citation_ref", ""),
                "reason": data.get("reason", ""),
                "ts": ts,
            })
        else:
            # Open variety bucket — any new event type flows here
            # without requiring a code change to this rebuild.
            other_events.append({"type": etype, "ts": ts, "data": data})

    # Keep only the tail of each aggregate — recency matters, older
    # events stay in the log for audit but fall off the digest.
    digest.recent_entity_names = entity_names[-_RECENT_ENTITY_NAMES_CAP:]
    digest.recent_queries = queries[-_RECENT_QUERIES_CAP:]
    digest.recent_ingest_types = ingest_types[-_RECENT_INGEST_TYPES_CAP:]
    digest.wikilink_edges = edges[-_WIKILINK_EDGES_CAP:]
    # Accepted/rejected are NOT capped — the matcher needs the full
    # user-feedback history to avoid re-proposing. If it grows too
    # large for one context we'll paginate in Sprint 5.
    digest.accepted_hypotheses = accepted
    digest.rejected_hypotheses = rejected

    return digest


def clear_state(vault: Path) -> None:
    """Remove both event log and digest. Test helper — never used in
    production, but explicit so tests aren't inventing ad-hoc cleanup.
    """
    vault = Path(vault).resolve()
    for rel in (EVENT_LOG_PATH, DIGEST_PATH):
        p = vault / rel
        if p.exists():
            p.unlink()
