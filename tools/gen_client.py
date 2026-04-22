#!/usr/bin/env python3
"""Unified generation API client for Bab-ilu v2.0.

Abstracts over:
  - OpenAI-compatible endpoints (Gemini image gen behind custom proxy)
  - MINIMAX native endpoints (fallback / video)

Used by /prompt --test to actually call generation models and score outputs.

Design goals:
  - Multi-backend with graceful fallback chain
  - Reads config from .env (never hard-coded keys)
  - Retry with exponential backoff on transient failures
  - Structured result objects — no opaque responses

Usage:
    python3 tools/gen_client.py --smoke                    # test connectivity
    python3 tools/gen_client.py --generate --prompt "..."  # one-shot image gen
    python3 tools/gen_client.py --score --image PATH --reference SLUG  # scoring

    # Programmatic:
    from gen_client import GenClient
    c = GenClient.from_env()
    result = c.generate_image("a blue cat", model="gemini-3-pro-image-preview")
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# Pattern for ![image](data:image/XXX;base64,<data>) — used by proxy response format
DATA_URL_RE = re.compile(r"!\[[^\]]*\]\(data:image/([a-zA-Z]+);base64,([A-Za-z0-9+/=_-]+)\)")

try:
    import httpx
except ImportError:
    print("error: httpx required · pip install 'httpx[http2]>=0.27'", file=sys.stderr)
    sys.exit(2)

REPO = Path(__file__).resolve().parents[1]

# Auto-load .env from project root
ENV_PATH = REPO / ".env"
if ENV_PATH.is_file():
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        os.environ.setdefault(k.strip(), v.strip())


@dataclass
class GenResult:
    success: bool
    model: str
    prompt: str
    image_b64: str | None = None
    image_url: str | None = None
    text: str | None = None
    latency_ms: int = 0
    error: str | None = None
    raw: dict | None = None


@dataclass
class GenClient:
    base_url: str
    api_key: str
    model_chain: list[str] = field(default_factory=list)
    timeout: float = 180.0
    max_retries: int = 3
    http2: bool = True

    @classmethod
    def from_env(cls) -> "GenClient":
        base = os.getenv("IMAGE_GEN_BASE_URL", "").rstrip("/")
        key = os.getenv("IMAGE_GEN_API_KEY", "")
        chain = [m.strip() for m in os.getenv("IMAGE_GEN_MODELS", "").split(",") if m.strip()]
        if not base or not key:
            raise RuntimeError(
                "IMAGE_GEN_BASE_URL / IMAGE_GEN_API_KEY missing from .env — "
                f"looked at {ENV_PATH}"
            )
        return cls(base_url=base, api_key=key, model_chain=chain or ["gemini-3.1-flash-image-preview"])

    def _client(self) -> httpx.Client:
        return httpx.Client(
            base_url=self.base_url,
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
            timeout=self.timeout,
            http2=self.http2,
        )

    def _openai_compatible_image(self, model: str, prompt: str) -> GenResult:
        """Call /v1/images/generations (OpenAI-compatible image endpoint)."""
        start = time.time()
        # `IMAGE_GEN_BASE_URL` is expected to be an OpenAI-compatible gateway.
        # Some gateways route image generation through `/v1/chat/completions`
        # with the image returned as a data URL in the response content;
        # others expose `/v1/images/generations` directly. We try chat/completions
        # first (more broadly supported across Gemini/DALL-E-style gateways),
        # then fall back to images/generations.
        url_candidates = ["/v1/chat/completions", "/v1/images/generations", "/images/generations"]
        last_err = None
        with self._client() as cli:
            for url in url_candidates:
                try:
                    if "images/generations" in url:
                        payload = {
                            "model": model,
                            "prompt": prompt,
                            "n": 1,
                            "size": "1024x1024",
                            "response_format": "b64_json",
                        }
                    else:
                        # chat-completions-style image gen (Gemini 3 preview convention)
                        payload = {
                            "model": model,
                            "messages": [
                                {"role": "user", "content": prompt}
                            ],
                            "modalities": ["image", "text"],
                        }
                    r = cli.post(url, json=payload)
                    if r.status_code == 404:
                        last_err = f"{url} returned 404"
                        continue
                    if r.status_code >= 400:
                        last_err = f"{url} returned {r.status_code}: {r.text[:200]}"
                        continue
                    try:
                        data = r.json()
                    except json.JSONDecodeError:
                        last_err = f"{url}: response not JSON (status {r.status_code}, len={len(r.text)})"
                        continue
                    # Parse response — try common shapes
                    b64 = None
                    url_out = None
                    text_out = None
                    if "data" in data and isinstance(data["data"], list) and data["data"]:
                        item = data["data"][0]
                        b64 = item.get("b64_json")
                        url_out = item.get("url")
                    elif "choices" in data and data["choices"]:
                        choice = data["choices"][0]
                        msg = choice.get("message", {})
                        content = msg.get("content", "")
                        if isinstance(content, list):
                            for part in content:
                                if isinstance(part, dict):
                                    if part.get("type") == "image_url":
                                        url_out = part.get("image_url", {}).get("url") if isinstance(part.get("image_url"), dict) else part.get("image_url")
                                    elif part.get("type") == "text":
                                        text_out = (text_out or "") + part.get("text", "")
                                    elif part.get("type") == "image" and "b64_json" in part:
                                        b64 = part["b64_json"]
                        elif isinstance(content, str):
                            # Proxy format: ![image](data:image/jpeg;base64,XXX) possibly followed by caption
                            m = DATA_URL_RE.search(content)
                            if m:
                                b64 = m.group(2)
                                # Remaining text after image tag is potential caption
                                caption = DATA_URL_RE.sub("", content).strip()
                                text_out = caption if caption else None
                            else:
                                text_out = content

                    return GenResult(
                        success=(b64 is not None or url_out is not None),
                        model=model,
                        prompt=prompt,
                        image_b64=b64,
                        image_url=url_out,
                        text=text_out,
                        latency_ms=int((time.time() - start) * 1000),
                        error=None if (b64 or url_out) else "response had no image payload",
                        raw=data if not (b64 or url_out) else None,
                    )
                except httpx.HTTPError as e:
                    last_err = f"{url}: {type(e).__name__} {e}"
                    continue
            return GenResult(
                success=False, model=model, prompt=prompt,
                latency_ms=int((time.time() - start) * 1000),
                error=last_err or "all endpoints failed",
            )

    def generate_image(self, prompt: str, model: str | None = None) -> GenResult:
        """Try each model in chain, first success wins. If `model` given, force that."""
        if model:
            chain = [model]
        else:
            chain = self.model_chain
        last_result: GenResult | None = None
        for m in chain:
            for attempt in range(self.max_retries):
                result = self._openai_compatible_image(m, prompt)
                last_result = result
                if result.success:
                    return result
                # retry on transient
                if result.error and ("timeout" in (result.error or "").lower() or "5" in (result.error or "")[:3]):
                    time.sleep(2 ** attempt)
                    continue
                break
        return last_result or GenResult(
            success=False, model="none", prompt=prompt, error="empty chain",
        )

    def smoke(self) -> dict:
        """Quick connectivity test — returns diagnostic dict, doesn't raise."""
        out: dict[str, Any] = {
            "base_url": self.base_url,
            "api_key_present": bool(self.api_key),
            "api_key_prefix": self.api_key[:12] + "..." if self.api_key else None,
            "model_chain_len": len(self.model_chain),
            "first_model": self.model_chain[0] if self.model_chain else None,
            "endpoints_tried": [],
            "endpoint_reachable": False,
            "generation_success": False,
        }
        # Try a tiny generation with first model
        test_prompt = "test generation — minimalist geometric poster, single yellow circle on black, bauhaus style"
        result = self.generate_image(test_prompt, model=self.model_chain[0] if self.model_chain else None)
        out["generation_success"] = result.success
        out["generation_latency_ms"] = result.latency_ms
        out["generation_model"] = result.model
        out["generation_error"] = result.error
        if result.success:
            out["image_received"] = bool(result.image_b64 or result.image_url)
            out["image_mode"] = "base64" if result.image_b64 else "url"
            if result.image_url:
                out["image_url_preview"] = result.image_url[:80] + "..."
        return out


