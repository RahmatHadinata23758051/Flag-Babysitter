---
name: ctf-writeup-custom
description: Write detailed, reproducible, website-ready CTF walkthroughs after an independently verified solution. Use for evidence-backed documentation, not solving, submission, or generic report templates.
metadata:
  short-description: Evidence-backed CTF writeups
---

# CTF writeup author

Use this skill only after a challenge solution has been independently verified. It creates documentation; it does not solve challenges, log in, submit flags, or infer missing evidence.

## Inputs

Gather the challenge title and category, event context if known, original prompt, supplied artifacts, verified evidence, solver path, commands and environment, and any site or event formatting requirements. If important evidence is missing, ask the orchestrator for it or clearly mark the draft as incomplete.

## Writing standard

1. Reconstruct the supported proof path: supplied input → observation → reasoning → implementation → verified result.
2. Explain every meaningful transition: what was observed, what it implied, what was tested, and how the result changed the solve path.
3. Use clear, natural language selected by the user or project configuration. Choose headings from the challenge reasoning; do not force generic sections such as `Root Cause`, `Impact`, or `Conclusion`.
4. Include a complete reproducible solver or link to the adjacent solver file. State invocation, inputs, dependencies, and expected success signal without inventing output.
5. Use Mermaid only when it clarifies a real flow, protocol, state, or dependency. For crypto, use Markdown LaTeX for the actual derivation; diagrams are supplementary.
6. Save `Readme.md` in the challenge directory unless the event or publication site requires another location.
7. Before handoff, check links, code, claims, Mermaid fences, equations, and output against the verified evidence.

Read [the editorial reference](references/style.md) for the full writing and rendering rules.

## Boundaries

- Never claim platform acceptance without the relevant platform response.
- Never fabricate commands, outputs, screenshots, derivations, artifacts, or a flag.
- Preserve event-required formatting when it conflicts with this style, while keeping evidence and reproducibility.
- Keep the walkthrough focused on the challenge-specific proof path; omit filler and repeated summaries.
