"""Tests for tools/incident_extractor.py — Claude-drive rewrite (v2.2).

The prior LLM-merge path has been removed (see ADR in the module
docstring). Tests now cover:

  - 9 primitives (canonicalize, hash, fact parsers)
  - 3 HTML/PDF extraction
  - 3 stub render (deterministic-only — no LLM merge)
  - 3 golden-fixture e2e — deterministic fields only
  - 2 boundary + integration (wrong lens, ingest_one journal)

All tests replay frozen HTML/PDF fixtures — no live HTTP.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from tests._mocks import MockHTTPClient
from tools.incident_extractor import (
    ALLOWED_DOMAINS,
    AGENT_MARKER,
    ExtractionError,
    IncidentPage,
    LENS_ID,
    PartialFacts,
    _canonicalize,
    _classify_domain,
    _content_hash,
    _extract_html_text,
    _extract_pdf_text,
    _normalize_service_name,
    _parse_date,
    _parse_duration_minutes,
    _parse_partial_facts,
    _render_page,
    extract_incident,
)
from tools.lens_loader import load_all_lenses


FIXTURES = Path(__file__).parent / "fixtures" / "incident_extractor"


@pytest.fixture(scope="module")
def engineering_lens():
    """Load the real engineering-alexander lens config."""
    lenses = load_all_lenses()
    return lenses["engineering-alexander"]


@pytest.fixture(scope="module")
def aesthetic_lens():
    """Load a non-engineering lens for the boundary test."""
    lenses = load_all_lenses()
    return lenses["aesthetic-warburg"]


def _make_facts(**kwargs) -> PartialFacts:
    defaults = dict(
        service_name=None, occurred=None, duration_minutes=None,
        domain=None, rfc_id=None, cve_id=None, cwe_id=None,
        content_hash="deadbeef", plain_text="",
    )
    defaults.update(kwargs)
    return PartialFacts(**defaults)


# ---------------------------------------------------------------------------
# 1-9 : extraction primitives (pure / deterministic)
# ---------------------------------------------------------------------------


class TestPrimitives:
    def test_canonicalize_strips_timestamps_and_whitespace(self):
        raw = (
            "As of 2024-01-01 this post has been viewed 500k times.\n"
            "  Real content line.  \n"
            "\u00a0Another line.   \n"
        )
        out = _canonicalize(raw)
        assert "As of 2024" not in out
        assert "\u00a0" not in out
        assert "500k times" not in out
        assert "Real content line." in out
        for line in out.splitlines():
            assert line == line.rstrip()

    def test_canonicalize_is_deterministic(self):
        raw = "First line.\nSecond line.\n"
        assert _content_hash(_canonicalize(raw)) == _content_hash(_canonicalize(raw))

    def test_content_hash_stable_across_whitespace_drift(self):
        a = "First line.\nSecond line.\n"
        b = "First line.\r\nSecond line.\r\n"
        c = "First line.   \nSecond line.\n"
        ha = _content_hash(_canonicalize(a))
        hb = _content_hash(_canonicalize(b))
        hc = _content_hash(_canonicalize(c))
        assert ha == hb == hc

    def test_parse_partial_facts_extracts_iso_date_from_prose(self):
        facts = _parse_partial_facts(_canonicalize("The outage began on July 2, 2019 at 13:42 UTC."))
        assert facts.occurred == "2019-07-02"

    def test_parse_partial_facts_extracts_duration_minutes_short_form(self):
        facts = _parse_partial_facts(_canonicalize("The event lasted for 27 minutes."))
        assert facts.duration_minutes == 27

    def test_parse_partial_facts_extracts_duration_hours(self):
        facts = _parse_partial_facts(_canonicalize("Restoration took approximately 4 hours in total."))
        assert facts.duration_minutes == 240

    def test_parse_partial_facts_normalizes_service_name(self):
        assert _normalize_service_name("Amazon S3 experienced an outage") == "Amazon S3"
        assert _normalize_service_name("nobody famous here") is None
        assert _normalize_service_name("Cloudflare blog post") == "Cloudflare"

    def test_parse_partial_facts_classifies_domain_by_keywords(self):
        assert _classify_domain("A BGP routing misconfiguration") == "network"
        assert _classify_domain("The binary rollout was canceled") == "deployment"
        assert _classify_domain("Postgres database ate the data") == "storage"
        assert _classify_domain("no matching keywords whatsoever") is None

    def test_parse_partial_facts_detects_cve_and_rfc_ids(self):
        text = _canonicalize(
            "We were hit by CVE-2021-44228 (log4j), which violates RFC 9110 section 2."
        )
        facts = _parse_partial_facts(text)
        assert facts.cve_id == "CVE-2021-44228"
        assert facts.rfc_id == "RFC 9110"


# ---------------------------------------------------------------------------
# 10-12: HTML / PDF extraction
# ---------------------------------------------------------------------------


class TestExtraction:
    def test_extract_html_text_from_cloudflare_fixture(self):
        html = (FIXTURES / "cloudflare-2019" / "raw.html").read_bytes()
        text = _extract_html_text(html)
        assert "catastrophic backtracking" in text
        assert "27 minutes" in text
        assert "Home | Blog | Contact" not in text
        assert "Related posts" not in text
        assert "sign up for the newsletter" not in text
        assert "var tracking" not in text

    def test_extract_html_text_unknown_structure_falls_back_to_body_text(self):
        html = b"<html><body><div>Unstructured incident narrative here.</div></body></html>"
        text = _extract_html_text(html)
        assert "Unstructured incident narrative here." in text

    def test_extract_pdf_text_from_pre_extracted_text_fixture(self, tmp_path):
        frozen_text = "Knight Capital lost approximately 460 million dollars on 2012-08-01.\n"
        out = _extract_pdf_text(frozen_text.encode("utf-8"))
        assert "Knight Capital" in out
        assert "2012-08-01" in out


# ---------------------------------------------------------------------------
# 13-15: stub render (Claude-drive — no LLM merge)
# ---------------------------------------------------------------------------


class TestStubRender:
    """The render path under the Claude-drive architecture: frontmatter is
    populated from PartialFacts (deterministic); body has structured TODO
    anchors + canonical-text excerpt for Claude to author prose against.
    """

    def test_render_page_fills_frontmatter_from_partial_facts(self):
        facts = _make_facts(
            service_name="TestVendor",
            occurred="2020-01-02",
            duration_minutes=30,
            domain="network",
            rfc_id="RFC 9110",
            content_hash="abc123def4567890",
            plain_text="Lorem ipsum canonical text.\n",
        )
        fm, md = _render_page(
            facts, slug="test-slug", raw_input="https://example.com/x",
            input_type="url", ingested_at="2026-04-22T00:00:00Z",
        )
        # Frontmatter deterministic anchors present and populated.
        assert fm["type"] == "incident"
        assert fm["lens"] == LENS_ID
        assert fm["slug"] == "test-slug"
        assert fm["postmortem_url"] == "https://example.com/x"
        assert fm["source_url"] == "https://example.com/x"
        assert fm["status"] == "draft"
        assert fm["service_name"] == "TestVendor"
        assert fm["occurred"] == "2020-01-02"
        assert fm["duration_minutes"] == 30
        assert fm["domain"] == "network"
        assert fm["rfc_id"] == "RFC 9110"
        assert fm["cve_id"] == ""
        assert fm["cwe_id"] == ""
        assert fm["content_hash"] == "abc123def4567890"

    def test_render_page_produces_required_body_landmarks(self):
        facts = _make_facts(
            service_name="TestVendor", occurred="2020-01-02",
            duration_minutes=30, domain="network",
            content_hash="abc123def4567890",
            plain_text="Short canonical text.\n",
        )
        _, md = _render_page(
            facts, slug="test-slug", raw_input="https://example.com/x",
            input_type="url", ingested_at="2026-04-22T00:00:00Z",
        )
        # Agent marker so ingest_runner can distinguish stub vs user content.
        assert AGENT_MARKER in md
        # Title uses deterministic service_name + occurred.
        assert "# TestVendor incident (2020-01-02)" in md
        # Required body landmarks — /lint and the E2 pattern extractor
        # read these as stable insertion points.
        assert "## Narrative" in md
        assert "## 根因 (Root cause)" in md
        assert "## 影响 (Impact)" in md
        assert "## 出现的模式 (Patterns observed)" in md
        assert "## 教训域 (Lesson domains)" in md
        assert "## Source" in md
        # Duration bullet is pre-filled deterministically.
        assert "- Duration: 30 min" in md
        # Content-hash anchor present for drift detection.
        assert "- Content hash: abc123def456" in md
        # TODO anchors tell Claude where to fill prose.
        assert "TODO" in md

    def test_render_page_embeds_source_excerpt_for_claude(self):
        """The stub body must include the canonical source text so the
        authoring Claude has material to ground its prose in. Excerpt is
        capped so the stub stays readable."""
        long_text = "Line of post-mortem prose. " * 500  # ~13500 chars
        facts = _make_facts(
            service_name="VendorX", occurred="2024-01-01",
            duration_minutes=10, domain="runtime",
            content_hash="hash1234567890",
            plain_text=long_text,
        )
        _, md = _render_page(
            facts, slug="vendorx-2024", raw_input="https://example.com/postmortem",
            input_type="url", ingested_at="2026-04-22T00:00:00Z",
        )
        assert "<details>" in md
        assert "<summary>Source excerpt" in md
        assert "truncated" in md  # long_text exceeds the cap
        # Excerpt preserves prose (not a hash-only reference).
        assert "Line of post-mortem prose." in md

    def test_render_page_handles_missing_deterministic_facts(self):
        """When regex passes extract nothing, the stub still renders
        cleanly with empty-string anchors — /lint treats '' as 'checked
        and not found' rather than 'never examined'."""
        facts = _make_facts(content_hash="emptyhash", plain_text="n/a\n")
        fm, md = _render_page(
            facts, slug="nothing", raw_input="https://example.com/blank",
            input_type="url", ingested_at="2026-04-22T00:00:00Z",
        )
        assert fm["service_name"] == ""
        assert fm["occurred"] == ""
        assert fm["duration_minutes"] == 0
        assert fm["domain"] == ""
        # Title still renders (just without the missing pieces).
        assert "incident" in md
        # Duration bullet shows TODO rather than a bogus zero.
        assert "- Duration: TODO min" in md


