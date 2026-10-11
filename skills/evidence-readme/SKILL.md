---
name: evidence-readme
description: Create or revise a professional, long-form repository README from verified repository evidence. Audit first, distinguish facts from inference, and avoid unsupported claims, secrets, source changes, or outward-facing mutations.
metadata:
  short-description: Evidence-backed README authoring
---

# Evidence-backed README author

Use this skill when a user asks for a repository README that should be professional, detailed, navigable, and grounded in the actual contents of the repository.

The README is a documentation artifact, not a place to fill gaps with assumptions. Treat the repository as the source of truth and preserve the user's approval boundary around source changes, GitHub changes, commits, pushes, releases, and deployments.

## Operating contract

1. Start with a read-only audit. Do not edit files before reporting the audit requested below.
2. Inspect the repository root, visible folder structure, package/config files, source entry points, existing documentation, tests, examples, and safe-to-read metadata. Do not read or print secret values, `.env` files, credentials, private keys, tokens, cookies, or other sensitive material.
3. Do not run the target application, migrations, deployments, dependency installation, destructive commands, network scans, or commands with material side effects without explicit approval. Safe inspection commands and relevant validators are allowed after implementation.
4. Build an evidence ledger. Every substantive README claim must be one of:
   - **Verified fact:** directly supported by a file, source path, test, command result, or repository metadata.
   - **Conservative inference:** a clearly labeled interpretation supported by multiple observations.
   - **Unverified:** missing evidence; omit it from claims or mark it explicitly as not verified.
5. Do not claim features, performance, security, coverage, users, production readiness, compatibility, benchmarks, or test success without repository evidence.
6. Do not copy wording, images, logos, or assets from other repositories. Use external repositories only as structural inspiration. Create original visuals when they materially improve understanding and are supported by evidence.
7. Keep the change limited to README documentation and explicitly approved documentation/assets. Do not change source behavior, package behavior, application configuration, GitHub metadata, commits, pushes, releases, or deployments unless separately authorized.

## Required audit report

Before writing or editing a README, report:

- the verified purpose and function of the project;
- the technology stack actually detected;
- source and command entry points;
- the architecture or workflow that can be supported by repository evidence;
- verified features;
- install, run, build, lint, and test commands that are actually documented or safely confirmed;
- existing documentation and its gaps;
- weaknesses of the current README, or state that no README exists;
- useful visualizations supported by the repository;
- files proposed for creation or modification;
- claims that must not be written because evidence is absent.

If the repository is empty, incomplete, or only contains planning documents, say so directly. Do not manufacture an application architecture from a roadmap or handoff document.

## README structure

After the audit and within the approved scope, write a substantial README with only sections supported by evidence. The following is a preferred structure, not a license to invent content:

1. **Hero section** — project name, concise tagline, factual one-paragraph description, and badges only for real repository status. Use an original banner only when it adds value.
2. **Contents** — useful for a long document.
3. **Problem and solution** — the demonstrated problem and how the repository addresses it; identify the intended audience only when supported by documentation or project structure.
4. **Key features** — source-backed capabilities, with links to the relevant files where useful.
5. **Architecture or how it works** — components and data/request flow supported by source. Use Mermaid only when the relationship is verifiable.
6. **Installation** — prerequisites, setup, configuration, and commands that are documented or safely verified. Never invent commands.
7. **Quick start** — a safe minimum example. Label illustrative examples as illustrative and never include real credentials.
8. **Usage examples** — verified examples and outputs; distinguish fixtures from observed output.
9. **Configuration** — names of environment variables or config keys only. Never expose secret values.
10. **Project structure** — a concise tree and responsibilities derived from actual files.
11. **Visual documentation** — Mermaid architecture, request flow, state, pipeline, or lifecycle diagrams only when source evidence supports them.
12. **Testing** — detected test commands and test types. State whether tests were inspected or run; do not claim that all tests pass unless they were actually run.
13. **Security and safety** — known boundaries and handling observed in the repository. Never call the project secure without an appropriate audit.
14. **Limitations** — missing evidence, known issues, incomplete areas, and architectural limits supported by the repository.
15. **Roadmap** — only documented TODOs, issues, plans, or explicit project decisions. Do not create a fictional roadmap.
16. **Contributing** — only documented contribution workflow, style, and checks.
17. **License** — only when a LICENSE file or reliable repository metadata provides the license.

Omit empty sections rather than filling them with boilerplate. Headings should be descriptive and the prose should remain specific to the project.

## Visual documentation

Use GitHub-renderable Mermaid fenced blocks for evidence-backed diagrams:

- `flowchart` for component, data, or pipeline relationships;
- `sequenceDiagram` for request or interaction order;
- `stateDiagram-v2` for a demonstrated state machine;
- a dependency or lifecycle diagram when the repository exposes those relationships.

Keep diagrams small, readable in light and dark themes, and accompanied by prose explaining non-obvious edges. A diagram must not replace the textual explanation or imply components that do not exist.

Create original SVG assets under `assets/` only when a static visual materially improves navigation or understanding. Every image needs useful alt text. Validate SVG as XML and avoid external assets with unclear licensing. Do not create decorative assets merely to make an empty repository look complete.

## Validation before handoff

After an approved implementation:

1. Validate relative README links.
2. Validate image and SVG paths; parse SVG as XML when SVG files were added.
3. Manually review Mermaid fences and diagram claims.
4. Run only safe, relevant validators or tests; do not install dependencies or run the application without approval.
5. Run `git diff --check` when the repository is under Git.
6. Search the proposed documentation for accidental secrets and private paths without printing sensitive values.
7. Confirm that application source and behavior did not change.
8. Report changed files, commands run and their outcomes, remaining unverifiable claims, and any intentionally omitted sections.

## Writing standard

Prefer precise, direct prose over marketing language. Explain the evidence behind important claims. Use tables for compact mappings, code fences for commands, and diagrams only when they clarify a real relationship. Do not add generic sections such as `Root Cause`, `Impact`, `Conclusion`, or `Lessons Learned` unless that repository genuinely needs one and the heading describes a specific, evidenced topic.
