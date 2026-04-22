"""Shared HTTP + LLM replay mocks for extractor tests.

Used by `tests/test_incident_extractor.py` and will be reused by E3
(source_ingester) and E4 (note_extractor) in later Sprint 3 passes.

Design: both mocks are **replay-only** — they never make real calls.
Tests compose them from fixture files committed under
`tests/fixtures/incident_extractor/<slug>/raw.html` and
`tests/fixtures/llm_responses/E1/<slug>.json`.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Mapping, Optional


class MockHTTPClient:
    """Replay HTTP GETs from a URL→bytes mapping.

    Unknown URLs raise KeyError so tests fail loudly rather than
    accidentally hitting the network via a misconfigured fixture.
    """

    def __init__(self, mapping: Mapping[str, bytes]) -> None:
        self._mapping = dict(mapping)
        self.calls: list[str] = []  # audit trail for tests

    def get(self, url: str, *, timeout: float = 15.0) -> bytes:
        self.calls.append(url)
        if url not in self._mapping:
            raise KeyError(f"unmocked URL: {url}")
        return self._mapping[url]

    @classmethod
    def from_fixtures(cls, fixture_dir: Path, mapping: Mapping[str, Path]) -> "MockHTTPClient":
        """Build a client from URL→fixture-filename mapping under
        `fixture_dir`. Convenience for the common e2e shape."""
        resolved = {
            url: (fixture_dir / rel).read_bytes()
            for url, rel in mapping.items()
        }
        return cls(resolved)


class MockLLMClient:
    """Replay LLM responses from a fixture mapping.

    Two usage shapes:
      - `MockLLMClient(response=dict)` always returns the same dict.
      - `MockLLMClient(responses={"slug": {...}, ...})` + `next_slug`
        attribute picks per-call response. The extractor makes exactly
        one call per ingest, so the simple form is usually enough.
    """

    def __init__(
        self,
        response: Optional[dict] = None,
        *,
        responses: Optional[Mapping[str, dict]] = None,
    ) -> None:
        if response is None and responses is None:
            raise ValueError("must pass either response=... or responses=...")
        self._single = response
        self._multi = dict(responses) if responses else None
        self.next_slug: Optional[str] = None
        self.calls: list[dict] = []

    def complete_json(self, *, system: str, prompt: str, schema: dict) -> dict:
        self.calls.append({"system": system, "prompt": prompt, "schema": schema})
        if self._single is not None:
            return dict(self._single)  # copy to defend against mutation
        assert self._multi is not None  # for type-checkers
        if self.next_slug is None or self.next_slug not in self._multi:
            raise KeyError(
                f"no response configured for slug={self.next_slug!r}; "
                f"set .next_slug before each call"
            )
        return dict(self._multi[self.next_slug])

    @classmethod
    def from_fixture(cls, fixture_path: Path) -> "MockLLMClient":
        data = json.loads(fixture_path.read_text(encoding="utf-8"))
        return cls(response=data)
