#!/usr/bin/env python3
"""Reverse-prompt tester for Bab-ilu — aesthetic-lens-only (v2.1).

This is the **abstraction training loop** for the aesthetic lens
(PRD §0.5.4 Karpathy inheritance ledger · Bab-ilu 扩展: 抽象化训练环).
Its job: take a prompt from an aesthetic entity page, generate an image
from it via `gen_client`, then ask a vision model to reverse-score the
generated image against the entity's canonical anchors (AAT, Iconclass,
Warburg panel, signature author). The score is the system's answer to
"does this prompt still land in the claimed Pathosformel?"

### v2.1 vault path resolution

Vault directories are declared by the active lens's `entity_model`.
For `aesthetic-warburg`, `entity_model.tier_1_cluster` is `panel`,
so the cluster directory is `wiki/panel/`. This module resolves that
path via `lens_loader.load_lens()` rather than hardcoding any directory
name.

`iter_aesthetics(vault)` now discovers slugs from
`wiki/<tier_1_cluster>/` as declared by the lens's entity_model.
`find_aesthetic(vault, slug)` continues to use `wiki/**/<slug>.md`
(rglob) — no directory assumption needed there.

### Scoring approach

  1. Generate image from the prompt
  2. Ask a vision model: "given this image and this expected aesthetic
     (AAT term, Iconclass, Warburg panel, signature author), is the image
     recognizably IN THE LINEAGE? Score 0-1 with rationale."
  3. Parse the score, write to frontmatter

### Usage

    python3 tools/prompt_tester.py --slug vermeer-milkmaid-interior-light --modality image
    python3 tools/prompt_tester.py --all --modality image --limit 5
    python3 tools/prompt_tester.py --slug X --modality Y --dry-run

Under a non-aesthetic lens, the CLI exits with a descriptive error
rather than generating nonsense output.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
# Default to cwd; author-path hardcode removed 2026-04-22.
DEFAULT_VAULT = Path.cwd()


def _validate_vault_or_exit(vault_path: Path) -> Path:
    """Fail fast if `vault_path` does not look like a Bab-ilu vault.

    A Bab-ilu vault has `.agent/` (lens configs) or `wiki/` (LLM-written
    content) at its root. The prior behaviour silently accepted any
    directory — which masked "works on my machine" bugs. Now we error
    clearly so the user sees the problem immediately.
    """
    vault_path = vault_path.resolve()
    has_agent = (vault_path / ".agent").is_dir()
    has_wiki = (vault_path / "wiki").is_dir()
    if not (has_agent or has_wiki):
        import sys as _sys
        print(
            f"error: {vault_path} does not look like a Bab-ilu vault "
            f"(no .agent/ or wiki/ subdirectory). Pass --vault <path> "
            f"explicitly or run this command from a vault root.",
            file=_sys.stderr,
        )
        _sys.exit(2)
    return vault_path

try:
    from gen_client import GenClient, DATA_URL_RE  # type: ignore[no-redef]
    from lens_loader import load_lens, LensValidationError  # type: ignore[no-redef]
except ImportError:  # tools/ also importable as a package (`python -m tools.prompt_tester`)
    from tools.gen_client import GenClient, DATA_URL_RE
    from tools.lens_loader import load_lens, LensValidationError

try:
    import httpx
except ImportError:
    print("error: httpx required", file=sys.stderr)
    sys.exit(2)

FRONTMATTER_RE = re.compile(r"^(---\n)(.*?)(\n---\n)", re.DOTALL)
PROMPT_SECTION_RE = re.compile(
    r"### (\w+(?:_\w+)?) prompt.*?\n(.*?)(?=\n###|\n<!-- llm:section-end|\Z)",
    re.DOTALL,
)


@dataclass
class TestResult:
    slug: str
    modality: str
    model: str
    prompt_length: int
    generated_image_path: str | None
    score: float | None
    rationale: str | None
    error: str | None
    latency_ms: int


def find_aesthetic(vault: Path, slug: str) -> Path | None:
    wiki = vault / "wiki"
    for md in wiki.rglob(f"{slug}.md"):
        if md.is_file() and not md.is_symlink():
            return md
    return None


def read_prompt(md_path: Path, modality: str) -> tuple[str | None, dict]:
    """Extract the specified modality's prompt body + frontmatter data."""
    text = md_path.read_text(encoding="utf-8")
    fm_match = FRONTMATTER_RE.match(text)
    if not fm_match:
        return None, {}
    fm_raw = fm_match.group(2)
    # quick parse of relevant frontmatter fields
    fm: dict[str, Any] = {}
    for line in fm_raw.split("\n"):
        tm = re.match(r"^([\w_-]+):\s*(.*)$", line)
        if tm:
            k, v = tm.group(1), tm.group(2).strip().strip('"').strip("'")
            fm[k] = v if v != "null" else None

    # Find prompt section body — look for the modality heading
    body = text[fm_match.end():]
    # Modality heading patterns: "### UI prompt" / "### Image prompt" / "### Video prompt"
    #                           / "### UX flow prompt" / "### Painting prompt" / "### Motion prompt"
    modality_display = {
        "ui": "UI",
        "image": "Image",
        "video": "Video",
        "ux_flow": "UX flow",
        "painting": "Painting",
        "motion": "Motion",
    }
    name = modality_display.get(modality, modality.capitalize())
    # Try multiple heading patterns (v1.3 vs v1.4 formats differ)
    patterns = [
        rf"###\s+{re.escape(name)}\s+prompt.*?\n(.*?)(?=\n###\s+\w+\s+prompt|<!-- llm:section-end|\n## |\Z)",
        rf"###\s+{re.escape(name)}.*?\n(.*?)(?=\n###|\n## |<!-- llm:section-end|\Z)",
    ]
    body_text = None
    for pat in patterns:
        m = re.search(pat, body, re.DOTALL | re.IGNORECASE)
        if m and len(m.group(1).strip()) > 20:
            body_text = m.group(1).strip()
            break

    # Fallback: if no explicit section found, try the entire Prompts section
    if not body_text:
        prompts_section = re.search(
            r"<!-- llm:section-start prompts -->\s*\n.*?## Prompts\s*\n(.*?)<!-- llm:section-end prompts -->",
            body, re.DOTALL,
        )
        if prompts_section:
            full_prompts = prompts_section.group(1).strip()
            if len(full_prompts) > 50:
                body_text = full_prompts

    if not body_text:
        return None, fm

    # Extract from fenced block if present
    code = re.search(r"```.*?\n(.*?)```", body_text, re.DOTALL)
    prompt = code.group(1).strip() if code else body_text
    return prompt, fm


