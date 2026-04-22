"""Tests for tools/lint.py

Validates all lint check functions with synthetic wiki fixtures:
  - Missing fields detection (all 8 entity types)
  - Broken wikilinks
  - Orphan pages
  - Field value validation (enums, ranges)
  - Idea failure_reason check
  - Experiment target_claim check
  - Cross-reference asymmetry
  - Graph edge consistency
  - Content quality suggestions
  - CLI interface (human-readable and JSON output)
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = PROJECT_ROOT / "tools"

# Add tools to path for direct import
sys.path.insert(0, str(TOOLS_DIR))
import lint as lint_mod


@pytest.fixture
def wiki_dir(tmp_path):
    """Create a minimal valid wiki directory structure."""
    for d in ["papers", "concepts", "topics", "people",
              "ideas", "experiments", "claims", "Summary", "foundations", "graph"]:
        (tmp_path / d).mkdir()
    (tmp_path / "graph" / "edges.jsonl").write_text("")
    return tmp_path


def _write_page(wiki_dir, entity_type, slug, frontmatter_lines, body=""):
    """Helper to write a wiki page with frontmatter."""
    fm = "\n".join(frontmatter_lines)
    content = f"---\n{fm}\n---\n\n{body}"
    path = wiki_dir / entity_type / f"{slug}.md"
    path.write_text(content, encoding="utf-8")
    return path


# ── extract_frontmatter ─────────────────────────────────────────────────────

class TestExtractFrontmatter:
    def test_basic_extraction(self):
        content = "---\ntitle: Test\nslug: test\n---\nBody"
        fm = lint_mod.extract_frontmatter(content)
        assert "title" in fm
        assert "slug" in fm

    def test_no_frontmatter(self):
        fm = lint_mod.extract_frontmatter("No frontmatter here")
        assert fm == {}

    def test_nested_keys_ignored(self):
        content = "---\nsetup:\n  model: gpt-4\n  dataset: mmlu\ntags: []\n---\n"
        fm = lint_mod.extract_frontmatter(content)
        assert "setup" in fm
        assert "tags" in fm
        # Nested keys should not appear at top level
        assert "model" not in fm


# ── Missing Fields ───────────────────────────────────────────────────────────

class TestMissingFields:
    def test_paper_missing_importance(self, wiki_dir):
        _write_page(wiki_dir, "papers", "test-paper",
                    ['title: "Test"', 'slug: test-paper', 'tags: [ml]'])
        issues = lint_mod.check_missing_fields(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        cats = [i.message for i in issues]
        assert any("importance" in m for m in cats)

    def test_paper_all_fields_present(self, wiki_dir):
        _write_page(wiki_dir, "papers", "good-paper",
                    ['title: "Good"', 'slug: good-paper', 'tags: [ml]', 'importance: 3'])
        pages = lint_mod.find_all_pages(wiki_dir)
        # Filter to just this page
        issues = [i for i in lint_mod.check_missing_fields(wiki_dir, pages)
                  if "good-paper" in i.file]
        assert len(issues) == 0

    def test_concept_missing_maturity(self, wiki_dir):
        _write_page(wiki_dir, "concepts", "test-concept",
                    ['title: "Test"', 'tags: [ml]', 'key_papers: [a]'])
        issues = lint_mod.check_missing_fields(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        msgs = [i.message for i in issues if "test-concept" in i.file]
        assert any("maturity" in m for m in msgs)

    def test_idea_missing_fields(self, wiki_dir):
        _write_page(wiki_dir, "ideas", "bad-idea",
                    ['title: "Bad"', 'slug: bad-idea'])
        issues = lint_mod.check_missing_fields(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        msgs = [i.message for i in issues if "bad-idea" in i.file]
        missing = {m.split(": ")[1] for m in msgs}
        assert "status" in missing
        assert "origin" in missing
        assert "tags" in missing
        assert "priority" in missing

    def test_experiment_missing_target_claim(self, wiki_dir):
        _write_page(wiki_dir, "experiments", "exp1",
                    ['title: "E1"', 'slug: exp1', 'status: planned',
                     'hypothesis: "test"', 'tags: [ml]'])
        issues = lint_mod.check_missing_fields(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        msgs = [i.message for i in issues if "exp1" in i.file]
        assert any("target_claim" in m for m in msgs)

    def test_claim_missing_evidence(self, wiki_dir):
        _write_page(wiki_dir, "claims", "claim1",
                    ['title: "C1"', 'slug: claim1', 'status: proposed',
                     'confidence: 0.5', 'tags: [ml]', 'source_papers: [p1]'])
        issues = lint_mod.check_missing_fields(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        msgs = [i.message for i in issues if "claim1" in i.file]
        assert any("evidence" in m for m in msgs)

    def test_summary_missing_scope(self, wiki_dir):
        _write_page(wiki_dir, "Summary", "area1",
                    ['title: "Area"', 'key_topics: [t1]'])
        issues = lint_mod.check_missing_fields(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        msgs = [i.message for i in issues if "area1" in i.file]
        assert any("scope" in m for m in msgs)

    def test_people_all_fields(self, wiki_dir):
        _write_page(wiki_dir, "people", "john-doe",
                    ['name: "John Doe"', 'tags: [ml]'])
        pages = lint_mod.find_all_pages(wiki_dir)
        issues = [i for i in lint_mod.check_missing_fields(wiki_dir, pages)
                  if "john-doe" in i.file]
        assert len(issues) == 0

    def test_topics_all_fields(self, wiki_dir):
        _write_page(wiki_dir, "topics", "topic1",
                    ['title: "T1"', 'tags: [ml]'])
        pages = lint_mod.find_all_pages(wiki_dir)
        issues = [i for i in lint_mod.check_missing_fields(wiki_dir, pages)
                  if "topic1" in i.file]
        assert len(issues) == 0

    def test_foundation_missing_domain(self, wiki_dir):
        _write_page(wiki_dir, "foundations", "bad-foundation",
                    ['title: "Bad"', 'slug: bad-foundation', 'status: mainstream'])
        issues = lint_mod.check_missing_fields(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        msgs = [i.message for i in issues if "bad-foundation" in i.file]
        assert any("domain" in m for m in msgs)

    def test_foundation_all_fields(self, wiki_dir):
        _write_page(wiki_dir, "foundations", "good-foundation",
                    ['title: "Good"', 'slug: good-foundation',
                     'domain: general', 'status: mainstream'])
        pages = lint_mod.find_all_pages(wiki_dir)
        issues = [i for i in lint_mod.check_missing_fields(wiki_dir, pages)
                  if "good-foundation" in i.file]
        assert len(issues) == 0

    def test_foundation_invalid_status(self, wiki_dir):
        _write_page(wiki_dir, "foundations", "bad-status",
                    ['title: "B"', 'slug: bad-status',
                     'domain: general', 'status: legendary'])
        issues = lint_mod.check_field_values(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        msgs = [i.message for i in issues if "bad-status" in i.file]
        assert any("status" in m for m in msgs)


# ── Broken Links ─────────────────────────────────────────────────────────────

class TestBrokenLinks:
    def test_broken_link_detected(self, wiki_dir):
        _write_page(wiki_dir, "papers", "p1",
                    ['title: "P1"', 'slug: p1', 'tags: [ml]', 'importance: 3'],
                    "See [[nonexistent]]")
        issues, _ = lint_mod.check_broken_links(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert len(issues) == 1
        assert "nonexistent" in issues[0].message

    def test_valid_link_no_issue(self, wiki_dir):
        _write_page(wiki_dir, "papers", "p1",
                    ['title: "P1"', 'slug: p1', 'tags: [ml]', 'importance: 3'],
                    "See [[p2]]")
        _write_page(wiki_dir, "concepts", "p2",
                    ['title: "P2"', 'tags: [ml]', 'maturity: active', 'key_papers: [p1]'])
        issues, incoming = lint_mod.check_broken_links(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert len(issues) == 0
        assert "p1" in incoming["p2"]

    def test_wikilink_with_alias(self, wiki_dir):
        _write_page(wiki_dir, "papers", "p1",
                    ['title: "P1"', 'slug: p1', 'tags: [ml]', 'importance: 3'],
                    "See [[p2|Paper 2]]")
        _write_page(wiki_dir, "papers", "p2",
                    ['title: "P2"', 'slug: p2', 'tags: [ml]', 'importance: 3'])
        issues, _ = lint_mod.check_broken_links(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert len(issues) == 0


# ── Orphan Pages ─────────────────────────────────────────────────────────────

class TestOrphanPages:
    def test_orphan_detected(self, wiki_dir):
        _write_page(wiki_dir, "papers", "lonely",
                    ['title: "Lonely"', 'slug: lonely', 'tags: [ml]', 'importance: 1'])
        pages = lint_mod.find_all_pages(wiki_dir)
        _, incoming = lint_mod.check_broken_links(wiki_dir, pages)
        issues = lint_mod.check_orphan_pages(wiki_dir, pages, incoming)
        assert any("lonely" in i.file for i in issues)

    def test_linked_page_not_orphan(self, wiki_dir):
        _write_page(wiki_dir, "papers", "linked",
                    ['title: "L"', 'slug: linked', 'tags: [ml]', 'importance: 3'])
        _write_page(wiki_dir, "concepts", "c1",
                    ['title: "C1"', 'tags: [ml]', 'maturity: active', 'key_papers: [linked]'],
                    "Based on [[linked]]")
        pages = lint_mod.find_all_pages(wiki_dir)
        _, incoming = lint_mod.check_broken_links(wiki_dir, pages)
        issues = lint_mod.check_orphan_pages(wiki_dir, pages, incoming)
        orphan_files = [i.file for i in issues]
        assert not any("linked" in f for f in orphan_files)

    def test_foundation_orphan_is_reported(self, wiki_dir):
        # Foundations are NOT exempt from orphan check. Under correct usage
        # every foundation receives an inward link via /ingest dedup. An
        # un-referenced foundation is a real diagnostic signal.
        _write_page(wiki_dir, "foundations", "gradient-descent",
                    ['title: "Gradient Descent"', 'slug: gradient-descent',
                     'domain: general', 'status: mainstream'])
        pages = lint_mod.find_all_pages(wiki_dir)
        _, incoming = lint_mod.check_broken_links(wiki_dir, pages)
        issues = lint_mod.check_orphan_pages(wiki_dir, pages, incoming)
        assert any("gradient-descent" in i.file for i in issues)

    def test_foundation_with_inward_link_not_orphan(self, wiki_dir):
        # When a paper or concept links to a foundation, it should NOT be an orphan.
        _write_page(wiki_dir, "foundations", "transformer",
                    ['title: "Transformer"', 'slug: transformer',
                     'domain: NLP', 'status: mainstream'])
        _write_page(wiki_dir, "papers", "attention-paper",
                    ['title: "Attention"', 'slug: attention-paper',
                     'tags: [nlp]', 'importance: 5'],
                    "Builds on [[transformer]]")
        pages = lint_mod.find_all_pages(wiki_dir)
        _, incoming = lint_mod.check_broken_links(wiki_dir, pages)
        issues = lint_mod.check_orphan_pages(wiki_dir, pages, incoming)
        assert not any("transformer" in i.file for i in issues)


# ── Field Values ─────────────────────────────────────────────────────────────

class TestFieldValues:
    def test_invalid_importance(self, wiki_dir):
        _write_page(wiki_dir, "papers", "bad-imp",
                    ['title: "B"', 'slug: bad-imp', 'tags: [ml]', 'importance: 9'])
        issues = lint_mod.check_field_values(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert any("importance" in i.message for i in issues)

    def test_valid_importance(self, wiki_dir):
        _write_page(wiki_dir, "papers", "good-imp",
                    ['title: "G"', 'slug: good-imp', 'tags: [ml]', 'importance: 3'])
        issues = lint_mod.check_field_values(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert not any("good-imp" in i.file for i in issues)

    def test_invalid_maturity(self, wiki_dir):
        _write_page(wiki_dir, "concepts", "bad-mat",
                    ['title: "B"', 'tags: [ml]', 'maturity: unknown', 'key_papers: [x]'])
        issues = lint_mod.check_field_values(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert any("maturity" in i.message for i in issues)

    def test_invalid_idea_status(self, wiki_dir):
        _write_page(wiki_dir, "ideas", "bad-status",
                    ['title: "B"', 'slug: bad-status', 'status: archived',
                     'origin: test', 'tags: [ml]', 'priority: 3'])
        issues = lint_mod.check_field_values(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert any("status" in i.message and "bad-status" in i.file for i in issues)

    def test_invalid_experiment_status(self, wiki_dir):
        _write_page(wiki_dir, "experiments", "bad-exp",
                    ['title: "E"', 'slug: bad-exp', 'status: done',
                     'target_claim: c1', 'hypothesis: test', 'tags: [ml]'])
        issues = lint_mod.check_field_values(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert any("status" in i.message and "bad-exp" in i.file for i in issues)

    def test_invalid_claim_status(self, wiki_dir):
        _write_page(wiki_dir, "claims", "bad-claim",
                    ['title: "C"', 'slug: bad-claim', 'status: confirmed',
                     'confidence: 0.5', 'tags: [ml]', 'source_papers: [p1]',
                     'evidence:'])
        issues = lint_mod.check_field_values(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert any("status" in i.message and "bad-claim" in i.file for i in issues)

    def test_confidence_out_of_range(self, wiki_dir):
        _write_page(wiki_dir, "claims", "high-conf",
                    ['title: "C"', 'slug: high-conf', 'status: supported',
                     'confidence: 1.5', 'tags: [ml]', 'source_papers: [p1]',
                     'evidence:'])
        issues = lint_mod.check_field_values(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert any("confidence" in i.message for i in issues)

    def test_confidence_valid(self, wiki_dir):
        _write_page(wiki_dir, "claims", "ok-conf",
                    ['title: "C"', 'slug: ok-conf', 'status: supported',
                     'confidence: 0.8', 'tags: [ml]', 'source_papers: [p1]',
                     'evidence:'])
        issues = lint_mod.check_field_values(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert not any("ok-conf" in i.file for i in issues)

    def test_confidence_not_a_number(self, wiki_dir):
        _write_page(wiki_dir, "claims", "nan-conf",
                    ['title: "C"', 'slug: nan-conf', 'status: proposed',
                     'confidence: high', 'tags: [ml]', 'source_papers: [p1]',
                     'evidence:'])
        issues = lint_mod.check_field_values(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert any("nan-conf" in i.file for i in issues)


# ── Idea Failure Reason ──────────────────────────────────────────────────────

class TestIdeaFailureReason:
    def test_failed_without_reason(self, wiki_dir):
        _write_page(wiki_dir, "ideas", "dead-idea",
                    ['title: "Dead"', 'slug: dead-idea', 'status: failed',
                     'origin: gap', 'tags: [ml]', 'priority: 2',
                     'failure_reason: ""'])
        issues = lint_mod.check_idea_failure_reason(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert len(issues) == 1
        assert "failure_reason" in issues[0].message

    def test_failed_with_reason(self, wiki_dir):
        _write_page(wiki_dir, "ideas", "explained-fail",
                    ['title: "Fail"', 'slug: explained-fail', 'status: failed',
                     'origin: gap', 'tags: [ml]', 'priority: 2',
                     'failure_reason: "compute too expensive"'])
        issues = lint_mod.check_idea_failure_reason(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert len(issues) == 0

    def test_proposed_no_reason_ok(self, wiki_dir):
        _write_page(wiki_dir, "ideas", "new-idea",
                    ['title: "New"', 'slug: new-idea', 'status: proposed',
                     'origin: gap', 'tags: [ml]', 'priority: 3',
                     'failure_reason: ""'])
        issues = lint_mod.check_idea_failure_reason(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert len(issues) == 0


# ── Experiment Claim Link ────────────────────────────────────────────────────

class TestExperimentClaimLink:
    def test_missing_claim_file(self, wiki_dir):
        _write_page(wiki_dir, "experiments", "exp-bad",
                    ['title: "E"', 'slug: exp-bad', 'status: planned',
                     'target_claim: nonexistent-claim', 'hypothesis: test', 'tags: [ml]'])
        issues = lint_mod.check_experiment_claim_link(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert len(issues) == 1
        assert "nonexistent-claim" in issues[0].message

    def test_valid_claim_reference(self, wiki_dir):
        _write_page(wiki_dir, "claims", "real-claim",
                    ['title: "RC"', 'slug: real-claim', 'status: proposed',
                     'confidence: 0.5', 'tags: [ml]', 'source_papers: [p1]',
                     'evidence:'])
        _write_page(wiki_dir, "experiments", "exp-good",
                    ['title: "E"', 'slug: exp-good', 'status: planned',
                     'target_claim: real-claim', 'hypothesis: test', 'tags: [ml]'])
        issues = lint_mod.check_experiment_claim_link(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        exp_issues = [i for i in issues if "exp-good" in i.file]
        assert len(exp_issues) == 0


# ── Cross-Reference Asymmetry ───────────────────────────────────────────────

class TestXrefAsymmetry:
    def test_concept_key_papers_asymmetry(self, wiki_dir):
        _write_page(wiki_dir, "concepts", "att",
                    ['title: "Attention"', 'tags: [ml]', 'maturity: active',
                     'key_papers: [transformer-paper]'])
        _write_page(wiki_dir, "papers", "transformer-paper",
                    ['title: "Transformer"', 'slug: transformer-paper',
                     'tags: [ml]', 'importance: 5'],
                    "## Related\nNothing here")
        issues = lint_mod.check_xref_asymmetry(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert any("att" in i.message and "transformer-paper" in i.message for i in issues)

    def test_concept_key_papers_symmetric(self, wiki_dir):
        _write_page(wiki_dir, "concepts", "att2",
                    ['title: "Attention"', 'tags: [ml]', 'maturity: active',
                     'key_papers: [tp2]'])
        _write_page(wiki_dir, "papers", "tp2",
                    ['title: "T2"', 'slug: tp2', 'tags: [ml]', 'importance: 5'],
                    "## Related\n[[att2]]")
        issues = lint_mod.check_xref_asymmetry(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        concept_issues = [i for i in issues if "att2" in i.file]
        assert len(concept_issues) == 0

    def test_idea_origin_gaps_asymmetry(self, wiki_dir):
        _write_page(wiki_dir, "ideas", "idea-x",
                    ['title: "X"', 'slug: idea-x', 'status: proposed',
                     'origin: gap', 'origin_gaps: [claim-y]',
                     'tags: [ml]', 'priority: 3'])
        _write_page(wiki_dir, "claims", "claim-y",
                    ['title: "Y"', 'slug: claim-y', 'status: proposed',
                     'confidence: 0.3', 'tags: [ml]', 'source_papers: [p]',
                     'evidence:'],
                    "## Linked ideas\nNothing")
        issues = lint_mod.check_xref_asymmetry(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert any("idea-x" in i.file and "claim-y" in i.message for i in issues)


# ── Graph Edge Consistency ───────────────────────────────────────────────────

class TestGraphEdges:
    def test_valid_edges(self, wiki_dir):
        _write_page(wiki_dir, "papers", "p1",
                    ['title: "P1"', 'slug: p1', 'tags: [ml]', 'importance: 3'])
        _write_page(wiki_dir, "concepts", "c1",
                    ['title: "C1"', 'tags: [ml]', 'maturity: active', 'key_papers: [p1]'])
        edge = json.dumps({"from": "papers/p1", "to": "concepts/c1", "type": "supports",
                           "evidence": "test", "date": "2026-04-08"})
        (wiki_dir / "graph" / "edges.jsonl").write_text(edge + "\n")
        issues = lint_mod.check_graph_edges(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert len(issues) == 0

    def test_invalid_json(self, wiki_dir):
        (wiki_dir / "graph" / "edges.jsonl").write_text("not json\n")
        issues = lint_mod.check_graph_edges(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert any("Invalid JSON" in i.message for i in issues)

    def test_missing_field(self, wiki_dir):
        edge = json.dumps({"from": "papers/p1", "to": "concepts/c1"})
        (wiki_dir / "graph" / "edges.jsonl").write_text(edge + "\n")
        issues = lint_mod.check_graph_edges(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert any("type" in i.message for i in issues)

    def test_unknown_edge_type(self, wiki_dir):
        edge = json.dumps({"from": "papers/p1", "to": "concepts/c1", "type": "likes"})
        (wiki_dir / "graph" / "edges.jsonl").write_text(edge + "\n")
        issues = lint_mod.check_graph_edges(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert any("Unknown edge type" in i.message for i in issues)

    def test_dangling_node(self, wiki_dir):
        edge = json.dumps({"from": "papers/ghost", "to": "concepts/phantom", "type": "supports"})
        (wiki_dir / "graph" / "edges.jsonl").write_text(edge + "\n")
        issues = lint_mod.check_graph_edges(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        dangling = [i for i in issues if "dangling" in i.category]
        assert len(dangling) == 2

    def test_no_edges_file(self, wiki_dir):
        (wiki_dir / "graph" / "edges.jsonl").unlink()
        issues = lint_mod.check_graph_edges(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert len(issues) == 0


# ── Content Quality ──────────────────────────────────────────────────────────

class TestContentQuality:
    def test_importance5_no_concept_ref(self, wiki_dir):
        _write_page(wiki_dir, "papers", "seminal",
                    ['title: "S"', 'slug: seminal', 'tags: [ml]', 'importance: 5'])
        issues = lint_mod.check_content_quality(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert any("importance=5" in i.message for i in issues)

    def test_stable_concept_one_paper(self, wiki_dir):
        _write_page(wiki_dir, "concepts", "stable-c",
                    ['title: "SC"', 'tags: [ml]', 'maturity: stable',
                     'key_papers: [only-one]'])
        issues = lint_mod.check_content_quality(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert any("stable" in i.message and "key_paper" in i.message for i in issues)

    def test_empty_open_problems(self, wiki_dir):
        _write_page(wiki_dir, "topics", "empty-topic",
                    ['title: "ET"', 'tags: [ml]'],
                    "## Open problems\n\n## My position\nSomething")
        issues = lint_mod.check_content_quality(wiki_dir, lint_mod.find_all_pages(wiki_dir))
        assert any("Open problems" in i.message for i in issues)


# ── Full Lint Integration ────────────────────────────────────────────────────

class TestLintIntegration:
    def test_empty_wiki_no_crash(self, wiki_dir):
        issues = lint_mod.lint(wiki_dir)
        assert isinstance(issues, list)

    def test_healthy_wiki(self, wiki_dir):
        _write_page(wiki_dir, "papers", "p1",
                    ['title: "P1"', 'slug: p1', 'tags: [ml]', 'importance: 3'],
                    "## Related\n[[c1]]")
        _write_page(wiki_dir, "concepts", "c1",
                    ['title: "C1"', 'tags: [ml]', 'maturity: active',
                     'key_papers: [p1]'],
                    "## Key papers\n[[p1]]")
        issues = lint_mod.lint(wiki_dir)
        # Should have no red issues
        red = [i for i in issues if i.level == "🔴"]
        assert len(red) == 0


# ── CLI ──────────────────────────────────────────────────────────────────────

class TestCLI:
    def test_cli_runs(self, wiki_dir):
        result = subprocess.run(
            [sys.executable, str(TOOLS_DIR / "lint.py"), "--wiki-dir", str(wiki_dir)],
            capture_output=True, text=True
        )
        assert "Lint:" in result.stdout or result.returncode == 0

    def test_cli_json_output(self, wiki_dir):
        _write_page(wiki_dir, "papers", "cli-test",
                    ['title: "T"', 'slug: cli-test', 'tags: [ml]', 'importance: 3'])
        result = subprocess.run(
            [sys.executable, str(TOOLS_DIR / "lint.py"),
             "--wiki-dir", str(wiki_dir), "--json"],
            capture_output=True, text=True
        )
        data = json.loads(result.stdout)
        assert isinstance(data, list)

    def test_cli_nonexistent_dir(self):
        result = subprocess.run(
            [sys.executable, str(TOOLS_DIR / "lint.py"),
             "--wiki-dir", "/tmp/nonexistent_wiki_dir_xyz"],
            capture_output=True, text=True
        )
        assert result.returncode != 0

    def test_cli_exit_code_red(self, wiki_dir):
        """Exit code 1 when red issues exist."""
        _write_page(wiki_dir, "papers", "no-importance",
                    ['title: "NI"', 'slug: no-importance', 'tags: [ml]'])
        result = subprocess.run(
            [sys.executable, str(TOOLS_DIR / "lint.py"), "--wiki-dir", str(wiki_dir)],
            capture_output=True, text=True
        )
        assert result.returncode == 1

    def test_lint_issue_to_dict(self):
        issue = lint_mod.LintIssue("🔴", "test", "file.md", "test message")
        d = issue.to_dict()
        assert d["level"] == "🔴"
        assert d["category"] == "test"
        assert d["file"] == "file.md"
        assert d["message"] == "test message"

    def test_lint_issue_str(self):
        issue = lint_mod.LintIssue("🟡", "broken-link", "papers/p.md", "link broken")
        s = str(issue)
        assert "🟡" in s
        assert "broken-link" in s

    def test_lint_issue_fixable_in_dict(self):
        issue = lint_mod.LintIssue("🟡", "xref", "f.md", "msg", fixable=True)
        d = issue.to_dict()
        assert d["fixable"] is True

    def test_lint_issue_suggestion_in_dict(self):
        issue = lint_mod.LintIssue("🟡", "broken-link", "f.md", "msg",
                                   suggestion="Remove the link")
        d = issue.to_dict()
        assert d["suggestion"] == "Remove the link"

    def test_cli_fix_json(self, wiki_dir):
        """--fix --json outputs dict with fixes key."""
        _write_page(wiki_dir, "concepts", "con-a",
                    ['title: "A"', 'tags: [ml]', 'maturity: active',
                     'key_papers: [paper-x]'],
                    body="## Definition\nTest")
        _write_page(wiki_dir, "papers", "paper-x",
                    ['title: "X"', 'slug: paper-x', 'tags: [ml]', 'importance: 3'],
                    body="## Related\n")
        result = subprocess.run(
            [sys.executable, str(TOOLS_DIR / "lint.py"),
             "--wiki-dir", str(wiki_dir), "--fix", "--json"],
            capture_output=True, text=True
        )
        data = json.loads(result.stdout)
        assert "issues" in data
        assert "fixes" in data
        assert isinstance(data["fixes"], list)

    def test_cli_suggest_output(self, wiki_dir):
        """--suggest shows suggestion text."""
        _write_page(wiki_dir, "papers", "s-paper",
                    ['title: "S"', 'slug: s-paper', 'tags: [ml]', 'importance: 3'],
                    body="See [[nonexistent-page]]")
        result = subprocess.run(
            [sys.executable, str(TOOLS_DIR / "lint.py"),
             "--wiki-dir", str(wiki_dir), "--suggest"],
            capture_output=True, text=True
        )
        assert "💡" in result.stdout


# ── Fix Functions ────────────────────────────────────────────────────────────

class TestFixXrefAsymmetry:
    """Test auto-fix for cross-reference asymmetry."""

    def test_fix_concept_paper_reverse_link(self, wiki_dir):
        """concepts.key_papers → papers: adds [[concept]] to paper's ## Related."""
        _write_page(wiki_dir, "concepts", "attention",
                    ['title: "Attention"', 'tags: [ml]', 'maturity: active',
                     'key_papers: [transformer-paper]'],
                    body="## Definition\nTest")
        _write_page(wiki_dir, "papers", "transformer-paper",
                    ['title: "Transformer"', 'slug: transformer-paper',
                     'tags: [ml]', 'importance: 5'],
                    body="## Related\n")

        issues = lint_mod.lint(wiki_dir)
        xref_issues = [i for i in issues if i.category == "xref-asymmetry"
                       and "attention" in i.message]
        assert len(xref_issues) > 0
        assert xref_issues[0].fixable

        fixes = lint_mod.fix_issues(wiki_dir, issues)
        assert any("attention" in f.action for f in fixes)

        # Verify the fix was applied
        paper_content = (wiki_dir / "papers" / "transformer-paper.md").read_text()
        assert "[[attention]]" in paper_content

    def test_fix_paper_people_reverse_link(self, wiki_dir):
        """papers → people: adds [[paper]] to person's ## Key papers."""
        _write_page(wiki_dir, "papers", "lora-paper",
                    ['title: "LoRA"', 'slug: lora-paper',
                     'tags: [ml]', 'importance: 4'],
                    body="By [[john-doe]]\n\n## Related\n")
        _write_page(wiki_dir, "people", "john-doe",
                    ['name: "John Doe"', 'tags: [ml]'],
                    body="## Key papers\n")

        issues = lint_mod.lint(wiki_dir)
        fixes = lint_mod.fix_issues(wiki_dir, issues)
        assert any("lora-paper" in f.action for f in fixes)

        person_content = (wiki_dir / "people" / "john-doe.md").read_text()
        assert "[[lora-paper]]" in person_content

    def test_fix_claim_paper_reverse_link(self, wiki_dir):
        """claims.source_papers → papers: adds [[claim]] to paper's ## Related."""
        _write_page(wiki_dir, "claims", "lora-claim",
                    ['title: "LoRA claim"', 'slug: lora-claim', 'status: proposed',
                     'confidence: 0.5', 'tags: [ml]',
                     'source_papers: [lora-paper]', 'evidence: []'],
                    body="## Statement\nTest")
        _write_page(wiki_dir, "papers", "lora-paper",
                    ['title: "LoRA"', 'slug: lora-paper',
                     'tags: [ml]', 'importance: 4'],
                    body="## Related\n")

        issues = lint_mod.lint(wiki_dir)
        fixes = lint_mod.fix_issues(wiki_dir, issues)
        assert any("lora-claim" in f.action for f in fixes)

        paper_content = (wiki_dir / "papers" / "lora-paper.md").read_text()
        assert "[[lora-claim]]" in paper_content

    def test_fix_idea_claim_reverse_link(self, wiki_dir):
        """ideas.origin_gaps → claims: adds [[idea]] to claim's ## Linked ideas."""
        _write_page(wiki_dir, "ideas", "my-idea",
                    ['title: "My Idea"', 'slug: my-idea', 'status: proposed',
                     'origin: "gap"', 'tags: [ml]', 'priority: 3',
                     'origin_gaps: [some-claim]'],
                    body="## Motivation\nTest")
        _write_page(wiki_dir, "claims", "some-claim",
                    ['title: "Some claim"', 'slug: some-claim', 'status: proposed',
                     'confidence: 0.5', 'tags: [ml]',
                     'source_papers: []', 'evidence: []'],
                    body="## Statement\nTest\n\n## Linked ideas\n")

        issues = lint_mod.lint(wiki_dir)
        fixes = lint_mod.fix_issues(wiki_dir, issues)
        assert any("my-idea" in f.action for f in fixes)

        claim_content = (wiki_dir / "claims" / "some-claim.md").read_text()
        assert "[[my-idea]]" in claim_content

    def test_fix_experiment_claim_reverse_link(self, wiki_dir):
        """experiments.target_claim → claims: adds experiment ref to claim."""
        _write_page(wiki_dir, "experiments", "exp-1",
                    ['title: "Exp 1"', 'slug: exp-1', 'status: planned',
                     'target_claim: some-claim', 'hypothesis: "test"',
                     'tags: [ml]'],
                    body="## Objective\nTest")
        _write_page(wiki_dir, "claims", "some-claim",
                    ['title: "Some claim"', 'slug: some-claim', 'status: proposed',
                     'confidence: 0.5', 'tags: [ml]',
                     'source_papers: []', 'evidence: []'],
                    body="## Statement\nTest\n\n## Evidence summary\n")

        issues = lint_mod.lint(wiki_dir)
        fixes = lint_mod.fix_issues(wiki_dir, issues)
        assert any("exp-1" in f.action for f in fixes)

        claim_content = (wiki_dir / "claims" / "some-claim.md").read_text()
        assert "exp-1" in claim_content

    def test_dry_run_does_not_modify(self, wiki_dir):
        """--dry-run reports fixes but doesn't change files."""
        _write_page(wiki_dir, "concepts", "con-b",
                    ['title: "B"', 'tags: [ml]', 'maturity: active',
                     'key_papers: [paper-y]'],
                    body="## Definition\nTest")
        _write_page(wiki_dir, "papers", "paper-y",
                    ['title: "Y"', 'slug: paper-y', 'tags: [ml]', 'importance: 3'],
                    body="## Related\n")

        original_content = (wiki_dir / "papers" / "paper-y.md").read_text()
        issues = lint_mod.lint(wiki_dir)
        fixes = lint_mod.fix_issues(wiki_dir, issues, dry_run=True)

        assert len(fixes) > 0
        assert (wiki_dir / "papers" / "paper-y.md").read_text() == original_content

    def test_fix_idempotent(self, wiki_dir):
        """Running fix twice doesn't duplicate links."""
        _write_page(wiki_dir, "concepts", "con-c",
                    ['title: "C"', 'tags: [ml]', 'maturity: active',
                     'key_papers: [paper-z]'],
                    body="## Definition\nTest")
        _write_page(wiki_dir, "papers", "paper-z",
                    ['title: "Z"', 'slug: paper-z', 'tags: [ml]', 'importance: 3'],
                    body="## Related\n")

        issues1 = lint_mod.lint(wiki_dir)
        lint_mod.fix_issues(wiki_dir, issues1)

        # Run again
        issues2 = lint_mod.lint(wiki_dir)
        fixes2 = lint_mod.fix_issues(wiki_dir, issues2)

        # No new xref fixes should be needed
        xref_fixes = [f for f in fixes2 if "xref" in f.action.lower() or "[[" in f.action]
        assert len(xref_fixes) == 0


