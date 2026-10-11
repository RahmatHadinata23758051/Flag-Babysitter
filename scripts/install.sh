#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: bash scripts/install.sh --dest <codex-skills-directory> [--force]

Copies Flag Babysitter skills into a chosen Codex skills directory.

Options:
  --dest <path>  Required destination directory for installed skills.
  --force        Preserve existing same-name skills in a timestamped backup,
                 then install this repository's versions.
  -h, --help     Show this help text.

The script never downloads dependencies. Without --force it refuses to replace
an existing skill directory.
USAGE
}

destination=""
force=0

while (($#)); do
  case "$1" in
    --dest)
      (($# >= 2)) || { echo "error: --dest needs a path" >&2; exit 2; }
      destination="$2"
      shift 2
      ;;
    --force)
      force=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "error: unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

[[ -n "$destination" ]] || { echo "error: --dest is required" >&2; usage >&2; exit 2; }

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_root="$repository_root/skills"
skill_names=(ctf-operator ctf-writeup-custom evidence-readme)

[[ -d "$source_root" ]] || { echo "error: source skills directory is missing" >&2; exit 1; }

# Complete every read-only check before creating or moving anything in the
# destination. A failed preflight therefore leaves an existing installation
# untouched.
for skill_name in "${skill_names[@]}"; do
  [[ -f "$source_root/$skill_name/SKILL.md" ]] || {
    echo "error: missing source skill: $skill_name" >&2
    exit 1
  }
done

if [[ -d "$destination" ]] && (( ! force )); then
  for skill_name in "${skill_names[@]}"; do
    if [[ -e "$destination/$skill_name" ]]; then
      echo "error: destination already contains $destination/$skill_name; rerun with --force to preserve and replace it" >&2
      exit 1
    fi
  done
fi

mkdir -p "$destination"
staging_root="$(mktemp -d "$destination/.flag-babysitter-staging.XXXXXXXX")"
cleanup() {
  rm -rf "$staging_root"
}
trap cleanup EXIT

# Copy every source skill into staging before replacing a destination skill.
for skill_name in "${skill_names[@]}"; do
  cp -R "$source_root/$skill_name" "$staging_root/$skill_name"
done

backup_root=""
for skill_name in "${skill_names[@]}"; do
  target_skill="$destination/$skill_name"

  if [[ -e "$target_skill" ]]; then
    if [[ -z "$backup_root" ]]; then
      backup_root="$destination/.flag-babysitter-backups/$(date -u +%Y%m%dT%H%M%SZ)-$$"
      mkdir -p "$backup_root"
    fi
    mv "$target_skill" "$backup_root/$skill_name"
  fi

  mv "$staging_root/$skill_name" "$target_skill"
  echo "installed: $target_skill"
done

if [[ -n "$backup_root" ]]; then
  echo "backup: $backup_root"
fi
