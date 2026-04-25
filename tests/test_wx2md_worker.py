from __future__ import annotations

from tests._mocks import MockHTTPClient
from tools import wx2md_worker as mod


WECHAT_URL = (
    "https://mp.weixin.qq.com/s?__biz=Mzk0MDQwMjU1MA==&mid=2247484096&idx=1"
    "&sn=66e0fea115603f6ea4936cb4e96ae887"
    "&chksm=c394fbfcba72f2191f3e471be8433895e128b6f07ab3225e8a2b8a87df001d31e1214c2dc8e7"
    "&mpshare=1&scene=24&srcid=0423QQYmvrPrS3JtbC3axLor"
    "&sharer_shareinfo=ccabdc3423175f8183567b5b4e102cbd"
    "&sharer_shareinfo_first=ccabdc3423175f8183567b5b4e102cbd#rd"
)


def test_normalize_wechat_url_strips_share_noise():
    raw = WECHAT_URL + "&scene=1&srcid=123&mpshare=1"

    out = mod.normalize_wechat_url(raw)

    assert "__biz=Mzk0MDQwMjU1MA%3D%3D" in out
    assert "mid=2247484096" in out
    assert "scene=" not in out
    assert "srcid=" not in out
    assert "mpshare=" not in out


def test_materialize_wechat_via_worker_writes_raw_markdown(tmp_path):
    worker_base = "https://mp.example.com"
    worker_url = worker_base + "/md?url=" + mod._quote_url_for_worker(WECHAT_URL)
    worker_md = """---
title: Worker Captured Title
image: https://cdn.example.com/cover.jpg
---

# Worker Captured Title

Worker body paragraph.
""".encode("utf-8")

    result = mod.materialize_wechat_via_worker(
        WECHAT_URL,
        vault=tmp_path,
        worker_base_url=worker_base,
        http=MockHTTPClient({worker_url: worker_md}),
    )

    assert result.status == "captured"
    assert result.extractor == "wechat_worker"
    assert result.output_path is not None
    assert result.output_path == tmp_path / "raw" / "articles" / f"{result.slug}.md"
    text = result.output_path.read_text(encoding="utf-8")
    assert "type: raw_article" in text
    assert "extractor: wechat_worker" in text
    assert "title: Worker Captured Title" in text
    assert "# Worker Captured Title" in text
    assert "Worker body paragraph." in text
    assert text.count("---") == 2
    assert "image: https://cdn.example.com/cover.jpg" not in text


def test_materialize_wechat_via_worker_reuses_same_hash(tmp_path):
    worker_base = "https://mp.example.com"
    worker_url = worker_base + "/md?url=" + mod._quote_url_for_worker(WECHAT_URL)
    worker_md = (
        b"---\ntitle: Worker Captured Title\n---\n\n"
        b"# Worker Captured Title\n\nWorker body paragraph.\n"
    )
    http = MockHTTPClient({worker_url: worker_md})

    first = mod.materialize_wechat_via_worker(
        WECHAT_URL,
        vault=tmp_path,
        worker_base_url=worker_base,
        http=http,
    )
    second = mod.materialize_wechat_via_worker(
        WECHAT_URL,
        vault=tmp_path,
        worker_base_url=worker_base,
        http=http,
    )

    assert first.status == "captured"
    assert second.status == "unchanged"
    assert second.output_path == first.output_path


def test_materialize_wechat_via_worker_writes_versioned_file_on_content_change(tmp_path):
    worker_base = "https://mp.example.com"
    worker_url = worker_base + "/md?url=" + mod._quote_url_for_worker(WECHAT_URL)

    first = mod.materialize_wechat_via_worker(
        WECHAT_URL,
        vault=tmp_path,
        worker_base_url=worker_base,
        http=MockHTTPClient({worker_url: b"# Worker Captured Title\n\nFirst body.\n"}),
    )
    second = mod.materialize_wechat_via_worker(
        WECHAT_URL,
        vault=tmp_path,
        worker_base_url=worker_base,
        http=MockHTTPClient({worker_url: b"# Worker Captured Title\n\nChanged body.\n"}),
    )

    assert first.status == "captured"
    assert second.status == "write_conflict_resolved"
    assert second.output_path is not None
    assert second.output_path.name.endswith("-v2.md")


def test_materialize_wechat_via_worker_rejects_non_wechat_url(tmp_path):
    result = mod.materialize_wechat_via_worker(
        "https://example.com/post",
        vault=tmp_path,
        http=MockHTTPClient({}),
    )

    assert result.status == "unsupported_url"
    assert result.output_path is None


def test_materialize_wechat_via_worker_handles_fetch_failure(tmp_path):
    worker_base = "https://mp.example.com"

    result = mod.materialize_wechat_via_worker(
        WECHAT_URL,
        vault=tmp_path,
        worker_base_url=worker_base,
        http=MockHTTPClient({}),
    )

    assert result.status == "fetch_failed"
    assert result.extractor == "wechat_worker"


def test_materialize_wechat_via_worker_debugs_missing_title(tmp_path):
    worker_base = "https://mp.example.com"
    worker_url = worker_base + "/md?url=" + mod._quote_url_for_worker(WECHAT_URL)

    result = mod.materialize_wechat_via_worker(
        WECHAT_URL,
        vault=tmp_path,
        worker_base_url=worker_base,
        http=MockHTTPClient({worker_url: b"body without markdown heading"}),
    )

    assert result.status == "render_failed"
    debug_dir = tmp_path / "raw" / "articles" / "_debug"
    assert any(debug_dir.iterdir())