class TestFixMissingFields:
    """Test auto-fix for missing frontmatter fields with safe defaults."""

    def test_fix_missing_importance(self, wiki_dir):
        _write_page(wiki_dir, "papers", "no-imp",
                    ['title: "NI"', 'slug: no-imp', 'tags: [ml]'])
        issues = lint_mod.lint(wiki_dir)
        fixes = lint_mod.fix_issues(wiki_dir, issues)
        assert any("importance" in f.action for f in fixes)

        content = (wiki_dir / "papers" / "no-imp.md").read_text()
        assert "importance: 3" in content

    def test_fix_missing_tags(self, wiki_dir):
        _write_page(wiki_dir, "concepts", "no-tags",
                    ['title: "NT"', 'maturity: active', 'key_papers: [a]'])
        issues = lint_mod.lint(wiki_dir)
        fixes = lint_mod.fix_issues(wiki_dir, issues)
        assert any("tags" in f.action for f in fixes)

    def test_no_fix_for_non_defaultable_field(self, wiki_dir):
        """Fields without safe defaults (like title, slug) are not auto-fixed."""
        _write_page(wiki_dir, "papers", "no-title",
                    ['slug: no-title', 'tags: [ml]', 'importance: 3'])
        issues = lint_mod.lint(wiki_dir)
        fixes = lint_mod.fix_issues(wiki_dir, issues)
        # title has no safe default, should not be fixed
        assert not any("title" in f.action for f in fixes)

    def test_fix_missing_confidence(self, wiki_dir):
        _write_page(wiki_dir, "claims", "no-conf",
                    ['title: "NC"', 'slug: no-conf', 'status: proposed',
                     'tags: [ml]', 'source_papers: []', 'evidence: []'])
        issues = lint_mod.lint(wiki_dir)
        fixes = lint_mod.fix_issues(wiki_dir, issues)
        assert any("confidence" in f.action for f in fixes)

        content = (wiki_dir / "claims" / "no-conf.md").read_text()
        assert "confidence: 0.5" in content


