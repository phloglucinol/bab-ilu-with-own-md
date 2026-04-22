#!/usr/bin/env python3
"""
Bab-ilu ingest-image hook.

Triggered on Claude Code UserPromptSubmit. Reads the hook JSON from stdin,
opens the transcript file pointed to by transcript_path, extracts image
attachments from the MOST RECENT user message, decodes them, and writes them
to raw/images/inbox/ under the vault root.

Contract:
  - Never blocks a prompt. Always exits 0.
  - Never modifies the user's prompt text (hook writes to stderr only).
  - Tolerant of transcript format variation — silently continues on mismatch.
  - Dedup by content SHA-256 short hash: re-pasting the same image is a no-op.

Filename convention:
  raw/images/inbox/YYYYMMDD-HHMMSS-<8charhash>.<ext>

Downstream consumer: /taste and /ingest skills default to the newest file in
raw/images/inbox/ when no path argument is provided.
"""

import sys
import os
import json
import base64
import hashlib
import time
import pathlib


def log(msg: str) -> None:
    print(f"[bab-ilu:ingest-image] {msg}", file=sys.stderr, flush=True)


def extract_content_list(entry: dict):
    """Tolerant extraction of a message's content list across transcript formats."""
    for key in ("content",):
        v = entry.get(key)
        if isinstance(v, list):
            return v
    # Nested under 'message' (some Claude Code versions wrap this way)
    msg = entry.get("message")
    if isinstance(msg, dict):
        v = msg.get("content")
        if isinstance(v, list):
            return v
    return None


def is_user_entry(entry: dict) -> bool:
    for key in ("role", "type"):
        v = entry.get(key)
        if isinstance(v, str) and v.lower() == "user":
            return True
    msg = entry.get("message")
    if isinstance(msg, dict):
        return is_user_entry(msg)
    return False


def main() -> int:
    try:
        hook_input = json.load(sys.stdin)
    except Exception as e:
        log(f"no hook input JSON: {e}")
        return 0

    transcript_path = hook_input.get("transcript_path") or hook_input.get("transcriptPath")
    cwd = hook_input.get("cwd") or os.getcwd()

    if not transcript_path or not os.path.exists(transcript_path):
        log(f"no transcript at {transcript_path!r}; skipping")
        return 0

    # Ensure inbox exists under vault root (cwd should be the vault)
    inbox = pathlib.Path(cwd) / "raw" / "images" / "inbox"
    try:
        inbox.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        log(f"cannot create inbox {inbox}: {e}")
        return 0

    # Read transcript (JSONL), find the MOST RECENT user message.
    try:
        with open(transcript_path) as f:
            lines = f.readlines()
    except Exception as e:
        log(f"cannot read transcript: {e}")
        return 0

    last_user = None
    for line in reversed(lines):
        try:
            entry = json.loads(line)
        except Exception:
            continue
        if is_user_entry(entry):
            last_user = entry
            break

    if last_user is None:
        log("no user messages in transcript")
        return 0

    content = extract_content_list(last_user)
    if not content:
        log("last user message has no content array")
        return 0

    # Scan for image blocks.
    ts = time.strftime("%Y%m%d-%H%M%S")
    saved = 0
    skipped_duplicate = 0

    for block in content:
        if not isinstance(block, dict):
            continue
        if block.get("type") != "image":
            continue
        source = block.get("source") or {}
        src_type = source.get("type")
        if src_type != "base64":
            log(f"skipping image source type={src_type!r} (only base64 supported)")
            continue

        media_type = source.get("media_type") or "image/png"
        ext = media_type.split("/")[-1].lower()
        if ext == "jpeg":
            ext = "jpg"
        if ext not in {"png", "jpg", "webp", "gif"}:
            log(f"skipping unknown media_type={media_type!r}")
            continue

        data_b64 = source.get("data") or ""
        try:
            data = base64.b64decode(data_b64)
        except Exception as e:
            log(f"base64 decode failed: {e}")
            continue

        if not data:
            continue

        short_hash = hashlib.sha256(data).hexdigest()[:8]

        # Dedup: if any existing inbox file has matching hash suffix, skip.
        dup = list(inbox.glob(f"*-{short_hash}.*"))
        if dup:
            skipped_duplicate += 1
            continue

        filename = f"{ts}-{short_hash}.{ext}"
        filepath = inbox / filename

        try:
            tmp = filepath.with_suffix(filepath.suffix + ".tmp")
            with open(tmp, "wb") as fout:
                fout.write(data)
            os.replace(tmp, filepath)
            log(f"saved raw/images/inbox/{filename}  ({len(data):,} bytes)")
            saved += 1
        except Exception as e:
            log(f"save failed: {e}")

    if saved == 0 and skipped_duplicate == 0:
        return 0  # silent no-op when no images attached
    if saved == 0 and skipped_duplicate > 0:
        log(f"all {skipped_duplicate} attached image(s) already in inbox (dedup)")
    else:
        log(f"✓ {saved} image(s) saved to raw/images/inbox/  (duplicates skipped: {skipped_duplicate})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
