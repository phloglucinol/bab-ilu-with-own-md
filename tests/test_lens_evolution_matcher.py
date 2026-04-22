"""Tests for tools/lens_evolution/matcher.py — Track L MVP.

These tests cover the PURE-FUNCTION surface of the matcher module.
The matcher module does NOT call any LLM — Claude (the Bab-ilu
session agent) does the reasoning under SKILL.md. Tests therefore
focus on:

  - Prompt construction (digest → prompt text)
  - Response parsing (well-formed JSON → TheoryCandidate)
  - Error paths (missing fields, <2 structural_elements, malformed JSON)
  - `null` response parses as `None` (valid "no theory matches yet")
"""

from __future__ import annotations

import json

import pytest

from pathlib import Path

from tools.lens_evolution.matcher import (
    MatcherError,
    TheoryCandidate,
    build_matcher_prompt,
    discover_installed_lenses,
    parse_candidate,
)
from tools.lens_evolution.observer import ObserverDigest


def _sample_digest() -> ObserverDigest:
    return ObserverDigest(
        recent_entity_names=[
            "reflection-in-action",
            "knowing-in-action",
            "practice-moments",
            "case-methods-archive",
        ],
        recent_queries=[
            "how does expertise manifest without explicit rules",
            "tacit knowledge in engineering decisions",
        ],
        recent_ingest_types=["pdf", "pdf", "article"],
        wikilink_edges=[["case-methods-archive", "reflection-in-action"]],
        total_events=20,
        first_event_ts="2026-04-01T00:00:00Z",
        last_event_ts="2026-04-20T00:00:00Z",
    )


def _valid_candidate_json(**overrides) -> str:
    payload = {
        "theory_name": "Reflection-on-action (Schön)",
        "author": "Donald A. Schön",
        "year": 1983,
        "primary_source": "The Reflective Practitioner",
        "core_concept": "reflection-on-action",
        "why_matches": (
            "The user's recent entities and queries "
            "center on tacit knowledge becoming visible through "
            "case-based retrospection — precisely Schön's frame."
        ),
        "structural_elements": [
            "knowing-in-action",
            "reflection-in-action",
            "reflection-on-action",
        ],
        "confidence": 0.78,
    }
    payload.update(overrides)
    return json.dumps(payload)


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------


class TestBuildMatcherPrompt:

    def test_prompt_contains_rigor_bar(self):
        prompt = build_matcher_prompt(_sample_digest())
        assert "瓦尔堡" in prompt or "Warburg" in prompt
        assert "null" in prompt  # refusal path is named
        assert "thirty years" in prompt or "30 years" in prompt.lower()

    def test_prompt_includes_behavioral_digest_content(self):
        prompt = build_matcher_prompt(_sample_digest())
        assert "reflection-in-action" in prompt
        assert "tacit knowledge" in prompt
        assert "pdf" in prompt

    def test_prompt_lists_accepted_and_rejected_history(self):
        digest = _sample_digest()
        digest.accepted_hypotheses = [
            {"theory": "Polanyi — tacit knowledge",
             "citation_ref": "Polanyi 1966"},
        ]
        digest.rejected_hypotheses = [
            {"theory": "Some pop framework",
             "citation_ref": "Medium 2023",
             "reason": "no academic citation"},
        ]
        prompt = build_matcher_prompt(digest)
        assert "ALREADY ACCEPTED" in prompt
        assert "Polanyi" in prompt
        assert "ALREADY REJECTED" in prompt
        assert "Medium 2023" in prompt
        assert "no academic citation" in prompt

    def test_prompt_excludes_directive_language(self):
        """No part of the prompt should accept user direction — this is
        the 'behavior over declaration' contract (PRD §0.5.3 principle 5)
        verified at the prompt-shape level."""
        digest = _sample_digest()
        prompt = build_matcher_prompt(digest)
        # None of the strings the digest tracks should be called
        # "user_intent" or "preferred_direction" or similar.
        forbidden = ["user_intent", "preferred_theory", "bias_toward",
                     "requested_direction"]
        for f in forbidden:
            assert f not in prompt, (
                f"Prompt contains directive-shaped key {f!r} — this "
                "violates the behavioral-only contract."
            )