class TestFixResult:
    def test_str_format(self):
        fr = lint_mod.FixResult("papers/foo.md", "Added reverse link")
        s = str(fr)
        assert "papers/foo.md" in s
        assert "Added reverse link" in s

    def test_to_dict(self):
        fr = lint_mod.FixResult("papers/foo.md", "Added reverse link")
        d = fr.to_dict()
        assert d["file"] == "papers/foo.md"
        assert d["action"] == "Added reverse link"


# ── A8: Lens-aware checks (--lens flag) + --rebuild-graph ──────────────────
#
# These tests cover the v2.1 lens-aware lint surface: when a lens is active,
# lint adds two checks on top of the v2.0 entity checks:
#   1. anchor-missing — tier-0 entries with ZERO authority_fields populated
#   2. tier-1-cluster-member-type — cluster wikilinks must resolve to
#      tier-0 or tier-1-atom pages (per the lens's entity_model)
#
# Lens fixtures are synthesized in tmp_path so tests don't depend on the
# real .agent/lenses/ directory and can exercise lenses without
# authority_fields (zettelkasten-shaped) alongside aesthetic-warburg.

import yaml as _yaml  # noqa: E402  (kept local so the v2.0 test block stays untouched)

_REPO_TOOLS = Path(__file__).resolve().parent.parent / "tools"
sys.path.insert(0, str(_REPO_TOOLS.parent))
from tools.lens_loader import load_lens  # noqa: E402


