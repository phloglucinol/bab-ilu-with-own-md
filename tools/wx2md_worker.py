"""WeChat Official Account article capture via wx2md-worker.

It only supports `mp.weixin.qq.com` article URLs and writes the worker-returned
Markdown to `raw/articles/<slug>.md`.
"""

from __future__ import annotations

import hashlib
import ipaddress
import re
import socket
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Protocol
from urllib.parse import parse_qsl, quote, urlencode, urlparse, urlunparse


_SLUG_RE = re.compile(r"[^a-z0-9]+")
_WECHAT_KEEP_PARAMS = ("__biz", "mid", "idx", "sn")


class HTTPClient(Protocol):
    def get(self, url: str, *, timeout: float = 15.0) -> bytes: ...


@dataclass(frozen=True)
class MaterializationResult:
    status: str
    reason: str | None
    extractor: str | None
    slug: str
    output_path: Path | None


def _is_private_or_loopback(hostname: str) -> bool:
    if not hostname:
        return True
    lower = hostname.lower()
    if lower in ("localhost", "metadata", "metadata.google.internal", "169.254.169.254"):
        return True
    try:
        addrs = socket.getaddrinfo(hostname, None)
    except socket.gaierror:
        return True
    for _family, _type, _proto, _canon, sockaddr in addrs:
        ip_str = sockaddr[0]
        try:
            ip = ipaddress.ip_address(ip_str)
        except ValueError:
            continue
        if (
            ip.is_private
            or ip.is_loopback
            or ip.is_link_local
            or ip.is_multicast
            or ip.is_reserved
            or ip.is_unspecified
        ):
            return True
    return False


def _default_http_client() -> HTTPClient:
    import urllib.request

    class _UrllibClient:
        def get(self, url: str, *, timeout: float = 15.0) -> bytes:
            parsed = urlparse(url)
            if parsed.scheme not in ("http", "https"):
                raise ValueError(f"refusing to fetch non-http(s) URL: {url!r}")
            if _is_private_or_loopback(parsed.hostname or ""):
                raise ValueError(
                    f"refusing to fetch private/loopback/metadata URL: {url!r}"
                )
            req = urllib.request.Request(
                url, headers={"User-Agent": "bab-ilu/2.2 wx2md-worker"},
            )
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()

    return _UrllibClient()


def _slugify(text: str) -> str:
    clean = _SLUG_RE.sub("-", text.lower()).strip("-")
    return clean or "untitled"


def _slug_from_url(url: str, title: str) -> str:
    parsed = urlparse(url)
    query = dict(parse_qsl(parsed.query, keep_blank_values=True))
    pieces = [parsed.netloc.replace(".", "-")]
    for key in ("__biz", "mid", "idx"):
        value = query.get(key, "")
        if value:
            pieces.append(value)
    if title:
        pieces.append(title)
    return _slugify("-".join(pieces))


def _quote_url_for_worker(url: str) -> str:
    return quote(url, safe="")


def normalize_wechat_url(raw: str) -> str:
    parsed = urlparse(raw)
    if parsed.scheme not in ("http", "https"):
        return raw
    if parsed.netloc != "mp.weixin.qq.com":
        return raw

    params = parse_qsl(parsed.query, keep_blank_values=True)
    kept = [(key, value) for key, value in params if key in _WECHAT_KEEP_PARAMS]
    query = urlencode(kept)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", query, ""))


def _extract_content_hash(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("content_hash:"):
            return line.split(":", 1)[1].strip()
    return ""


def _extract_frontmatter_value(markdown_text: str, key: str) -> str:
    lines = markdown_text.splitlines()
    if not lines or lines[0].strip() != "---":
        return ""
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith(f"{key}:"):
            return line.split(":", 1)[1].strip()
    return ""


def _extract_markdown_title(markdown_text: str) -> str:
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def _strip_leading_frontmatter(markdown_text: str) -> str:
    lines = markdown_text.splitlines()
    if not lines or lines[0].strip() != "---":
        return markdown_text.strip()
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return "\n".join(lines[idx + 1:]).strip()
    return markdown_text.strip()


def _render_worker_markdown(
    *,
    title: str,
    normalized_url: str,
    markdown_body: str,
) -> str:
    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    body = markdown_body.strip()
    content_hash = hashlib.sha256(body.encode("utf-8")).hexdigest()
    return "\n".join(
        [
            "---",
            "type: raw_article",
            f"source_url: {normalized_url}",
            f"canonical_url: {normalized_url}",
            f"source_domain: {urlparse(normalized_url).netloc}",
            f"title: {title}",
            "author: ",
            "published_at: ",
            f"fetched_at: {fetched_at}",
            "extractor: wechat_worker",
            f"content_hash: {content_hash}",
            "status: captured",
            "---",
            "",
            body,
            "",
        ]
    )


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False, prefix=f".{path.name}."
    ) as tmp:
        tmp.write(content)
        tmp_path = Path(tmp.name)
    tmp_path.replace(path)


