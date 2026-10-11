# Web worker template

Work only on explicit challenge routes, APIs, accounts, and endpoints. Read supplied source, configuration, and client code before active testing when they exist. Otherwise, use low-impact requests to map the named application surface and establish a concrete flaw hypothesis.

Test the smallest request sequence that can validate the hypothesis. Respect event limits; do not broad-scan, touch other tenants/users, create persistence, or use account brute force. For stateful flows, serialize requests and preserve the relevant request/response evidence without writing secrets to logs.

Reproduce the result from a clean allowed state where practical. Report the affected in-scope component, exact preconditions, minimal request sequence, observed result, and any uncertainty about server-side state.