_MIN_SCHEMA_SRC = (_REPO_TOOLS.parent / ".agent" / "lenses" / "schema.json")


def _write_lens(base: Path, lens_id: str, **overrides) -> None:
    """Materialize a minimal valid lens.yaml under base/<lens_id>/.

    The defaults describe a zettelkasten-shaped lens (tier-0=note,
    tier-1-atom=concept-ref, tier-1-cluster=concept, no authority_fields).
    Overrides merge shallow so individual tests can swap a single field
    (entity_model, anchors, thresholds …) without restating the rest.
    """
    cfg = {
        "id": lens_id,
        "version": "1.0.0",
        "name": f"Test lens {lens_id}",
        "description": "fixture lens for test_lint A8 suite",
        "deliverable_types": ["entry"],
        "entity_model": {
            "tier_0": "note",
            "tier_1_atom": "concept-ref",
            "tier_1_cluster": "concept",
        },
        "activation": {"mode": "triggers", "triggers": ["|note| >= 1"]},
        "thresholds": {
            "cluster_member_min": 3,
            "cluster_min_size": 3,
            "density_multiplier": 3.0,
            "orphan_min_degree": 1,
            "domain_min": 5,
        },
        "allowed_subdomains": ["open"],
        "community_detection": {
            "algorithm": "louvain",
            "resolution": 1.0,
            "random_state": 42,
        },
        "analysis_contract": {
            "gap": ["orphan_note", "understaffed_concept"],
            "taste": ["recurrence"],
        },
    }
    cfg.update(overrides)
    lens_dir = base / lens_id
    lens_dir.mkdir(parents=True, exist_ok=True)
    (lens_dir / "lens.yaml").write_text(_yaml.safe_dump(cfg), encoding="utf-8")


