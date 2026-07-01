# Cognis Vanguard — Verification Results

Reproduce with: `python bench/run_all.py` (regenerates this file).

Environment: CPython 3.14.0 on Windows/AMD64. Deterministic inputs and default offline provider.

## Accuracy vs. ground-truth goldset

| Task | Metric |
|---|---|
| Entity extraction | P=1.000 / R=1.000 / F1=1.000 (tp=14, fp=0, fn=0) |
| Entity resolution accuracy | 1.000 |
| Retrieval precision@1 | 1.000 |
| Retrieval recall@3 | 1.000 |
| Retrieval MRR | 1.000 |
| STIX determinism (2 runs identical) | True |

## Performance (single-thread, stdlib only)

| Reports | Mentions | Extract (s) | Resolve (s) | Graph (s) | Index (s) | Query (ms) | Reports/s |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 500 | 3,000 | 0.0187 | 0.0066 | 0.0259 | 0.0072 | 1.882 | 8,557 |
| 2,000 | 12,000 | 0.059 | 0.0517 | 0.1591 | 0.0361 | 8.335 | 6,538 |
| 8,000 | 48,000 | 0.2757 | 0.0905 | 0.4752 | 0.1187 | 29.504 | 8,332 |

All numbers are produced by `bench/run_all.py` and gated in CI by `tests/test_bench.py`. See `docs/LIMITATIONS.md` for scope caveats.
