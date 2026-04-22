"""Lens-specific incident extractor for the engineering-alexander lens.

Parallel to `tools/note_extractor.py`. Architecture contract (post-v2.2
rewrite, aligned with Bab-ilu's Claude-drive skill pattern):

1. **No LLM calls.** This module does deterministic IO + canonicalization
   + regex-driven partial-fact extraction + path resolution only. The
   narrative prose, root-cause analysis, impact bullets, and lesson
   bullets are authored by the invoking Claude Code session via the
   `/ingest` SKILL.md after this module has rendered the stub. This
   removes the prior dependency on the Anthropic SDK and the
   ANTHROPIC_API_KEY environment variable — matching the headline
   README promise that all LLM reasoning happens inside the current
   Claude Code session.

2. **Deterministic pre-work still lives here.** Service-name
   canonicalization, date parsing, duration extraction, domain
   classification, RFC/CVE/CWE anchor detection, content-hash drift
   canary — all of these are cheap regex/keyword passes that produce
   reproducible results without any LLM. They are pre-filled into the
   stub frontmatter so Claude's content-authoring pass starts with
   ground-truth anchors and only fills the prose.

3. **Pure-function core, filesystem shell.** `extract_incident` is a
   pure transform — no file writes, no journal writes. The caller
   (`ingest_runner._run_incident_extractor`) is responsible for
   persisting the `markdown` at `output_path`.

4. **Protocol-typed HTTP for tests.** `HTTPClient` Protocol lets test
   fixtures replay frozen HTML/PDF bytes without real network. Default
   implementation is a stdlib-only `urllib` client with an SSRF guard.

The shape of the generated page is fixed: every heading listed in the
rendered stub is produced here, with structured TODO anchors showing
Claude what to fill under each. Downstream `/lint` and the E2 pattern
extractor depend on the exact heading strings.
"""

from __future__ import annotations

import hashlib
import re
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Protocol
from urllib.parse import urlparse

try:
    from lens_loader import LensConfig  # type: ignore[no-redef]
except ImportError:  # tools/ also importable as a package
    from tools.lens_loader import LensConfig

LENS_ID = "engineering-alexander"
AGENT_MARKER = "<!-- ingest-runner:agent-stub -->"
"""Re-exported for fixture comparisons; must equal `ingest_runner.AGENT_MARKER`."""

ALLOWED_DOMAINS = (
    "runtime",
    "storage",
    "network",
    "build",
    "auth",
    "observability",
    "deployment",
)

# Service-name normalization. Keys are case-folded substrings; values are
# the vendor-canonical spelling. Extend only when the lens's
# `terminology fidelity` list needs a new anchor.
_SERVICE_NAME_MAP: tuple[tuple[str, str], ...] = (
    ("amazon s3", "Amazon S3"),
    ("aws s3", "Amazon S3"),
    (" s3 ", "Amazon S3"),
    ("cloudflare", "Cloudflare"),
    ("gitlab", "GitLab.com"),
    ("github", "GitHub"),
    ("google cloud", "Google Cloud"),
    ("fastly", "Fastly"),
    ("stripe", "Stripe"),
    ("slack", "Slack"),
    ("facebook", "Meta"),
    ("knight capital", "Knight Capital"),
)

# Keyword → domain classifier. First hit wins (ordering matters: more
# specific keywords appear first).
_DOMAIN_KEYWORDS: tuple[tuple[str, str], ...] = (
    # network
    ("bgp", "network"),
    ("dns", "network"),
    ("cdn", "network"),
    ("routing", "network"),
    ("peering", "network"),
    ("regex", "network"),  # Cloudflare 2019 lived here
    ("waf", "network"),
    ("network partition", "network"),
    # storage
    ("database", "storage"),
    ("postgres", "storage"),
    ("mysql", "storage"),
    ("blob store", "storage"),
    ("s3", "storage"),
    ("replication", "storage"),
    ("cache tier", "storage"),
    # auth
    ("oauth", "auth"),
    ("session", "auth"),
    ("iam role", "auth"),
    ("authentication", "auth"),
    # build
    ("ci/cd", "build"),
    ("artifact pipeline", "build"),
    ("build pipeline", "build"),
    # deployment
    ("canary", "deployment"),
    ("blue/green", "deployment"),
    ("rollout", "deployment"),
    ("binary rollout", "deployment"),
    # observability
    ("alerting", "observability"),
    ("metrics", "observability"),
    ("tracing", "observability"),
    # runtime (catch-all below)
    ("jvm", "runtime"),
    ("kernel panic", "runtime"),
    ("goroutine", "runtime"),
)

