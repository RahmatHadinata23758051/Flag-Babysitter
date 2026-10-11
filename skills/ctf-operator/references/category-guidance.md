# Portable category guidance

Route by the artifact and intended solve path rather than a platform label alone. Select only the guidance needed for the challenge.

| Category | First evidence-driven approach |
| --- | --- |
| Crypto | Identify scheme, parameters, and assumptions; test a bounded cryptanalytic hypothesis; verify recovered material against original ciphertext or verifier. |
| Pwn | Triage architecture, mitigations, input path, and crash behavior; establish a minimal primitive before an exploit; validate from a clean run. |
| Reverse | Start with file identification, strings, and static data/control flow; use dynamic debugging only to answer a concrete question; implement the smallest decoder or solver. |
| Web | Map only scoped routes and inputs; read supplied source first; validate one concrete flaw hypothesis with low-impact requests. |
| Forensics/stego | Preserve originals, identify format and structure, document transformations, and validate extracted material against the source artifact. |
| Malware | Start static; execute only in an isolated challenge environment when necessary; trace behavior or configuration without contacting real infrastructure. |
| OSINT | Use event-permitted public sources and supplied clues; record sources and timestamps; do not contact, impersonate, or expose people. |
| Misc | Classify the artifact or puzzle before choosing tools; automate repeatable transformations and preserve intermediate results. |
| Cloud/blockchain/mobile/hardware/ICS | Prefer supplied local artifacts, simulators, or disposable challenge instances; do not touch public services, real equipment, unrelated tenants, or funds. |

For mixed challenges, use no more than the genuinely relevant guidance. Remote/stateful services need serialized, low-noise interaction and explicit request budgets.