# ---------------------------------------------------------------------------
# Response parsing
# ---------------------------------------------------------------------------


class TestParseCandidate:

    def test_parses_well_formed_json(self):
        cand = parse_candidate(_valid_candidate_json())
        assert isinstance(cand, TheoryCandidate)
        assert cand.author == "Donald A. Schön"
        assert cand.year == 1983
        assert cand.citation_ref == (
            "Donald A. Schön (1983), The Reflective Practitioner"
        )
        assert len(cand.structural_elements) == 3
        assert 0 <= cand.confidence <= 1

    def test_null_response_returns_none(self):
        assert parse_candidate("null") is None
        assert parse_candidate("None") is None
        assert parse_candidate("  null  ") is None

    def test_empty_response_returns_none(self):
        assert parse_candidate("") is None

    def test_tolerates_code_fence(self):
        wrapped = f"```json\n{_valid_candidate_json()}\n```"
        cand = parse_candidate(wrapped)
        assert cand is not None
        assert cand.author == "Donald A. Schön"

    def test_rejects_missing_required_field(self):
        # missing core_concept
        payload = json.loads(_valid_candidate_json())
        del payload["core_concept"]
        with pytest.raises(MatcherError, match="missing required field"):
            parse_candidate(json.dumps(payload))

    def test_rejects_fewer_than_three_structural_elements(self):
        bad = _valid_candidate_json(
            structural_elements=["only-one"],
        )
        with pytest.raises(MatcherError, match="structural_elements"):
            parse_candidate(bad)

    def test_rejects_non_integer_year(self):
        bad = _valid_candidate_json(year="not-a-year")
        with pytest.raises(MatcherError, match="year must be"):
            parse_candidate(bad)

    def test_rejects_outright_malformed_json(self):
        with pytest.raises(MatcherError, match="non-JSON"):
            parse_candidate("this is not JSON at all")

    def test_extracts_json_from_surrounding_prose(self):
        # Defense: model sometimes ignores "no prose" and adds commentary.
        noisy = "Here is my analysis:\n" + _valid_candidate_json() + "\nHope that helps."
        cand = parse_candidate(noisy)
        assert cand is not None

    def test_clamps_invalid_confidence(self):
        bad = _valid_candidate_json(confidence=1.5)
        cand = parse_candidate(bad)
        assert cand is not None
        assert cand.confidence == 1.0


# ---------------------------------------------------------------------------
# Round-trip: build_matcher_prompt → Claude (simulated) → parse_candidate
# ---------------------------------------------------------------------------


