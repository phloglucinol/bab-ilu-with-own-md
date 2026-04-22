#!/usr/bin/env bash
# Bab-ilu ingest-image hook wrapper.
# Never blocks, never fails non-zero.
# Delegates to ingest_image.py which reads the hook JSON from stdin.

set +e  # tolerate any error from the python script

HOOK_DIR="$(cd "$(dirname "$0")" && pwd)"
python3 "$HOOK_DIR/ingest_image.py"
exit 0