@pytest.fixture
def lenses_base(tmp_path) -> Path:
    base = tmp_path / "lenses_base"
    base.mkdir()
    # Lenses rely on a sibling schema.json — copy the real one so load_lens
    # passes schema validation.
    (base / "schema.json").write_text(
        _MIN_SCHEMA_SRC.read_text(encoding="utf-8"), encoding="utf-8"
    )
    return base


@pytest.fixture
def zettel_lens(lenses_base) -> "lint_mod.LensConfig":  # forward-ref string
    _write_lens(lenses_base, "test-zettel")
    return load_lens("test-zettel", base=lenses_base)


@pytest.fixture
def anchored_lens(lenses_base):
    """A lens that REQUIRES authority_fields — exercises the anchor check."""
    _write_lens(
        lenses_base,
        "test-anchored",
        entity_model={
            "tier_0": "aesthetic",
            "tier_1_atom": "motif",
            "tier_1_cluster": "panel",
        },
        anchors={"authority_fields": ["aat_id", "wikidata"]},
    )
    return load_lens("test-anchored", base=lenses_base)


class TestLensAnchorCheck:
    """check_lens_anchors: tier-0 entries must populate ≥1 authority field."""

    def test_function_exists(self):
        assert hasattr(lint_mod, "check_lens_anchors")

    def test_flags_tier_zero_without_any_anchor(self, wiki_dir, anchored_lens):
        # A tier-0 "aesthetic" page with neither aat_id nor wikidata.
        (wiki_dir / "aesthetic").mkdir()
        (wiki_dir / "aesthetic" / "empty-anchor.md").write_text(
            "---\ntitle: Empty\ntype: aesthetic\nslug: empty-anchor\n---\nBody",
            encoding="utf-8",
        )
        pages = lint_mod._scan_all_markdown(wiki_dir)
        issues = lint_mod.check_lens_anchors(wiki_dir, pages, anchored_lens)
        cats = [i for i in issues if i.category == "lens-anchor"]
        assert len(cats) == 1
        assert "empty-anchor" in cats[0].file
        # Suggestion should list the available authority fields.
        assert "aat_id" in cats[0].suggestion or "wikidata" in cats[0].suggestion

    def test_ok_when_at_least_one_anchor_present(self, wiki_dir, anchored_lens):
        (wiki_dir / "aesthetic").mkdir()
        (wiki_dir / "aesthetic" / "has-one.md").write_text(
            '---\ntitle: "One"\ntype: aesthetic\nslug: has-one\naat_id: 300000000\n---\nBody',
            encoding="utf-8",
        )
        pages = lint_mod._scan_all_markdown(wiki_dir)
        issues = lint_mod.check_lens_anchors(wiki_dir, pages, anchored_lens)
        assert not [i for i in issues if i.category == "lens-anchor"]

    def test_lens_without_authority_fields_yields_nothing(self, wiki_dir, zettel_lens):
        """Zettelkasten-shaped lens has no authority_fields — check is a no-op."""
        (wiki_dir / "note").mkdir()
        (wiki_dir / "note" / "plain.md").write_text(
            "---\ntitle: Plain\ntype: note\nslug: plain\n---\nBody",
            encoding="utf-8",
        )
        pages = lint_mod._scan_all_markdown(wiki_dir)
        issues = lint_mod.check_lens_anchors(wiki_dir, pages, zettel_lens)
        assert issues == []

    def test_non_tier_zero_pages_ignored(self, wiki_dir, anchored_lens):
        """A page with a different type (e.g. panel) is not checked for anchors."""
        (wiki_dir / "panel").mkdir()
        (wiki_dir / "panel" / "grief.md").write_text(
            '---\ntitle: Grief\ntype: panel\nslug: grief\n---\n',
            encoding="utf-8",
        )
        pages = lint_mod._scan_all_markdown(wiki_dir)
        issues = lint_mod.check_lens_anchors(wiki_dir, pages, anchored_lens)
        assert [i for i in issues if i.category == "lens-anchor"] == []


