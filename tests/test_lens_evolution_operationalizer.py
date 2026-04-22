"""Tests for tools/lens_evolution/operationalizer.py — Track L MVP.

Post-refactor (2026-04-21, Phoenix correction): operationalize()
takes Claude-authored `prompts_md` and `examples_md` strings directly.
No LLM call happens in this module. Tests pass canned markdown.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pytest

from tools.lens_evolution.matcher import TheoryCandidate
from tools.lens_evolution.operationalizer import (
    OperationalizationError,
    lens_id_for_theory,
    operationalize,
    render_examples_instructions,
    render_prompts_instructions,
)
from tools.lens_evolution.verifier import VerificationResult


def _candidate(**overrides) -> TheoryCandidate:
    base = dict(
        theory_name="Reflection-on-action (Schön)",
        author="Donald A. Schön",
        year=1983,
        primary_source="The Reflective Practitioner",
        core_concept="reflection-on-action",
        why_matches="sample why",
        structural_elements=[
            "knowing-in-action",
            "reflection-in-action",
            "reflection-on-action",
        ],
        confidence=0.8,
    )
    base.update(overrides)
    return TheoryCandidate(**base)


def _confirmed() -> VerificationResult:
    return VerificationResult(
        status="confirmed",
        reasoning="standard citation",
        raw_response="",
    )


def _uncertain() -> VerificationResult:
    return VerificationResult(
        status="uncertain",
        reasoning="not sure",
        raw_response="",
    )


def _rejected() -> VerificationResult:
    return VerificationResult(
        status="rejected",
        reasoning="no such book",
        raw_response="",
    )


# Minimal Claude-authored markdown — in real use Claude writes these
# with richer content guided by render_*_instructions().
PROMPTS_MD_SAMPLE = (
    "## Tone\n"
    "Write with attention to hidden frames.\n\n"
    "## Rubrics\n"
    "- What tacit frame applies?\n\n"
    "## Traps\n"
    "- Don't conflate reflection-on-action with ordinary hindsight.\n"
)

EXAMPLES_MD_SAMPLE = (
    "## Example 1\n"
    "A debugging session that shifts mental models mid-trace.\n"
)


def _happy_kwargs():
    """Default kwargs for a successful operationalize call."""
    return dict(
        prompts_md=PROMPTS_MD_SAMPLE,
        examples_md=EXAMPLES_MD_SAMPLE,
        today=date(2026, 4, 21),
    )


# ---------------------------------------------------------------------------
# Lens id derivation
# ---------------------------------------------------------------------------


class TestLensIdDerivation:

    def test_ascii_surname_and_concept(self):
        c = _candidate()
        assert lens_id_for_theory(c) == "schon-knowing-in-action"

    def test_non_ascii_author_folded(self):
        c = _candidate(author="Donald A. Schön")
        assert lens_id_for_theory(c) == "schon-knowing-in-action"


# ---------------------------------------------------------------------------
# Instruction rendering (what Claude reads before authoring markdown)
# ---------------------------------------------------------------------------


class TestRenderInstructions:

    def test_prompts_instructions_include_theory_context(self):
        text = render_prompts_instructions(_candidate())
        assert "Reflection-on-action (Schön)" in text
        assert "Donald A. Schön" in text
        assert "1983" in text
        # Rigor gate language carried into the instructions
        assert "primary source" in text.lower()

    def test_examples_instructions_include_structural_elements(self):
        text = render_examples_instructions(_candidate())
        for elem in ("knowing-in-action", "reflection-in-action",
                     "reflection-on-action"):
            assert elem in text

    def test_instructions_warn_against_inventing_concepts(self):
        text = render_prompts_instructions(_candidate())
        assert "not from the primary source" in text.lower() or (
            "not from this theory" in text.lower()
        )


# ---------------------------------------------------------------------------
# Safety gates
# ---------------------------------------------------------------------------


class TestOperationalizeSafety:

    def test_uncertain_verification_refused(self, tmp_path: Path):
        with pytest.raises(OperationalizationError, match="status"):
            operationalize(
                _candidate(), _uncertain(), tmp_path, **_happy_kwargs(),
            )

    def test_rejected_verification_refused(self, tmp_path: Path):
        with pytest.raises(OperationalizationError, match="status"):
            operationalize(
                _candidate(), _rejected(), tmp_path, **_happy_kwargs(),
            )

    def test_too_few_structural_elements_refused(self, tmp_path: Path):
        bad = _candidate(structural_elements=["only-one"])
        with pytest.raises(OperationalizationError, match="structural"):
            operationalize(
                bad, _confirmed(), tmp_path, **_happy_kwargs(),
            )

    def test_empty_prompts_md_refused(self, tmp_path: Path):
        kwargs = _happy_kwargs()
        kwargs["prompts_md"] = ""
        with pytest.raises(OperationalizationError, match="prompts_md"):
            operationalize(_candidate(), _confirmed(), tmp_path, **kwargs)

    def test_empty_examples_md_refused(self, tmp_path: Path):
        kwargs = _happy_kwargs()
        kwargs["examples_md"] = "   \n\n  "
        with pytest.raises(OperationalizationError, match="examples_md"):
            operationalize(_candidate(), _confirmed(), tmp_path, **kwargs)

    def test_low_confidence_candidate_refused(self, tmp_path: Path):
        bad = _candidate(confidence=0.2)
        with pytest.raises(OperationalizationError, match="confidence"):
            operationalize(bad, _confirmed(), tmp_path, **_happy_kwargs())

    def test_existing_lens_dir_not_overwritten_by_default(
        self, tmp_path: Path,
    ):
        operationalize(
            _candidate(), _confirmed(), tmp_path, **_happy_kwargs(),
        )
        with pytest.raises(OperationalizationError, match="already exists"):
            operationalize(
                _candidate(), _confirmed(), tmp_path, **_happy_kwargs(),
            )

    def test_overwrite_flag_permits_regeneration(self, tmp_path: Path):
        operationalize(
            _candidate(), _confirmed(), tmp_path,
            prompts_md="## Tone\nv1\n## Rubrics\n- a\n## Traps\n- b\n",
            examples_md="## Example\nv1 example\n",
            today=date(2026, 4, 21),
        )
        result = operationalize(
            _candidate(), _confirmed(), tmp_path,
            prompts_md="## Tone\nv2\n## Rubrics\n- a\n## Traps\n- b\n",
            examples_md="## Example\nv2 example\n",
            today=date(2026, 4, 21),
            overwrite=True,
        )
        prompts = (result.lens_dir / "prompts.md").read_text()
        assert "v2" in prompts and "v1" not in prompts


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------


class TestOperationalizeHappyPath:

    def test_produces_four_files(self, tmp_path: Path):
        result = operationalize(
            _candidate(), _confirmed(), tmp_path, **_happy_kwargs(),
        )
        assert len(result.files_written) == 4
        names = {p.name for p in result.files_written}
        assert names == {
            "lens.yaml", "prompts.md", "examples.md", "candidate.json",
        }

    def test_lens_yaml_has_required_v21_keys(self, tmp_path: Path):
        result = operationalize(
            _candidate(), _confirmed(), tmp_path, **_happy_kwargs(),
        )
        yaml_text = (result.lens_dir / "lens.yaml").read_text()
        assert "id: schon-knowing-in-action" in yaml_text
        assert "entity_model:" in yaml_text
        assert "tier_0:" in yaml_text
        assert "tier_1_atom:" in yaml_text
        assert "tier_1_cluster:" in yaml_text
        assert "version:" in yaml_text
        # Candidate status explicit
        assert "candidate" in yaml_text

    def test_candidate_json_records_verification(self, tmp_path: Path):
        result = operationalize(
            _candidate(), _confirmed(), tmp_path, **_happy_kwargs(),
        )
        meta = json.loads(
            (result.lens_dir / "candidate.json").read_text()
        )
        assert meta["status"] == "candidate"
        assert meta["theory"]["author"] == "Donald A. Schön"
        assert meta["verification"]["status"] == "confirmed"

    def test_structural_elements_map_to_entity_model(self, tmp_path: Path):
        result = operationalize(
            _candidate(), _confirmed(), tmp_path, **_happy_kwargs(),
        )
        yaml_text = (result.lens_dir / "lens.yaml").read_text()
        assert "tier_0: knowing-in-action" in yaml_text
        assert "tier_1_atom: reflection-in-action" in yaml_text
        assert "tier_1_cluster: reflection-on-action" in yaml_text

    def test_native_structural_model_preserved(self, tmp_path: Path):
        """Architecture-audit fix: the native structural model is in
        extensions.candidate.structural_model regardless of tier layout."""
        result = operationalize(
            _candidate(), _confirmed(), tmp_path, **_happy_kwargs(),
        )
        yaml_text = (result.lens_dir / "lens.yaml").read_text()
        assert "structural_model:" in yaml_text

    def test_extra_structural_elements_preserved_in_extensions(
        self, tmp_path: Path,
    ):
        c = _candidate(structural_elements=[
            "a-tier0", "b-atom", "c-cluster", "d-extra", "e-extra",
        ])
        result = operationalize(
            c, _confirmed(), tmp_path, **_happy_kwargs(),
        )
        yaml_text = (result.lens_dir / "lens.yaml").read_text()
        assert "elements_outside_compat_shim" in yaml_text
        assert "d-extra" in yaml_text
        assert "e-extra" in yaml_text

    def test_two_element_theory_handled_without_fake_cluster(
        self, tmp_path: Path,
    ):
        """Principle 2 (family resemblance): a 2-element theory like
        Polanyi's tacit/explicit must not be forced into a false 3rd tier."""
        c = _candidate(structural_elements=["tacit", "explicit"])
        result = operationalize(
            c, _confirmed(), tmp_path, **_happy_kwargs(),
        )
        yaml_text = (result.lens_dir / "lens.yaml").read_text()
        # Synthetic cluster name is present as compat shim but labeled honestly
        assert "synthetic" in yaml_text or "compatibility_shim_applied: true" in yaml_text
        # Native view carries both poles
        assert "tacit:" in yaml_text
        assert "explicit:" in yaml_text

    def test_claude_authored_prompts_md_written_verbatim(
        self, tmp_path: Path,
    ):
        result = operationalize(
            _candidate(), _confirmed(), tmp_path, **_happy_kwargs(),
        )
        prompts = (result.lens_dir / "prompts.md").read_text()
        # Canary text from _happy_kwargs()
        assert "attention to hidden frames" in prompts
        examples = (result.lens_dir / "examples.md").read_text()
        assert "mid-trace" in examples

    def test_yaml_injection_defense_strips_llm_newlines(
        self, tmp_path: Path,
    ):
        """CRITICAL fix from code review: LLM-sourced string containing
        a literal newline must not bleed into PARSED top-level YAML keys.

        The sanitizer replaces newlines with spaces — so the hostile
        fragment 'malicious_key: MALICIOUS_VALUE' may still appear as
        inline text inside a scalar, but crucially it does NOT appear
        as a line-starting key (which is what YAML parsers recognize
        as top-level keys).
        """
        import yaml as yamlmod
        hostile = _candidate(
            core_concept="concept\nmalicious_key: MALICIOUS_VALUE",
        )
        result = operationalize(
            hostile, _confirmed(), tmp_path, **_happy_kwargs(),
        )
        yaml_text = (result.lens_dir / "lens.yaml").read_text()
        # No line starts with 'malicious_key' — the guarantee that matters
        for line in yaml_text.splitlines():
            stripped = line.lstrip()
            assert not stripped.startswith("malicious_key"), (
                f"newline injection produced a top-level key: {line!r}"
            )
        # Parsed YAML must not contain 'malicious_key' as any key
        parsed = yamlmod.safe_load(yaml_text)
        assert "malicious_key" not in parsed, (
            "sanitizer failed — malicious_key ended up as a parsed key"
        )

    def test_custom_lenses_base_respected(self, tmp_path: Path):
        custom = tmp_path / "alt-lens-location"
        result = operationalize(
            _candidate(), _confirmed(), tmp_path,
            lenses_base=custom, **_happy_kwargs(),
        )
        assert result.lens_dir.parent == custom.resolve()