@dataclass
class MiniMaxClient:
    """Fallback / video gen via MINIMAX."""
    api_key: str
    base_url: str = "https://api.minimax.chat/v1"

    @classmethod
    def from_env(cls) -> "MiniMaxClient":
        key = os.getenv("MINIMAX_API_KEY", "")
        url = os.getenv("MINIMAX_BASE_URL", "https://api.minimax.chat/v1")
        if not key:
            raise RuntimeError("MINIMAX_API_KEY missing")
        return cls(api_key=key, base_url=url)

    def smoke(self) -> dict:
        out = {"base_url": self.base_url, "api_key_present": bool(self.api_key)}
        try:
            with httpx.Client(timeout=10) as cli:
                r = cli.get(f"{self.base_url}/user/query", headers={"Authorization": f"Bearer {self.api_key}"})
                out["status_code"] = r.status_code
                out["reachable"] = r.status_code < 500
        except httpx.HTTPError as e:
            out["reachable"] = False
            out["error"] = f"{type(e).__name__}: {e}"
        return out


def cmd_smoke(_args):
    try:
        c = GenClient.from_env()
    except RuntimeError as e:
        print(f"✗ gen_client config: {e}", file=sys.stderr)
        return 2
    print("=== Image Gen smoke ===")
    res = c.smoke()
    for k, v in res.items():
        marker = "✓" if (k in ("endpoint_reachable", "generation_success") and v) or (k not in ("endpoint_reachable", "generation_success")) else "✗"
        print(f"  {marker} {k}: {v}")
    print()
    try:
        m = MiniMaxClient.from_env()
        print("=== MINIMAX smoke ===")
        mres = m.smoke()
        for k, v in mres.items():
            print(f"  {k}: {v}")
    except RuntimeError as e:
        print(f"✗ minimax config: {e}")
    return 0 if res.get("generation_success") else 1