def _write_debug_artifact(
    vault: Path,
    *,
    slug: str,
    normalized_url: str,
    status: str,
    payload: bytes | str,
) -> None:
    debug_dir = vault / "raw" / "articles" / "_debug"
    debug_dir.mkdir(parents=True, exist_ok=True)
    path = debug_dir / f"{slug}-{status}.md"
    body = payload.decode("utf-8", errors="ignore") if isinstance(payload, bytes) else payload
    text = "\n".join(
        [
            f"url: {normalized_url}",
            "extractor: wechat_worker",
            f"status: {status}",
            "",
            body[:4000],
            "",
        ]
    )
    _atomic_write(path, text)


def _versioned_path(base: Path) -> Path:
    candidate = base
    version = 2
    while candidate.exists():
        candidate = base.with_name(f"{base.stem}-v{version}{base.suffix}")
        version += 1
    return candidate


def _write_materialized_text(
    *,
    vault: Path,
    normalized_url: str,
    slug: str,
    rendered: str,
) -> MaterializationResult:
    output_path = vault / "raw" / "articles" / f"{slug}.md"
    content_hash = _extract_content_hash(rendered)
    if output_path.exists():
        existing = output_path.read_text(encoding="utf-8")
        existing_hash = _extract_content_hash(existing)
        if existing_hash == content_hash:
            return MaterializationResult(
                status="unchanged",
                reason=None,
                extractor="wechat_worker",
                slug=slug,
                output_path=output_path,
            )
        output_path = _versioned_path(output_path)
        _atomic_write(output_path, rendered)
        return MaterializationResult(
            status="write_conflict_resolved",
            reason="existing raw article had different content_hash",
            extractor="wechat_worker",
            slug=output_path.stem,
            output_path=output_path,
        )

    _atomic_write(output_path, rendered)
    return MaterializationResult(
        status="captured",
        reason=None,
        extractor="wechat_worker",
        slug=slug,
        output_path=output_path,
    )


def materialize_wechat_via_worker(
    url: str,
    *,
    vault: Path,
    worker_base_url: str = "https://mp.084817.xyz",
    http: HTTPClient | None = None,
) -> MaterializationResult:
    normalized = normalize_wechat_url(url)
    parsed = urlparse(normalized)
    slug = _slug_from_url(normalized, "")

    if parsed.scheme not in ("http", "https") or parsed.netloc != "mp.weixin.qq.com":
        return MaterializationResult(
            status="unsupported_url",
            reason="wx2md-worker only supports mp.weixin.qq.com article URLs",
            extractor="wechat_worker",
            slug=slug,
            output_path=None,
        )

    worker_url = worker_base_url.rstrip("/") + "/md?url=" + _quote_url_for_worker(url)
    try:
        raw_bytes = (http or _default_http_client()).get(worker_url)
    except Exception as exc:
        return MaterializationResult(
            status="fetch_failed",
            reason=str(exc),
            extractor="wechat_worker",
            slug=slug,
            output_path=None,
        )

    markdown_text = raw_bytes.decode("utf-8", errors="ignore").strip()
    if not markdown_text:
        _write_debug_artifact(
            vault,
            slug=slug,
            normalized_url=normalized,
            status="render_failed",
            payload=raw_bytes,
        )
        return MaterializationResult(
            status="render_failed",
            reason="worker returned empty markdown",
            extractor="wechat_worker",
            slug=slug,
            output_path=None,
        )

    title = _extract_frontmatter_value(markdown_text, "title") or _extract_markdown_title(markdown_text)
    if not title:
        _write_debug_artifact(
            vault,
            slug=slug,
            normalized_url=normalized,
            status="render_failed",
            payload=raw_bytes,
        )
        return MaterializationResult(
            status="render_failed",
            reason="worker markdown missing title",
            extractor="wechat_worker",
            slug=slug,
            output_path=None,
        )

    markdown_body = _strip_leading_frontmatter(markdown_text)
    slug = _slug_from_url(normalized, title)
    rendered = _render_worker_markdown(
        title=title,
        normalized_url=normalized,
        markdown_body=markdown_body,
    )
    return _write_materialized_text(
        vault=vault,
        normalized_url=normalized,
        slug=slug,
        rendered=rendered,
    )
