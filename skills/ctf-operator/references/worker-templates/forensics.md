# Forensics and steganography worker template

Preserve original evidence. Work from copies inside the challenge workspace and record hashes when material transformations occur. Identify container/file formats, metadata, timestamps, encodings, embedded objects, and protocol or signal structure before choosing extraction tools.

Use file-type- or clue-driven tests rather than an unbounded tool sweep. Document every extraction, decode, and transformation path so another worker can reproduce it. For PCAP, media, or disk evidence, connect a recovered item back to its source offset, packet, stream, or artifact where possible.

Validate recovered data against original artifacts or a supplied verifier. Report evidence lineage, transformations, tool commands, extracted files, and the basis for any candidate result.