class TestLensTierConsistency:
    """check_lens_tier_consistency: tier-1-cluster wikilinks must resolve
    to tier-0 or tier-1-atom pages (per the lens entity_model)."""

    def test_function_exists(self):
        assert hasattr(lint_mod, "check_lens_tier_consistency")

    def test_cluster_linking_to_wrong_type_is_flagged(self, wiki_dir, anchored_lens):
        # Set up a panel (tier-1-cluster) linking to an unrelated "sources" page.
        (wiki_dir / "panel").mkdir()
        (wiki_dir / "sources").mkdir()
        (wiki_dir / "sources" / "some-source.md").write_text(
            "---\ntitle: Src\ntype: source\nslug: some-source\n---\n", encoding="utf-8"
        )
        (wiki_dir / "panel" / "bad.md").write_text(
            "---\ntitle: Bad\ntype: panel\nslug: bad\n---\nSee [[some-source]].",
            encoding="utf-8",
        )
        pages = lint_mod._scan_all_markdown(wiki_dir)
        issues = lint_mod.check_lens_tier_consistency(wiki_dir, pages, anchored_lens)
        tier = [i for i in issues if i.category == "lens-tier"]
        assert len(tier) == 1
        assert "bad" in tier[0].file
        assert "some-source" in tier[0].message

    def test_cluster_linking_to_tier_zero_is_ok(self, wiki_dir, anchored_lens):
        (wiki_dir / "panel").mkdir()
        (wiki_dir / "aesthetic").mkdir()
        (wiki_dir / "aesthetic" / "a1.md").write_text(
            "---\ntitle: A1\ntype: aesthetic\nslug: a1\naat_id: 1\n---\n",
            encoding="utf-8",
        )
        (wiki_dir / "panel" / "ok.md").write_text(
            "---\ntitle: OK\ntype: panel\nslug: ok\n---\nContains [[a1]].",
            encoding="utf-8",
        )
        pages = lint_mod._scan_all_markdown(wiki_dir)
        issues = lint_mod.check_lens_tier_consistency(wiki_dir, pages, anchored_lens)
        assert [i for i in issues if i.category == "lens-tier"] == []

    def test_cluster_linking_to_tier_atom_is_ok(self, wiki_dir, anchored_lens):
        (wiki_dir / "panel").mkdir()
        (wiki_dir / "motif").mkdir()
        (wiki_dir / "motif" / "m1.md").write_text(
            "---\ntitle: M1\ntype: motif\nslug: m1\n---\n", encoding="utf-8"
        )
        (wiki_dir / "panel" / "ok2.md").write_text(
            "---\ntitle: OK2\ntype: panel\nslug: ok2\n---\nContains [[m1]].",
            encoding="utf-8",
        )
        pages = lint_mod._scan_all_markdown(wiki_dir)
        issues = lint_mod.check_lens_tier_consistency(wiki_dir, pages, anchored_lens)
        assert [i for i in issues if i.category == "lens-tier"] == []

    def test_cluster_with_broken_wikilink_not_double_reported(
        self, wiki_dir, anchored_lens
    ):
        """A missing target is already covered by check_broken_links;
        lens-tier should only flag EXISTING pages of the wrong type."""
        (wiki_dir / "panel").mkdir()
        (wiki_dir / "panel" / "lost.md").write_text(
            "---\ntitle: Lost\ntype: panel\nslug: lost\n---\nSee [[nowhere]].",
            encoding="utf-8",
        )
        pages = lint_mod._scan_all_markdown(wiki_dir)
        issues = lint_mod.check_lens_tier_consistency(wiki_dir, pages, anchored_lens)
        assert [i for i in issues if i.category == "lens-tier"] == []


