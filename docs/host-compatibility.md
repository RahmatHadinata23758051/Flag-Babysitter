# Host compatibility

Flag Babysitter publishes three portable Agent Skills. The canonical unit is a folder containing `SKILL.md`, optional references, and optional scripts. The repository does not ship separate copies of the instructions for each agent CLI.

## What is verified here

`python scripts/validate_repo.py` proves that each bundled skill has the required frontmatter, internal Markdown links resolve, the installer copies all three directory trees to an explicitly chosen destination, and the offline fixture passes. It does not start or configure an external AI CLI.

## Documented host layouts

| Host | Documented discovery or packaging route | Repository guidance |
| --- | --- | --- |
| [Gemini CLI](https://geminicli.com/docs/cli/using-agent-skills/) | User: `~/.gemini/skills/` or `~/.agents/skills/`; workspace: `.gemini/skills/` or `.agents/skills/`. | Use the installer with the selected parent directory, or Gemini's own skill-management command where appropriate. |
| [Cursor](https://cursor.com/docs/skills) | Discovers `.agents/skills/`, `.cursor/skills/`, and several compatible host directories. | Use `.agents/skills/` for a workspace shared with Gemini CLI, or a Cursor-native location. |
| [Claude Code](https://code.claude.com/docs/en/skills) | Skills are reusable, on-demand workflows; project skills use `.claude/skills/<name>/SKILL.md`. | Use the installer with `.claude/skills` for a workspace-scoped copy. |
| [OpenAI skill runtimes](https://developers.openai.com/api/docs/guides/tools-skills) | A host discovers `SKILL.md` directories supplied as capability directories or uploaded skill bundles. | Provide a single skill folder per host bundle when required; do not upload the entire repository as one skill. |

The table is based on the linked vendor documentation, not an end-to-end runtime test performed by this repository. Host features, directory precedence, consent prompts, and UI invocation syntax can change independently.

## Optional OpenAI metadata

Each skill includes `agents/openai.yaml` for OpenAI-facing display metadata. The canonical instructions remain in `SKILL.md`; other hosts may ignore `agents/openai.yaml` without losing the documented workflow.

## Unsupported hosts

Not every AI CLI implements Agent Skills or discovers `SKILL.md`. For an unlisted host, do not assume compatibility. Check its documentation for Agent Skills or an equivalent extensibility mechanism, then either install into its documented skill root or provide the relevant `SKILL.md` as user-controlled context.
