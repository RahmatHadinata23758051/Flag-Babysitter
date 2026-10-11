# Skill routing and instruction precedence

Choose instructions in this order. Higher items always win when they conflict.

1. Host policy, event rules, explicit user authorization, and exact allowed scope.
2. `ctf-operator` boundaries: isolated workspace, at most three workers, no credential sharing, independent verification, and user-controlled submission.
3. The task card and a user-supplied category template, when one is provided for this event.
4. The matching bundled worker template in `worker-templates/` when no user template exists, or as a portable supplement when the user requests both.
5. A relevant installed specialist skill, such as `ctf-crypto`, `ctf-pwn`, `ctf-reverse`, or `ctf-web`.
6. An optional third-party companion reference, used only when installed, relevant, and compatible with every higher item.

Never use lower-priority material to expand scope, send credentials to a worker, submit a flag, bypass a rate limit, or replace verification evidence.

## Selection procedure

1. Classify by artifact and intended solve path, not only a platform label.
2. Check whether the event workspace contains a user template. If it does, make that template the primary technical instruction.
3. Otherwise select exactly one bundled template below. Mixed challenges may use two only when both are necessary.
4. Check whether a matching specialist skill is already installed. Load it as a focused supplement; do not assume it exists.
5. For remote or stateful services, use a harness/oracle technique skill only if installed and only after the target allowlist, request budget, and serialization requirements are in the task card.
6. Record the chosen template and supplemental skill in the worker task card.

## Worker prompt assembly

Construct each worker prompt from four parts, in this order:

```text
1. Completed worker task card: scope, objective, budget, and stop condition.
2. One primary technical template: user-supplied when present; otherwise bundled.
3. Focused material from one installed specialist skill, only if selected by routing.
4. Required worker report: status, evidence, reproduction, files, uncertainty, checkpoint.
```

Do not paste an entire external skill pack into every task. The primary template carries the category workflow; supplemental skills fill a concrete knowledge gap for the selected challenge.

| Challenge path | Primary bundled template | Optional installed specialist examples |
| --- | --- | --- |
| Crypto/math | [crypto.md](worker-templates/crypto.md) | `ctf-crypto`, `crypto-ctf` |
| Pwn/binary exploitation | [pwn.md](worker-templates/pwn.md) | `ctf-pwn`, `pwn-ctf` |
| Reverse/bytecode/VM | [reverse.md](worker-templates/reverse.md) | `ctf-reverse`, `reverse-ctf` |
| Web/API | [web.md](worker-templates/web.md) | `ctf-web`, `web-ctf` |
| Disk, PCAP, media, stego | [forensics.md](worker-templates/forensics.md) | `ctf-forensics`, `forensics-ctf` |
| Suspicious binary/script/config | [malware.md](worker-templates/malware.md) | `ctf-malware`, `malware-ctf` |
| OSINT, encoding, puzzle, jail | [osint-misc.md](worker-templates/osint-misc.md) | `ctf-osint`, `ctf-misc`, `osint-ctf`, `misc-ctf` |
| AI/ML | [ai-ml.md](worker-templates/ai-ml.md) | `ctf-ai-ml`, `ai-ml-ctf` |
| Blockchain, cloud, mobile, hardware, ICS, game, satellite | [systems.md](worker-templates/systems.md) | a relevant installed domain specialist |

The examples in the final column are integration names, not repository dependencies. Their availability and license are outside this project.