class TestDiscoverInstalledLenses:
    """Closes the FTG-test architecture gap 2026-04-21 — matcher must
    know about lenses already installed on the vault (pre-installed
    or previously evolved) so it doesn't re-propose them."""

    def _seed_lens(self, vault: Path, lens_id: str, name: str,
                   origin_theory: str = "", origin_author: str = ""):
        lens_dir = vault / ".agent" / "lenses" / lens_id
        lens_dir.mkdir(parents=True, exist_ok=True)
        yaml_body = f'id: {lens_id}\nname: "{name}"\n'
        if origin_theory or origin_author:
            yaml_body += "extensions:\n  candidate:\n"
            if origin_theory:
                yaml_body += f'    origin_theory: "{origin_theory}"\n'
            if origin_author:
                yaml_body += f'    origin_author: "{origin_author}"\n'
        (lens_dir / "lens.yaml").write_text(yaml_body, encoding="utf-8")

    def test_missing_vault_returns_empty(self, tmp_path: Path):
        assert discover_installed_lenses(tmp_path / "nowhere") == []

    def test_none_vault_returns_empty(self):
        assert discover_installed_lenses(None) == []

    def test_empty_lenses_dir_returns_empty(self, tmp_path: Path):
        (tmp_path / ".agent" / "lenses").mkdir(parents=True)
        assert discover_installed_lenses(tmp_path) == []

    def test_discovers_single_pre_installed_lens(self, tmp_path: Path):
        self._seed_lens(tmp_path, "aesthetic-warburg",
                        "Warburg Pathosformel")
        result = discover_installed_lenses(tmp_path)
        assert len(result) == 1
        assert result[0]["id"] == "aesthetic-warburg"
        assert "Warburg" in result[0]["name"]

    def test_ignores_active_pointer_dir(self, tmp_path: Path):
        self._seed_lens(tmp_path, "real-lens", "Real")
        (tmp_path / ".agent/lenses/active").mkdir()
        result = discover_installed_lenses(tmp_path)
        assert len(result) == 1
        assert result[0]["id"] == "real-lens"

    def test_discovers_multiple_lenses(self, tmp_path: Path):
        self._seed_lens(tmp_path, "aesthetic-warburg", "Warburg")
        self._seed_lens(tmp_path, "engineering-alexander", "Alexander")
        self._seed_lens(tmp_path, "general-zettelkasten", "Zettelkasten")
        result = discover_installed_lenses(tmp_path)
        ids = {r["id"] for r in result}
        assert ids == {"aesthetic-warburg", "engineering-alexander",
                       "general-zettelkasten"}

    def test_surfaces_candidate_metadata_when_present(self, tmp_path: Path):
        self._seed_lens(
            tmp_path, "schon-knowing-in-action",
            "Reflection-on-action (Schön)",
            origin_theory="Reflection-on-action (Schön)",
            origin_author="Donald A. Schön",
        )
        result = discover_installed_lenses(tmp_path)
        assert result[0]["origin_theory"] == "Reflection-on-action (Schön)"
        assert result[0]["origin_author"] == "Donald A. Schön"

    def test_malformed_lens_yaml_skipped_silently(self, tmp_path: Path):
        bad = tmp_path / ".agent/lenses/bad-lens"
        bad.mkdir(parents=True)
        (bad / "lens.yaml").write_text("{ this is : not ] valid yaml: [",
                                        encoding="utf-8")
        self._seed_lens(tmp_path, "good-lens", "Good")
        result = discover_installed_lenses(tmp_path)
        assert len(result) == 1
        assert result[0]["id"] == "good-lens"

    def test_build_matcher_prompt_includes_installed_lenses(
        self, tmp_path: Path,
    ):
        self._seed_lens(
            tmp_path, "aesthetic-warburg",
            "Warburg Pathosformel",
            origin_theory="Warburg Pathosformel",
            origin_author="Aby Warburg",
        )
        digest = _sample_digest()
        prompt = build_matcher_prompt(digest, vault=tmp_path)
        assert "ALREADY-INSTALLED LENSES" in prompt
        assert "aesthetic-warburg" in prompt
        assert "Aby Warburg" in prompt


class TestMatcherRoundTrip:
    """Simulates the Claude-driven flow by producing a prompt, feigning
    Claude's response, and parsing it. No LLM call — Claude's role is
    represented by the `simulated_response` string."""

    def test_populated_digest_produces_parseable_candidate(self):
        prompt = build_matcher_prompt(_sample_digest())
        assert len(prompt) > 100  # Prompt was actually built
        # Claude (under SKILL.md) would read `prompt` and emit:
        simulated_response = _valid_candidate_json()
        candidate = parse_candidate(simulated_response)
        assert isinstance(candidate, TheoryCandidate)
        assert candidate.author == "Donald A. Schön"

    def test_null_response_survives_roundtrip(self):
        prompt = build_matcher_prompt(_sample_digest())
        assert len(prompt) > 0
        # Claude declines at the rigor bar:
        assert parse_candidate("null") is None

    def test_parse_catches_malformed_simulated_response(self):
        with pytest.raises(MatcherError):
            parse_candidate("garbage non-json")
