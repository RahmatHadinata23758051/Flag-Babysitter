#!/usr/bin/env python3
"""Worker-side solver for the synthetic fixture."""

from __future__ import annotations

import base64
from pathlib import Path


def main() -> None:
    artifact = Path(__file__).with_name("artifact.txt")
    payload = artifact.read_text(encoding="ascii").strip()
    candidate = base64.b64decode(payload, validate=True).decode("ascii")
    print(f"candidate={candidate}")


if __name__ == "__main__":
    main()