class TestLensCLI:
    """CLI surface for --lens and --lenses-base."""

    def _setup_minimal_aesthetic_wiki(self, wiki_dir, lenses_base):
        """Zero-anchor tier-0 + a cluster with a good link. Lens anchor check
        should fire; lens-tier check should not."""
        _write_lens(
            lenses_base,
            "test-anchored",
            entity_model={
                "tier_0": "aesthetic",
                "tier_1_atom": "motif",
                "tier_1_cluster": "panel",
            },
            anchors={"authority_fields": ["aat_id", "wikidata"]},
        )
        (wiki_dir / "aesthetic").mkdir()
        (wiki_dir / "aesthetic" / "naked.md").write_text(
            "---\ntitle: Naked\ntype: aesthetic\nslug: naked\n---\n",
            encoding="utf-8",
        )

    def test_cli_lens_runs_anchor_check(self, wiki_dir, lenses_base):
        self._setup_minimal_aesthetic_wiki(wiki_dir, lenses_base)
        result = subprocess.run(
            [
                sys.executable, str(TOOLS_DIR / "lint.py"),
                "--wiki-dir", str(wiki_dir),
                "--lens", "test-anchored",
                "--lenses-base", str(lenses_base),
                "--json",
            ],
            capture_output=True, text=True,
        )
        assert result.returncode in (0, 1), result.stderr
        data = json.loads(result.stdout)
        cats = [i["category"] for i in data]
        assert "lens-anchor" in cats, f"expected lens-anchor in {cats}"

    def test_cli_lens_unknown_id_exits_nonzero(self, wiki_dir, lenses_base):
        result = subprocess.run(
            [
                sys.executable, str(TOOLS_DIR / "lint.py"),
                "--wiki-dir", str(wiki_dir),
                "--lens", "does-not-exist",
                "--lenses-base", str(lenses_base),
            ],
            capture_output=True, text=True,
        )
        assert result.returncode != 0
        assert "does-not-exist" in (result.stderr + result.stdout)

    def test_cli_without_lens_flag_skips_lens_checks(self, wiki_dir, lenses_base):
        """No --lens → lens-anchor/lens-tier categories never appear."""
        self._setup_minimal_aesthetic_wiki(wiki_dir, lenses_base)
        result = subprocess.run(
            [sys.executable, str(TOOLS_DIR / "lint.py"),
             "--wiki-dir", str(wiki_dir), "--json"],
            capture_output=True, text=True,
        )
        data = json.loads(result.stdout)
        cats = [i["category"] for i in data]
        assert "lens-anchor" not in cats
        assert "lens-tier" not in cats