# Regex patterns — compiled once at module load.
_MONTH_NAMES = (
    "january|february|march|april|may|june|july|august|september|"
    "october|november|december"
)
_MONTH_TO_NUM = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5,
    "june": 6, "july": 7, "august": 8, "september": 9, "october": 10,
    "november": 11, "december": 12,
}

_RE_ISO_DATE = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
_RE_PROSE_DATE = re.compile(
    rf"\b({_MONTH_NAMES})\s+(\d{{1,2}})(?:st|nd|rd|th)?,?\s+(\d{{4}})\b",
    re.IGNORECASE,
)
_RE_DURATION_MIN = re.compile(
    r"\b(?:for|approximately|about|~)?\s*(\d{1,3})\s*(?:minute|min)s?\b",
    re.IGNORECASE,
)
_RE_DURATION_HR = re.compile(
    r"\b(?:for|approximately|about|~)?\s*(\d{1,2})\s*(?:hour|hr)s?\b",
    re.IGNORECASE,
)
_RE_RFC = re.compile(r"\bRFC\s*(\d{3,5})\b", re.IGNORECASE)
_RE_CVE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b")
_RE_CWE = re.compile(r"\bCWE-\d{1,4}\b")

# Canonicalization strips drifting metadata before hashing.
_RE_DRIFT_LINES = re.compile(
    r"^\s*(?:As of|Last updated|View count|Share this|Copied!).*$",
    re.IGNORECASE | re.MULTILINE,
)


# ---------------------------------------------------------------------------
# Protocol surfaces (injected by callers, mocked in tests)
# ---------------------------------------------------------------------------


class HTTPClient(Protocol):
    """Minimal HTTP surface. Default impl uses stdlib `urllib`; tests
    pass `tests._mocks.MockHTTPClient`.
    """
    def get(self, url: str, *, timeout: float = 15.0) -> bytes: ...


# ---------------------------------------------------------------------------
# Data carriers (frozen — immutable, hashable, safe to share)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class PartialFacts:
    """Deterministically-extracted fields from a post-mortem.

    Every field except `content_hash` and `plain_text` may be None when
    no regex anchor fires. The Claude-authoring pass fills prose body
    sections; these anchors stay deterministic.
    """
    service_name: Optional[str]
    occurred: Optional[str]           # ISO date YYYY-MM-DD
    duration_minutes: Optional[int]
    domain: Optional[str]             # one of ALLOWED_DOMAINS
    rfc_id: Optional[str]
    cve_id: Optional[str]
    cwe_id: Optional[str]
    content_hash: str                 # sha256 hex digest of canonical text
    plain_text: str                   # canonicalized body text


@dataclass(frozen=True)
class IncidentPage:
    """Rendered output. Caller writes `output_path` with `markdown`."""
    frontmatter: dict
    markdown: str
    slug: str
    output_path: Path


@dataclass(frozen=True)
class ExtractionError:
    """Non-throwing failure record. Lets the caller journal it."""
    stage: str                        # "fetch" | "parse" | "render"
    reason: str
    retriable: bool


# ---------------------------------------------------------------------------
# Primitives (pure, independently testable)
# ---------------------------------------------------------------------------


def _canonicalize(text: str) -> str:
    """Strip drifting metadata + normalize whitespace for byte-stable hash."""
    norm = unicodedata.normalize("NFC", text).replace("\u00a0", " ")
    stripped = _RE_DRIFT_LINES.sub("", norm)
    unified = stripped.replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip() for ln in unified.split("\n")]
    out_lines: list[str] = []
    blank_run = 0
    for ln in lines:
        if ln == "":
            blank_run += 1
            if blank_run <= 1:
                out_lines.append(ln)
        else:
            blank_run = 0
            out_lines.append(ln)
    return "\n".join(out_lines).strip() + "\n"


def _content_hash(canonical_text: str) -> str:
    """SHA-256 hex digest over canonicalized bytes. Used as drift canary."""
    return hashlib.sha256(canonical_text.encode("utf-8")).hexdigest()


