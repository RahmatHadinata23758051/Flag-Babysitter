#!/usr/bin/env python3
"""Independent verifier for the synthetic fixture; it never imports the worker solver."""

from __future__ import annotations

import base64
import hashlib
import re
from pathlib import Path


EXPECTED_ARTIFACT_SHA256 = "b13f540ef97cc4d70098bc841445b4942cf09a2586018f93af3b41d22145476a"
EXPECTED_FLAG = "ORCTF{evidence_before_claims}"
FLAG_PATTERN = re.compile(r"^ORCTF\{[a-z_]+\}$")


def main() -> None:
    artifact = Path(__file__).with_name("artifact.txt")
    raw = artifact.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_ARTIFACT_SHA256:
        raise SystemExit(f"artifact digest mismatch: {digest}")

    decoded = base64.b64decode(raw.strip(), validate=True).decode("ascii")
    if not FLAG_PATTERN.fullmatch(decoded):
        raise SystemExit("decoded content does not match the synthetic flag format")
    if decoded != EXPECTED_FLAG:
        raise SystemExit("decoded content does not match the expected synthetic result")

    print(f"verified={decoded}")
    print(f"artifact_sha256={digest}")


if __name__ == "__main__":
    main()
