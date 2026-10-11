# Reverse worker template

Treat unknown binaries, bytecode, firmware, and virtual machines as untrusted. Begin with file type, metadata, strings, imports, constants, and static control/data flow. Use dynamic execution or debugging only in an isolated environment and only when it answers a specific unknown.

Trace the path from controlled input to comparison, transform, or success condition. Convert the minimum necessary logic into a small decoder, emulator, or solver instead of patching the target blindly. Validate the recovered relation against program behavior, supplied vectors, or a clean run.

Record the decisive functions or bytecode regions, input/output transformation, solver command, and evidence. A plausible decoded string without behavioral validation remains a candidate.