def score_prompt_structure(prompt: str, metadata: dict) -> tuple[float, str]:
    """Deterministic structural scoring — no LLM needed.

    Checks whether the prompt follows Panofsky 4-segment structure and cites
    at least one authoritative anchor. Returns (score in [0,1], rationale).

    Rubric (max 1.0):
      - Has `[pre-iconographic]` segment      → +0.15
      - Has `[iconographic]` segment          → +0.15
      - Has `[iconological]` segment          → +0.15
      - Has `[lineage]` segment               → +0.15
      - Cites at least one AAT term           → +0.10
      - Cites Iconclass / Wikidata / ULAN     → +0.10
      - Cites Warburg panel wikilink          → +0.10
      - Cites a canonical author / signature  → +0.10
    """
    prompt_lower = prompt.lower()
    score = 0.0
    passes: list[str] = []
    fails: list[str] = []
    for seg in ("pre-iconographic", "iconographic", "iconological", "lineage"):
        marker = f"[{seg}]"
        if marker in prompt_lower:
            score += 0.15
            passes.append(seg)
        else:
            fails.append(seg)
    if re.search(r"\baat:?[\s_]*\d+|aat:30\d{7}", prompt, re.IGNORECASE):
        score += 0.10
        passes.append("aat")
    else:
        fails.append("aat")
    if re.search(r"iconclass|wikidata|ulan|Q\d{3,}|q\d{3,}", prompt):
        score += 0.10
        passes.append("iconclass/wikidata/ulan")
    else:
        fails.append("iconclass/wikidata/ulan")
    if "warburg" in prompt_lower or re.search(r"\[\[[\w-]+\]\]", prompt):
        score += 0.10
        passes.append("panel")
    else:
        fails.append("panel")
    # signature authors: a surname followed by era/year
    if re.search(r"[A-Z][a-z]+(?:[\s-][A-Z][a-z]+)?\s*(?:c\.|ca\.|\d{4})", prompt):
        score += 0.10
        passes.append("signature")
    else:
        fails.append("signature")
    rationale = f"structural pass: {', '.join(passes)} · missing: {', '.join(fails) or 'none'}"
    return min(1.0, score), rationale