def _extract_html_text(raw_bytes: bytes) -> str:
    """Extract article body text from HTML. Prefers <article>/<main>; falls
    back to <body>. Strips scripts, styles, nav, footer.
    """
    from bs4 import BeautifulSoup  # local import keeps module-load cost low

    soup = BeautifulSoup(raw_bytes, "html.parser")
    for tag_name in ("script", "style", "nav", "footer", "aside", "header"):
        for tag in soup.find_all(tag_name):
            tag.decompose()
    container = soup.find("article") or soup.find("main") or soup.body or soup
    return container.get_text(separator="\n", strip=True)


def _extract_pdf_text(raw_bytes: bytes) -> str:
    """Extract text from a PDF. Tests pass pre-extracted text bytes
    (`.txt` fixtures) so no real PDF parser is needed in test.

    If `raw_bytes` does not look like a PDF (no `%PDF-` header), we
    treat it as pre-extracted plain text. This is the contract the
    fixture protocol relies on: live code runs `pypdf` once, fixtures
    replay frozen text.
    """
    if not raw_bytes.lstrip().startswith(b"%PDF-"):
        return raw_bytes.decode("utf-8", errors="replace")
    try:
        import pypdf  # type: ignore
    except ImportError as exc:  # pragma: no cover — covered by synthetic path
        raise RuntimeError(
            "pypdf not installed; add to requirements.txt to enable live "
            "PDF extraction (fixtures use pre-extracted text and do not "
            "need pypdf)."
        ) from exc
    import io
    reader = pypdf.PdfReader(io.BytesIO(raw_bytes))  # pragma: no cover
    return "\n".join(page.extract_text() or "" for page in reader.pages)  # pragma: no cover


def _normalize_service_name(text: str) -> Optional[str]:
    """Return the vendor-canonical spelling when a known service is
    mentioned. Picks the service with the most occurrences, ties broken
    by first-appearance offset. Unknown services → None.
    """
    lower = text.lower()
    best: tuple[int, int, Optional[str]] = (0, 10**9, None)
    seen_canonical: dict[str, tuple[int, int]] = {}
    for needle, canonical in _SERVICE_NAME_MAP:
        count = lower.count(needle)
        if count == 0:
            continue
        first_offset = lower.find(needle)
        prev = seen_canonical.get(canonical)
        if prev is None:
            seen_canonical[canonical] = (count, first_offset)
        else:
            seen_canonical[canonical] = (prev[0] + count, min(prev[1], first_offset))
    for canonical, (count, first_offset) in seen_canonical.items():
        if count > best[0] or (count == best[0] and first_offset < best[1]):
            best = (count, first_offset, canonical)
    return best[2]


def _parse_date(text: str) -> Optional[str]:
    """Return the incident date in ISO-8601 form, or None. Prose dates
    ('July 2, 2019') preferred over bare ISO dates — the latter usually
    appear in publication metadata while the former appear in the
    narrative body.
    """
    m_prose = _RE_PROSE_DATE.search(text)
    if m_prose:
        try:
            month = _MONTH_TO_NUM[m_prose.group(1).lower()]
            day = int(m_prose.group(2))
            year = int(m_prose.group(3))
            return datetime(year, month, day).strftime("%Y-%m-%d")
        except (ValueError, KeyError):
            pass
    m_iso = _RE_ISO_DATE.search(text)
    if m_iso:
        try:
            y, mo, d = (int(g) for g in m_iso.groups())
            return datetime(y, mo, d).strftime("%Y-%m-%d")
        except ValueError:
            return None
    return None


def _parse_duration_minutes(text: str) -> Optional[int]:
    """Extract duration in minutes from prose. 'N minutes' beats 'N hours'
    when both appear."""
    m_min = _RE_DURATION_MIN.search(text)
    if m_min:
        mins = int(m_min.group(1))
        if 1 <= mins <= 999:
            return mins
    m_hr = _RE_DURATION_HR.search(text)
    if m_hr:
        hrs = int(m_hr.group(1))
        if 1 <= hrs <= 72:
            return hrs * 60
    return None


def _classify_domain(text: str) -> Optional[str]:
    """Assign `text` to one of `ALLOWED_DOMAINS` via keyword heuristics."""
    lowered = text.lower()
    for keyword, domain in _DOMAIN_KEYWORDS:
        if keyword in lowered:
            return domain
    return None