# ---------------------------------------------------------------------------
# 16-18: golden-fixture e2e (deterministic fields only — no LLM)
# ---------------------------------------------------------------------------


class TestGoldenFixturesE2E:
    def _run(self, slug: str, url: str, engineering_lens, tmp_path):
        html_bytes = (FIXTURES / slug / "raw.html").read_bytes()
        http = MockHTTPClient({url: html_bytes})
        result = extract_incident(
            url, vault=tmp_path, lens=engineering_lens, http=http,
        )
        return result

    def test_extract_incident_cloudflare_2019_end_to_end(self, engineering_lens, tmp_path):
        result = self._run(
            "cloudflare-2019",
            "https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/",
            engineering_lens, tmp_path,
        )
        assert isinstance(result, IncidentPage)
        # Deterministic anchors extracted directly from the HTML.
        assert result.frontmatter["service_name"] == "Cloudflare"
        assert result.frontmatter["occurred"] == "2019-07-02"
        assert result.frontmatter["duration_minutes"] == 27
        assert result.frontmatter["domain"] == "network"
        assert result.frontmatter["rfc_id"] == "RFC 9110"
        assert result.frontmatter["cve_id"] == ""
        # Path respects lens.entity_model.tier_0 ("incident" singular).
        assert result.output_path == tmp_path / "wiki" / "incident" / f"{result.slug}.md"
        # Body has the expected structural anchors.
        assert "## 根因 (Root cause)" in result.markdown
        assert AGENT_MARKER in result.markdown

    def test_extract_incident_gitlab_2017_end_to_end(self, engineering_lens, tmp_path):
        result = self._run(
            "gitlab-2017",
            "https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/",
            engineering_lens, tmp_path,
        )
        assert isinstance(result, IncidentPage)
        assert result.frontmatter["service_name"] == "GitLab.com"
        assert result.frontmatter["occurred"] == "2017-01-31"
        assert result.frontmatter["duration_minutes"] == 360
        assert result.frontmatter["domain"] == "storage"
        assert "## 根因 (Root cause)" in result.markdown

    def test_extract_incident_aws_s3_2017_end_to_end(self, engineering_lens, tmp_path):
        result = self._run(
            "aws-s3-2017",
            "https://aws.amazon.com/message/41926/",
            engineering_lens, tmp_path,
        )
        assert isinstance(result, IncidentPage)
        assert result.frontmatter["service_name"] == "Amazon S3"
        assert result.frontmatter["occurred"] == "2017-02-28"
        assert result.frontmatter["duration_minutes"] == 240
        assert result.frontmatter["domain"] == "storage"
        assert result.frontmatter["domain"] in ALLOWED_DOMAINS


