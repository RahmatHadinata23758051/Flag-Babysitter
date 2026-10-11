#!/usr/bin/env python3
"""Create one portable ZIP bundle per Flag Babysitter skill."""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ("ctf-operator", "ctf-writeup-custom", "evidence-readme")
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create one portable ZIP bundle per selected Flag Babysitter skill."
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Directory that will receive <skill-name>.zip files.",
    )
    parser.add_argument(
        "--skill",
        choices=SKILLS,
        action="append",
        dest="selected_skills",
        help="Package only this skill; repeat the option to select multiple skills.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing ZIP with the same name in the output directory.",
    )
    return parser.parse_args()


def write_bundle(skill: str, output: Path, force: bool) -> Path:
    source = ROOT / "skills" / skill
    manifest = source / "SKILL.md"
    if not manifest.is_file():
        raise RuntimeError(f"missing skill manifest: {manifest.relative_to(ROOT)}")

    destination = output / f"{skill}.zip"
    if destination.exists() and not force:
        raise RuntimeError(
            f"refusing to replace {destination}; rerun with --force to overwrite that bundle"
        )

    files = sorted(path for path in source.rglob("*") if path.is_file())
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            relative = path.relative_to(source)
            entry = zipfile.ZipInfo(f"{skill}/{relative.as_posix()}", FIXED_TIMESTAMP)
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes())
    return destination


def main() -> int:
    args = parse_args()
    selected = tuple(dict.fromkeys(args.selected_skills or SKILLS))
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        for skill in selected:
            destination = write_bundle(skill, args.output, args.force)
            print(f"packaged: {destination}")
    except RuntimeError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