def _parse_partial_facts(canonical_text: str) -> PartialFacts:
    """Run every deterministic extractor over canonical text."""
    rfc_match = _RE_RFC.search(canonical_text)
    cve_match = _RE_CVE.search(canonical_text)
    cwe_match = _RE_CWE.search(canonical_text)
    return PartialFacts(
        service_name=_normalize_service_name(canonical_text),
        occurred=_parse_date(canonical_text),
        duration_minutes=_parse_duration_minutes(canonical_text),
        domain=_classify_domain(canonical_text),
        rfc_id=f"RFC {rfc_match.group(1)}" if rfc_match else None,
        cve_id=cve_match.group(0) if cve_match else None,
        cwe_id=cwe_match.group(0) if cwe_match else None,
        content_hash=_content_hash(canonical_text),
        plain_text=canonical_text,
    )


# ---------------------------------------------------------------------------
# Page rendering — Claude-drive stub (no LLM)
# ---------------------------------------------------------------------------


_SOURCE_EXCERPT_CHAR_LIMIT = 3000
"""How much canonical source text to embed in the stub as provenance.
Claude reads this when authoring the prose sections; the full
canonical text is re-available via the source URL. 3000 chars ≈ one
magazine-length post-mortem paragraph, enough to orient without
bloating the stub."""


def _render_page(
    facts: PartialFacts,
    slug: str,
    raw_input: str,
    input_type: str,
    ingested_at: str,
) -> tuple[dict, str]:
    """Produce (frontmatter_dict, full_markdown) for the incident page.

    This is the Claude-drive version: all deterministic facts are
    pre-filled in the frontmatter; the body has structured TODO anchors
    showing Claude where to place narrative / root cause / impact /
    lesson prose, and includes a canonical source excerpt for
    orientation. Downstream `/lint` and the E2 pattern extractor depend
    on the exact heading strings below.
    """
    frontmatter = {
        "type": "incident",
        "lens": LENS_ID,
        "slug": slug,
        "ingested_at": ingested_at,
        "input_type": input_type,
    }
    if input_type == "url":
        frontmatter["source_url"] = raw_input
        frontmatter["postmortem_url"] = raw_input
    else:
        frontmatter["source_path"] = raw_input
        frontmatter["postmortem_url"] = ""
    # Deterministic anchors. Empty string means "none found" so /lint can
    # tell the field was considered.
    frontmatter["rfc_id"] = facts.rfc_id or ""
    frontmatter["cve_id"] = facts.cve_id or ""
    frontmatter["cwe_id"] = facts.cwe_id or ""
    frontmatter["service_name"] = facts.service_name or ""
    frontmatter["bug_tracker_url"] = ""
    frontmatter["occurred"] = facts.occurred or ""
    frontmatter["duration_minutes"] = facts.duration_minutes if facts.duration_minutes is not None else 0
    frontmatter["domain"] = facts.domain or ""
    frontmatter["content_hash"] = facts.content_hash
    frontmatter["status"] = "draft"

    # Render frontmatter as YAML manually for diff-stable field ordering.
    fm_lines = ["---"]
    _field_order = [
        "type", "lens", "slug", "ingested_at", "input_type",
        "source_url", "source_path",
        "rfc_id", "cve_id", "cwe_id", "postmortem_url", "service_name",
        "bug_tracker_url",
        "occurred", "duration_minutes", "domain",
        "content_hash",
        "status",
    ]
    for key in _field_order:
        if key not in frontmatter:
            continue
        val = frontmatter[key]
        if isinstance(val, str):
            if val == "" or ":" in val or val.startswith(("-", "#", "&", "*")):
                fm_lines.append(f'{key}: "{val}"')
            else:
                fm_lines.append(f"{key}: {val}")
        else:
            fm_lines.append(f"{key}: {val}")
    fm_lines.append("---")

    # Title uses deterministic facts; Claude may adjust it during authoring.
    title_parts = []
    if facts.service_name:
        title_parts.append(facts.service_name)
    title_parts.append("incident")
    if facts.occurred:
        title_parts.append(f"({facts.occurred})")
    title = " ".join(title_parts)

    excerpt = facts.plain_text[:_SOURCE_EXCERPT_CHAR_LIMIT]
    excerpt_truncated = len(facts.plain_text) > _SOURCE_EXCERPT_CHAR_LIMIT

    body_lines = [
        "",
        AGENT_MARKER,
        "",
        f"# {title}",
        "",
        f"_Stub generated by `/ingest` under lens `{LENS_ID}`._",
        "_Fill each section below per `.agent/lenses/engineering-alexander/prompts.md`._",
        "_See `.agent/lenses/engineering-alexander/examples.md` for worked examples._",
        "",
        "<!-- Deterministic facts already extracted into the frontmatter:",
        f"       service_name={facts.service_name!r}",
        f"       occurred={facts.occurred!r}",
        f"       duration_minutes={facts.duration_minutes!r}",
        f"       domain={facts.domain!r}",
        f"       rfc_id={facts.rfc_id!r}, cve_id={facts.cve_id!r}, cwe_id={facts.cwe_id!r}",
        "     Do not contradict these values in the prose unless the source clearly disputes them. -->",
        "",
        "## Narrative",
        "",
        "<!-- Senior SRE post-mortem voice. No hedging. Specific numbers,",
        "     vendor-accurate terminology. 2-4 paragraphs. Ground each claim",
        "     in the source excerpt below or the original URL. -->",
        "",
        "TODO",
        "",
        "## 根因 (Root cause)",
        "",
        "<!-- One paragraph. Single-sentence thesis + 2-3 sentences of",
        "     specific technical detail. If the source names multiple",
        "     contributing factors, call out the primary one and list the",
        "     others as contributors. -->",
        "",
        "TODO",
        "",
        "## 影响 (Impact)",
        "",
        f"- Duration: {facts.duration_minutes if facts.duration_minutes is not None else 'TODO'} min",
        "<!-- Add 1-3 more bullets covering: scope (users affected, regions,",
        "     % of traffic), collateral (downstream systems, customer money),",
        "     recovery window (time to detect, time to mitigate). -->",
        "- TODO",
        "",
        "## 出现的模式 (Patterns observed)",
        "",
        "<!-- List ≥2 [[pattern-slug]] wikilinks that this incident justifies.",
        "     Each pattern must either (a) exist in seed-kit/engineering-alexander/patterns/",
        "     or (b) be marked 'proposed — will be created after a second instance'.",
        "     Do NOT promote a one-instance pattern to a new slug. -->",
        "",
        "- TODO",
        "",
        "## 教训域 (Lesson domains)",
        "",
        "<!-- 1-3 bullets naming which force-atoms this incident strains.",
        "     Use [[force-slug]] wikilinks when the force file already exists.",
        "     Example: [[consistency-vs-availability]], [[recovery-time-vs-redundancy-cost]]. -->",
        "",
        "- TODO",
        "",
        "## Source",
        "",
        f"- Input: `{raw_input}`",
        f"- Type: {input_type}",
        f"- Fetched: {ingested_at}",
        f"- Content hash: {facts.content_hash[:12]}",
        "",
        "<details>",
        f"<summary>Source excerpt ({len(excerpt)} chars{' — truncated' if excerpt_truncated else ''})</summary>",
        "",
        "```",
        excerpt,
        "```",
        "",
        "</details>",
        "",
    ]

    markdown = "\n".join(fm_lines) + "\n" + "\n".join(body_lines)
    return frontmatter, markdown