def score_image_vision(
    image_b64: str,
    prompt: str,
    metadata: dict,
) -> tuple[float | None, str]:
    """Ask a vision model: does the image recognizably fit the aesthetic lineage?
    Returns (score [0-1], rationale). Uses the same image API (OpenAI-compatible).

    NOTE: not every `IMAGE_GEN_BASE_URL` gateway supports vision input across
    all models. This function tries several candidate models; callers should
    fall back to score_prompt_structure on failure."""
    base = os.getenv("IMAGE_GEN_BASE_URL", "").rstrip("/")
    key = os.getenv("IMAGE_GEN_API_KEY", "")
    if not base or not key:
        return None, "api config missing"

    # Use the pro model for scoring (reasoning quality matters here)
    # Fallback chain: try unrouted pro first, then 「prefix」pro variants, then flash
    vision_models = [
        "「CS」gemini-3-pro-image-preview",
        "「KS」gemini-3-pro-image-preview",
        "「Rim」gemini-3-pro-image-preview",
        "gemini-3-pro-image-preview",
        "gemini-3.1-flash-image-preview",
    ]
    # Build evaluation prompt
    anchors_lines = []
    for fld in ("aat_id", "iconclass", "wikidata", "warburg_panel", "ulan_id", "panofsky_layer", "domain"):
        val = metadata.get(fld)
        if val and val != "null":
            anchors_lines.append(f"  - {fld}: {val}")
    title = metadata.get("title", "")
    anchor_text = "\n".join(anchors_lines) if anchors_lines else "  (no anchors declared)"
    eval_prompt = f"""You are an aesthetic-lineage evaluator for Bab-ilu (a Warburg/Panofsky-informed knowledge base).

Below is a GENERATED image produced from the prompt that appears after the image.
Your job: assess whether the image recognizably sits in the declared aesthetic lineage.

Aesthetic title: {title}
Authoritative anchors:
{anchor_text}

Original prompt used:
<<<
{prompt[:2000]}
>>>

Evaluation rubric:
- 0.9-1.0: fully recognizable lineage — the image could be mistaken for a real exemplar of the tradition
- 0.7-0.9: strong lineage signals — clear affinity with the declared anchors
- 0.5-0.7: partial — some correct elements but also generic / cliché fallbacks
- 0.3-0.5: weak — only surface features match, deeper compositional/iconographic logic missing
- 0.0-0.3: off-target — image does not belong to the declared lineage

Output MUST be strictly: `SCORE: <0.0-1.0>` on one line, then a 1-3 sentence rationale.

Do NOT regenerate an image. Score the provided image and explain."""
    last_err = "all scorer models failed"
    for vision_model in vision_models:
        try:
            with httpx.Client(timeout=120.0) as cli:
                r = cli.post(
                    f"{base}/v1/chat/completions",
                    headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                    json={
                        "model": vision_model,
                        "messages": [
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "image_url",
                                        "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"},
                                    },
                                    {"type": "text", "text": eval_prompt},
                                ],
                            }
                        ],
                    },
                )
            if r.status_code >= 400:
                last_err = f"{vision_model}: HTTP {r.status_code}: {r.text[:160]}"
                continue
            data = r.json()
            reply = data.get("choices", [{}])[0].get("message", {}).get("content", "")
            if isinstance(reply, list):
                reply = " ".join(p.get("text", "") for p in reply if isinstance(p, dict))
            # Skip image-only responses (no SCORE)
            m = re.search(r"SCORE:\s*([0-9.]+)", reply)
            if not m:
                last_err = f"{vision_model}: no SCORE in reply: {reply[:160]}"
                continue
            score = float(m.group(1))
            rationale = re.sub(r"SCORE:\s*[0-9.]+\s*", "", reply, count=1).strip()
            # Strip any trailing image data URL from rationale
            rationale = DATA_URL_RE.sub("[image omitted]", rationale).strip()
            return max(0.0, min(1.0, score)), rationale or "(no rationale)"
        except Exception as e:
            last_err = f"{vision_model} exception: {type(e).__name__}: {e}"
            continue
    return None, last_err