def cmd_generate(args):
    c = GenClient.from_env()
    result = c.generate_image(args.prompt, model=args.model)
    if result.success:
        out_dir = Path(args.out_dir)
        out_dir.mkdir(exist_ok=True, parents=True)
        if result.image_b64:
            out_path = out_dir / f"gen_{int(time.time())}.png"
            out_path.write_bytes(base64.b64decode(result.image_b64))
            print(f"✓ {out_path} · model={result.model} · {result.latency_ms}ms")
        elif result.image_url:
            print(f"✓ url-only response: {result.image_url}")
            print(f"  model={result.model} · {result.latency_ms}ms")
        return 0
    print(f"✗ {result.error}", file=sys.stderr)
    return 1


def main():
    ap = argparse.ArgumentParser(description="Bab-ilu v2.0 gen client")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("smoke", help="connectivity diagnostics")
    g = sub.add_parser("generate", help="one-shot image generation")
    g.add_argument("--prompt", required=True)
    g.add_argument("--model", default=None)
    g.add_argument("--out-dir", default="/tmp/babilu-gen")
    # Convenience: --smoke and --generate as top-level flags too
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--generate", action="store_true")
    ap.add_argument("--prompt", default=None)
    ap.add_argument("--model", default=None)
    ap.add_argument("--out-dir", default="/tmp/babilu-gen")
    args = ap.parse_args()

    if args.smoke or args.cmd == "smoke":
        sys.exit(cmd_smoke(args))
    if args.generate or args.cmd == "generate":
        if not args.prompt:
            print("--prompt required for generate", file=sys.stderr)
            sys.exit(2)
        sys.exit(cmd_generate(args))
    ap.print_help()


if __name__ == "__main__":
    main()