# ---------------------------------------------------------------------------
# Default HTTP client (lazy) — stdlib only, with SSRF guard
# ---------------------------------------------------------------------------


def _is_private_or_loopback(hostname: str) -> bool:
    """SSRF guard: reject hostnames that resolve to private/loopback IPs."""
    import ipaddress
    import socket
    if not hostname:
        return True
    lower = hostname.lower()
    if lower in ("localhost", "metadata", "metadata.google.internal",
                 "169.254.169.254"):
        return True
    try:
        addrs = socket.getaddrinfo(hostname, None)
    except socket.gaierror:
        return True
    for family, _type, _proto, _canon, sockaddr in addrs:
        ip_str = sockaddr[0]
        try:
            ip = ipaddress.ip_address(ip_str)
        except ValueError:
            continue
        if (ip.is_private or ip.is_loopback or ip.is_link_local
                or ip.is_multicast or ip.is_reserved or ip.is_unspecified):
            return True
    return False


def _default_http_client() -> HTTPClient:
    """Return a stdlib-only HTTP client with an SSRF guard. No new deps."""
    import urllib.request
    from urllib.parse import urlparse

    class _UrllibClient:
        def get(self, url: str, *, timeout: float = 15.0) -> bytes:
            parsed = urlparse(url)
            if parsed.scheme not in ("http", "https"):
                raise ValueError(
                    f"refusing to fetch non-http(s) URL: {url!r}"
                )
            if _is_private_or_loopback(parsed.hostname or ""):
                raise ValueError(
                    f"refusing to fetch private/loopback/metadata URL: "
                    f"{url!r}"
                )
            req = urllib.request.Request(
                url, headers={"User-Agent": "bab-ilu/2.2 incident-extractor"},
            )
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()

    return _UrllibClient()