def write_back_score(md_path: Path, modality: str, score: float, timestamp: str) -> None:
    """Update ONLY the specified modality's test_score + last_tested in frontmatter.

    Two supported shapes:
      1. Single-line: `  image: {generated: X, last_tested: null, test_score: null, ...}`
      2. Multi-line:  `  image:\n    generated: X\n    last_tested: null\n    test_score: null\n    ...`
    """
    text = md_path.read_text(encoding="utf-8")

    # Shape 1: single-line dict
    single_re = rf"^(\s+{re.escape(modality)}:\s*\{{)([^}}]*)(\}})$"
    m1 = re.search(single_re, text, re.MULTILINE)
    if m1:
        prefix, inner, suffix = m1.group(1), m1.group(2), m1.group(3)
        new_inner = re.sub(r"last_tested:\s*null", f"last_tested: {timestamp}", inner)
        new_inner = re.sub(r"test_score:\s*null", f"test_score: {score}", new_inner)
        if "last_tested:" not in new_inner:
            new_inner = new_inner.rstrip(" ,") + f", last_tested: {timestamp}"
        if "test_score:" not in new_inner:
            new_inner = new_inner.rstrip(" ,") + f", test_score: {score}"
        text = text[: m1.start()] + prefix + new_inner + suffix + text[m1.end():]
        md_path.write_text(text, encoding="utf-8")
        return

    # Shape 2: multi-line block. Detect base indent from the modality line, then
    # only replace within the contiguous sub-indented lines following it.
    lines = text.split("\n")
    header_re = re.compile(rf"^(\s+){re.escape(modality)}:\s*$")
    for idx, line in enumerate(lines):
        hm = header_re.match(line)
        if not hm:
            continue
        base_indent = len(hm.group(1))
        # Scan following lines while they are indented more than base
        end_idx = idx + 1
        while end_idx < len(lines):
            next_line = lines[end_idx]
            if next_line.strip() == "":
                end_idx += 1
                continue
            nl_indent = len(next_line) - len(next_line.lstrip(" "))
            if nl_indent <= base_indent:
                break
            end_idx += 1
        # Edit within [idx+1, end_idx)
        for j in range(idx + 1, end_idx):
            if "last_tested:" in lines[j] and "null" in lines[j]:
                lines[j] = re.sub(r"last_tested:\s*null", f"last_tested: {timestamp}", lines[j])
            if "test_score:" in lines[j] and "null" in lines[j]:
                lines[j] = re.sub(r"test_score:\s*null", f"test_score: {score}", lines[j])
        md_path.write_text("\n".join(lines), encoding="utf-8")
        return


def test_slug(
    vault: Path, slug: str, modality: str, dry_run: bool, out_dir: Path
) -> TestResult:
    start = time.time()
    md_path = find_aesthetic(vault, slug)
    if not md_path:
        return TestResult(slug, modality, "", 0, None, None, None, f"slug not found in vault", 0)
    prompt, fm = read_prompt(md_path, modality)
    if not prompt:
        return TestResult(slug, modality, "", 0, None, None, None, f"no {modality} prompt found", 0)

    client = GenClient.from_env()
    print(f"  → generating {modality} for {slug}...", file=sys.stderr)
    gen = client.generate_image(prompt)
    if not gen.success:
        return TestResult(
            slug, modality, gen.model, len(prompt), None, None, None,
            gen.error or "generation failed", gen.latency_ms,
        )
    # Save image
    img_path = None
    if gen.image_b64:
        out_dir.mkdir(parents=True, exist_ok=True)
        img_path = out_dir / f"{slug}_{modality}_{int(time.time())}.jpg"
        img_path.write_bytes(base64.b64decode(gen.image_b64))

    # Score: try vision first, fall back to structural
    if dry_run:
        return TestResult(
            slug, modality, gen.model, len(prompt), str(img_path) if img_path else None,
            None, "[dry-run: no scoring]", None, gen.latency_ms,
        )
    print(f"  → scoring (vision)...", file=sys.stderr)
    score, rationale = score_image_vision(gen.image_b64 or "", prompt, fm)
    if score is None:
        print(f"  → vision failed, falling back to structural scorer...", file=sys.stderr)
        score, rationale = score_prompt_structure(prompt, fm)
        rationale = f"[structural] {rationale}"
    else:
        rationale = f"[vision] {rationale}"
    write_back_score(md_path, modality, score, date.today().isoformat())
    print(f"  ✓ {slug} {modality}: score={score:.2f} · {rationale[:100]}", file=sys.stderr)

    return TestResult(
        slug, modality, gen.model, len(prompt),
        str(img_path) if img_path else None,
        score, rationale, None,
        int((time.time() - start) * 1000),
    )


AESTHETIC_LENS_ID = "aesthetic-warburg"


def _resolve_tier1_cluster_path(vault: Path) -> Path:
    """Return the wiki subdirectory declared by the active lens's tier_1_cluster.

    Loads the aesthetic-warburg lens from ``<vault>/.agent/lenses/`` and reads
    ``entity_model.tier_1_cluster``.  For the current lens that value is
    ``panel``, so the returned path is ``<vault>/wiki/panel/``.

    Falls back to ``wiki/panel`` (hardcoded default) if the lens cannot be
    loaded, so existing callers never crash on a misconfigured vault.
    """
    lenses_base = vault / ".agent" / "lenses"
    try:
        cfg = load_lens(AESTHETIC_LENS_ID, base=lenses_base)
        cluster_name = cfg.entity_model.get("tier_1_cluster", "panel")
    except (FileNotFoundError, LensValidationError):
        cluster_name = "panel"
    return vault / "wiki" / cluster_name


