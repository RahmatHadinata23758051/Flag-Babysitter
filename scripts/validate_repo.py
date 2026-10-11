#!/usr/bin/env python3
"""Dependency-free validation for the public Flag Babysitter source tree."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ("ctf-operator", "ctf-writeup-custom", "evidence-readme")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---", re.DOTALL)


def fail(message: str) -> None:
    raise SystemExit(f"validation failed: {message}")


def validate_skill_metadata() -> None:
    for skill in SKILLS:
        skill_file = ROOT / "skills" / skill / "SKILL.md"
        ui_file = ROOT / "skills" / skill / "agents" / "openai.yaml"
        if not skill_file.is_file():
            fail(f"missing {skill_file.relative_to(ROOT)}")
        if not ui_file.is_file():
            fail(f"missing {ui_file.relative_to(ROOT)}")

        contents = skill_file.read_text(encoding="utf-8")
        frontmatter = FRONTMATTER_RE.match(contents)
        if not frontmatter:
            fail(f"missing YAML frontmatter in {skill_file.relative_to(ROOT)}")
        for field in ("name:", "description:"):
            if field not in frontmatter.group(1):
                fail(f"missing {field} in {skill_file.relative_to(ROOT)}")

        ui_contents = ui_file.read_text(encoding="utf-8")
        expected_prompt = f"${skill}"
        for field in ("display_name:", "short_description:", "default_prompt:", expected_prompt):
            if field not in ui_contents:
                fail(f"missing {field} in {ui_file.relative_to(ROOT)}")


def validate_markdown_links() -> None:
    missing: list[str] = []
    for markdown_file in ROOT.rglob("*.md"):
        if ".git" in markdown_file.parts:
            continue
        text = markdown_file.read_text(encoding="utf-8")
        for link in LINK_RE.findall(text):
            if link.startswith(("#", "http://", "https://", "mailto:")):
                continue
            path_text = link.split("#", maxsplit=1)[0]
            if not (markdown_file.parent / path_text).exists():
                missing.append(f"{markdown_file.relative_to(ROOT)} -> {link}")
    if missing:
        fail("missing Markdown links:\n" + "\n".join(missing))


def run_fixture() -> None:
    subprocess.run(
        ["bash", "tests/validate-synthetic-fixture.sh"],
        cwd=ROOT,
        check=True,
    )


def test_installer() -> None:
    work_root = ROOT / ".work"
    work_root.mkdir(exist_ok=True)
    scratch = Path(tempfile.mkdtemp(prefix="validate-install-", dir=work_root))
    destination = scratch / "skills"
    try:
        command = ["bash", "scripts/install.sh", "--dest", str(destination)]
        subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True)
        for skill in SKILLS:
            if not (destination / skill / "SKILL.md").is_file():
                fail(f"installer omitted {skill}")

        sentinel = destination / "ctf-operator" / "SENTINEL"
        sentinel.write_text("preserve me", encoding="utf-8")
        blocked = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        if blocked.returncode == 0:
            fail("installer replaced an existing skill without --force")
        if not sentinel.is_file():
            fail("installer changed an existing skill without --force")

        force_command = command + ["--force"]
        subprocess.run(force_command, cwd=ROOT, check=True, capture_output=True, text=True)
        backups = list((destination / ".flag-babysitter-backups").rglob("SENTINEL"))
        if len(backups) != 1:
            fail("installer did not preserve existing skill during --force")
    finally:
        shutil.rmtree(scratch, ignore_errors=True)


def test_packager() -> None:
    work_root = ROOT / ".work"
    work_root.mkdir(exist_ok=True)
    scratch = Path(tempfile.mkdtemp(prefix="validate-package-", dir=work_root))
    output = scratch / "bundles"
    try:
        command = ["python3", "scripts/package_skills.py", "--output", str(output)]
        subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True)
        initial_bundles: dict[str, bytes] = {}
        for skill in SKILLS:
            bundle = output / f"{skill}.zip"
            if not bundle.is_file():
                fail(f"packager omitted {bundle.name}")
            initial_bundles[skill] = bundle.read_bytes()
            with zipfile.ZipFile(bundle) as archive:
                names = archive.namelist()
                if f"{skill}/SKILL.md" not in names:
                    fail(f"bundle missing manifest: {bundle.name}")
                if any(not name.startswith(f"{skill}/") for name in names):
                    fail(f"bundle contains an unexpected top-level path: {bundle.name}")

        blocked = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        if blocked.returncode == 0:
            fail("packager replaced an existing bundle without --force")

        subprocess.run(command + ["--force"], cwd=ROOT, check=True, capture_output=True, text=True)
        for skill, initial_bytes in initial_bundles.items():
            if (output / f"{skill}.zip").read_bytes() != initial_bytes:
                fail(f"packager produced a non-deterministic bundle: {skill}.zip")
        if list(output.glob(".*.zip")):
            fail("packager left a temporary ZIP behind")

        not_a_directory = scratch / "not-a-directory"
        not_a_directory.write_text("not a directory", encoding="utf-8")
        invalid_output = subprocess.run(
            ["python3", "scripts/package_skills.py", "--output", str(not_a_directory)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if invalid_output.returncode == 0:
            fail("packager accepted a non-directory output path")
    finally:
        shutil.rmtree(scratch, ignore_errors=True)


def main() -> None:
    validate_skill_metadata()
    validate_markdown_links()
    run_fixture()
    test_installer()
    test_packager()
    print("repository validation: PASS")


if __name__ == "__main__":
    main()