# ---------------------------------------------------------------------------
# Public entry
# ---------------------------------------------------------------------------


def extract_incident(
    url_or_path: str,
    *,
    vault: Path,
    lens: LensConfig,
    http: Optional[HTTPClient] = None,
    now: Optional[datetime] = None,
) -> IncidentPage | ExtractionError:
    """Fetch, extract, and render one incident stub page.

    Contract:
      - `lens.id` MUST equal `LENS_ID`; else raises ValueError.
      - `url_or_path` MUST classify as "url" or "pdf"; else raises ValueError.
      - Pure transform: no file writes, no journal writes. Caller
        (ingest_runner) is responsible for persisting `markdown` at
        `output_path` and journaling success/failure.
      - Returns IncidentPage on success or ExtractionError on any
        stage failure. Never raises for transient I/O — those become
        ExtractionError with `retriable=True`.
      - No LLM calls. The body ships with structured TODO anchors;
        Claude (the invoking session) fills narrative / root cause /
        impact bullets / pattern wikilinks / lesson bullets in-session
        per the /ingest SKILL.md playbook.
    """
    if lens.id != LENS_ID:
        raise ValueError(
            f"expected lens {LENS_ID!r}, got {lens.id!r} — "
            f"incident_extractor only handles the engineering-alexander lens"
        )
    input_type = _classify_input_type(url_or_path)
    if input_type not in ("url", "pdf"):
        raise ValueError(
            f"incident_extractor only handles url/pdf inputs, "
            f"got {input_type!r} for {url_or_path!r}"
        )

    # Stage 1: fetch.
    try:
        raw_bytes = _fetch(url_or_path, http or _default_http_client())
    except Exception as exc:
        return ExtractionError(
            stage="fetch",
            reason=f"fetch failed: {type(exc).__name__}: {exc}",
            retriable=True,
        )

    # Stage 2: parse to canonical text.
    try:
        if input_type == "url":
            raw_text = _extract_html_text(raw_bytes)
        else:
            raw_text = _extract_pdf_text(raw_bytes)
    except Exception as exc:
        return ExtractionError(
            stage="parse",
            reason=f"parse failed: {type(exc).__name__}: {exc}",
            retriable=False,
        )
    canonical = _canonicalize(raw_text)
    if not canonical.strip():
        return ExtractionError(
            stage="parse",
            reason="parsed body is empty after canonicalization",
            retriable=False,
        )
    facts = _parse_partial_facts(canonical)

    # Stage 3: render (no LLM). Claude fills prose sections in-session.
    slug = _slug_from_input(url_or_path)
    ingested_at = (now or datetime.now(timezone.utc)).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        frontmatter, markdown = _render_page(
            facts, slug, url_or_path, input_type, ingested_at,
        )
    except Exception as exc:
        return ExtractionError(
            stage="render",
            reason=f"render failed: {type(exc).__name__}: {exc}",
            retriable=False,
        )

    tier_0 = lens.entity_model["tier_0"]
    output_path = vault / "wiki" / tier_0 / f"{slug}.md"
    return IncidentPage(
        frontmatter=frontmatter,
        markdown=markdown,
        slug=slug,
        output_path=output_path,
    )


# Small helpers used by the entry point. Duplicated from ingest_runner.py to
# avoid a reverse import cycle.


def _classify_input_type(raw: str) -> str:
    if raw.startswith(("http://", "https://")):
        return "url"
    suffix = Path(raw).suffix.lower()
    if suffix in (".pdf",):
        return "pdf"
    return "unknown"


_SLUG_RE = re.compile(r"[^a-z0-9]+")


def _slug_from_input(raw: str) -> str:
    if raw.startswith(("http://", "https://")):
        parsed = urlparse(raw)
        base = (parsed.netloc + parsed.path).strip("/")
    else:
        base = Path(raw).stem
    lower = base.lower()
    clean = _SLUG_RE.sub("-", lower).strip("-")
    return clean or "untitled"


def _fetch(url_or_path: str, http: HTTPClient) -> bytes:
    if url_or_path.startswith(("http://", "https://")):
        return http.get(url_or_path)
    p = Path(url_or_path)
    if not p.exists():
        raise FileNotFoundError(f"input not found: {url_or_path}")
    return p.read_bytes()
