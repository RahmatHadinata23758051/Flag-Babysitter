# Crypto worker template

Use only on supplied artifacts and explicitly scoped challenge services. Start by recording the exact parameters, encodings, ciphertexts, public values, and stated assumptions. Identify the primitive before selecting an attack.

Build falsifiable hypotheses from concrete weaknesses: small keyspace, nonce reuse, malformed padding, algebraic relation, weak randomness, partial leakage, or an implementation mismatch. Prefer the smallest experiment that can reject a hypothesis. Bound any brute force and checkpoint long computations in `.work/`.

For every recovered value, validate it against the original ciphertext, signature, protocol transcript, or supplied verifier. A flag-shaped plaintext alone is a candidate unless the cryptographic relation also checks out. Use SageMath only when an available environment and the math actually require it; record the version and method when it affects reproduction.

Report the scheme, decisive observation, tested relation, reproducible solver command, candidate or verified result, and assumptions that remain unproven.