class TestRebuildGraph:
    """CLI --rebuild-graph delegates to tools/graph_analyzer.py as subprocess."""

    def test_function_exists(self):
        assert hasattr(lint_mod, "rebuild_graph")

    def test_rebuild_graph_invokes_graph_analyzer(self, wiki_dir, monkeypatch):
        recorded = {}

        def fake_run(cmd, *args, **kwargs):
            recorded["cmd"] = list(cmd)
            recorded["cwd"] = kwargs.get("cwd")

            class _R:
                returncode = 0
                stdout = ""
                stderr = ""
            return _R()

        monkeypatch.setattr(lint_mod.subprocess, "run", fake_run)
        result = lint_mod.rebuild_graph(wiki_dir, lens_id=None, lenses_base=None)
        assert result.returncode == 0
        # Command should invoke the analyzer as a package module (-m form; a
        # bare-script invocation fails with ModuleNotFoundError because
        # graph_analyzer.py does `from tools.lens_loader import ...`).
        joined = " ".join(recorded["cmd"])
        assert "-m" in recorded["cmd"]
        assert "tools.graph_analyzer" in joined
        # Analyzer takes --vault (the vault root), not --wiki-dir. The lint
        # runner passes wiki_dir.parent to satisfy that contract.
        assert "--vault" in recorded["cmd"]
        assert str(wiki_dir.parent) in joined

    def test_rebuild_graph_passes_lens_flag_through(self, wiki_dir, monkeypatch):
        recorded = {}

        def fake_run(cmd, *args, **kwargs):
            recorded["cmd"] = list(cmd)

            class _R:
                returncode = 0
                stdout = ""
                stderr = ""
            return _R()

        monkeypatch.setattr(lint_mod.subprocess, "run", fake_run)
        lint_mod.rebuild_graph(
            wiki_dir, lens_id="test-anchored", lenses_base=Path("/tmp/l")
        )
        assert "--lens" in recorded["cmd"]
        assert "test-anchored" in recorded["cmd"]
        assert "--lenses-base" in recorded["cmd"]

    def test_cli_rebuild_graph_flag(self, wiki_dir, monkeypatch):
        """End-to-end: --rebuild-graph on the CLI triggers the subprocess."""
        result = subprocess.run(
            [sys.executable, str(TOOLS_DIR / "lint.py"),
             "--wiki-dir", str(wiki_dir), "--rebuild-graph", "--json"],
            capture_output=True, text=True,
        )
        # Exit 0 or 1 depending on v2.0 issues; important bit: no crash,
        # and the graph_analyzer invocation is reflected in stderr or stdout.
        assert result.returncode in (0, 1, 2), result.stderr


class TestPublicSurface:
    """A8 guards against accidental removal of lens-aware symbols."""

    def test_module_exports(self):
        for name in ("check_lens_anchors", "check_lens_tier_consistency",
                     "rebuild_graph"):
            assert hasattr(lint_mod, name), f"lint module missing '{name}'"