def iter_aesthetics(vault: Path) -> list[str]:
    wiki_cluster = _resolve_tier1_cluster_path(vault)
    slugs = []
    for md in wiki_cluster.rglob("*.md"):
        if md.is_symlink():
            continue
        slugs.append(md.stem)
    return sorted(slugs)


def _guard_aesthetic_lens(vault: Path, lens_override: str | None) -> None:
    """Exit early if the active lens is not aesthetic-warburg.

    Reverse prompting is currently a pre-installed capability **only** for
    the aesthetic lens (PRD §0.5.4). Other lenses' equivalent of abstraction
    training loops will grow via LENS EVOLUTION (Track L) and are not the
    subject of Sprint 4. Trying to run prompt_tester against an engineering
    or zettelkasten vault would produce meaningless Pathosformel-shaped
    outputs.

    Resolution order for the active lens:
      1. Explicit `lens_override` (from `--lens` CLI arg), honored verbatim.
      2. `<vault>/.agent/lenses/active/lens.yaml:id` field.
      3. Error with a clear diagnostic if neither is present.
    """
    if lens_override:
        active = lens_override
    else:
        active_yaml = vault / ".agent" / "lenses" / "active" / "lens.yaml"
        if not active_yaml.exists():
            print(
                f"error: no active lens at {active_yaml}. "
                "prompt_tester requires an aesthetic-warburg vault. "
                "Run /genesis in the target vault first.",
                file=sys.stderr,
            )
            sys.exit(2)
        try:
            import yaml
        except ImportError:
            print("error: PyYAML required for lens resolution", file=sys.stderr)
            sys.exit(2)
        try:
            parsed = yaml.safe_load(active_yaml.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            print(f"error: cannot parse {active_yaml}: {exc}", file=sys.stderr)
            sys.exit(2)
        active = parsed.get("id") or ""

    if active != AESTHETIC_LENS_ID:
        print(
            f"error: prompt_tester is aesthetic-only (active lens: {active!r}). "
            "Reverse prompting for other lenses will grow via LENS EVOLUTION "
            "(Track L) — see PRD §0.5.3 principle 2 (anti-essentialism).",
            file=sys.stderr,
        )
        sys.exit(2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=str(DEFAULT_VAULT))
    ap.add_argument("--lens", default=None,
                    help="Lens override (default: read from <vault>/.agent/lenses/active/)")
    ap.add_argument("--slug", help="Single aesthetic slug to test")
    ap.add_argument("--all", action="store_true", help="Test all aesthetic cards")
    ap.add_argument("--modality", default="image", choices=["ui", "image", "video", "ux_flow", "painting", "motion"])
    ap.add_argument("--dry-run", action="store_true", help="Generate but don't score")
    ap.add_argument("--limit", type=int, default=None, help="Cap number of cards when --all")
    ap.add_argument("--out-dir", default="/tmp/babilu-gen", help="Where to save generated images")
    ap.add_argument("--json", action="store_true", help="Emit JSON summary")
    args = ap.parse_args()

    vault = _validate_vault_or_exit(Path(args.vault))
    # Lens guard — reverse prompting is aesthetic-lens-only in Sprint 4 MVP.
    _guard_aesthetic_lens(vault, args.lens)
    out_dir = Path(args.out_dir)
    if args.slug:
        slugs = [args.slug]
    elif args.all:
        slugs = iter_aesthetics(vault)
        if args.limit:
            slugs = slugs[: args.limit]
    else:
        print("--slug <S> or --all required", file=sys.stderr)
        sys.exit(2)

    print(f"Testing {len(slugs)} card(s) × modality={args.modality}", file=sys.stderr)
    results: list[TestResult] = []
    for slug in slugs:
        res = test_slug(vault, slug, args.modality, args.dry_run, out_dir)
        results.append(res)

    # summary
    scored = [r for r in results if r.score is not None]
    passed = [r for r in scored if r.score >= 0.7]
    print("", file=sys.stderr)
    print(f"=== summary ===", file=sys.stderr)
    print(f"  tested: {len(results)}", file=sys.stderr)
    print(f"  scored: {len(scored)}", file=sys.stderr)
    print(f"  passed (>=0.7): {len(passed)}", file=sys.stderr)
    print(f"  failed: {len(scored) - len(passed)}", file=sys.stderr)
    errors = [r for r in results if r.error]
    print(f"  errors: {len(errors)}", file=sys.stderr)

    if args.json:
        print(json.dumps([asdict(r) for r in results], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
