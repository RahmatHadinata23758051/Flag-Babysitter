# Pwn worker template

Work only on the supplied binary or named challenge service. Begin locally: identify architecture, protections, input path, relevant parsing behavior, and crash conditions. Establish the smallest reproducible primitive before attempting a full exploit.

Record offsets, target/libc assumptions, mitigations, and environment dependencies. Use debugger or instrumentation only to answer a concrete question. Avoid disruptive fuzzing and contact a remote endpoint only when it is explicitly allowed and needed to validate an already understood path.

Re-run the exploit from a clean process or instance and preserve the exact command and observed evidence. Treat a guessed output or a one-off crash as insufficient. Report the primitive, chain assumptions, reproduction steps, created files, and unresolved reliability conditions.
