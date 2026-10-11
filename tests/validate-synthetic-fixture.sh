#!/usr/bin/env bash
set -euo pipefail

fixture_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/../fixtures/synthetic-ctf/base64-proof" && pwd)"
candidate="$(python3 "$fixture_dir/worker-solution.py")"
verified="$(python3 "$fixture_dir/verify.py")"

test "$candidate" = 'candidate=ORCTF{evidence_before_claims}'
printf '%s\n' "$verified" | grep -Fx 'verified=ORCTF{evidence_before_claims}' >/dev/null
printf '%s\n' "$verified" | grep -Fx 'artifact_sha256=b13f540ef97cc4d70098bc841445b4942cf09a2586018f93af3b41d22145476a' >/dev/null

printf 'synthetic fixture: PASS\n'