# ---------------------------------------------------------------------------
# 19-20: boundary + integration
# ---------------------------------------------------------------------------


class TestBoundaryAndIntegration:
    def test_extract_incident_rejects_wrong_lens(self, aesthetic_lens, tmp_path):
        http = MockHTTPClient({})
        with pytest.raises(ValueError, match="engineering-alexander"):
            extract_incident(
                "https://example.com/x", vault=tmp_path,
                lens=aesthetic_lens, http=http,
            )

    def test_extract_incident_returns_extraction_error_on_fetch_failure(
        self, engineering_lens, tmp_path,
    ):
        """Fetch failures surface as ExtractionError(retriable=True) — the
        caller (ingest_runner) journals them as ingest.fail, not as an
        uncaught exception."""

        class FailingHTTP:
            def get(self, url, *, timeout=15.0):
                raise TimeoutError("simulated network stall")

        result = extract_incident(
            "https://example.com/x", vault=tmp_path, lens=engineering_lens,
            http=FailingHTTP(),
        )
        assert isinstance(result, ExtractionError)
        assert result.stage == "fetch"
        assert result.retriable is True

    def test_extract_incident_returns_extraction_error_on_empty_body(
        self, engineering_lens, tmp_path,
    ):
        """Empty canonical bodies surface as a non-retriable parse error
        rather than writing an empty stub."""
        http = MockHTTPClient({
            "https://example.com/empty": b"<html><body></body></html>"
        })
        result = extract_incident(
            "https://example.com/empty", vault=tmp_path,
            lens=engineering_lens, http=http,
        )
        assert isinstance(result, ExtractionError)
        assert result.stage == "parse"
        assert result.retriable is False

    def test_ingest_one_incident_extractor_journal_integration(
        self, engineering_lens, tmp_path, monkeypatch,
    ):
        """ingest_one dispatches to incident_extractor for engineering lens URLs
        and journals success with extractor-tag; rerunning is idempotent."""
        from tools import ingest_runner

        url = (
            "https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/"
        )
        html_bytes = (FIXTURES / "cloudflare-2019" / "raw.html").read_bytes()

        http = MockHTTPClient({url: html_bytes})
        monkeypatch.setattr(
            "tools.incident_extractor._default_http_client", lambda: http,
        )

        vault = tmp_path
        results = ingest_runner.run_ingest(vault, engineering_lens, [url])
        assert len(results) == 1
        rec = results[0]
        assert rec["action"] == "ingest.success", rec
        assert rec.get("extractor") == "incident_extractor"

        out_path = vault / rec["outputs"][0]
        body = out_path.read_text(encoding="utf-8")
        assert "## 根因 (Root cause)" in body
        assert "service_name: Cloudflare" in body

        log_lines = (vault / "wiki" / "_log" / "usage.jsonl").read_text().splitlines()
        assert any(
            json.loads(line).get("lens") == LENS_ID for line in log_lines
        )

        # Idempotency: second run is a no-op.
        results2 = ingest_runner.run_ingest(vault, engineering_lens, [url])
        assert results2[0]["action"] == "ingest.skip"
        assert results2[0].get("reason") == "already-success"
