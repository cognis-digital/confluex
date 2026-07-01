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
| 500 | 3,000 | 0.0218 | 0.005 | 0.0289 | 0.0075 | 1.965 | 7,916 |
| 2,000 | 12,000 | 0.063 | 0.018 | 0.1279 | 0.0275 | 7.483 | 8,459 |
| 8,000 | 48,000 | 0.2399 | 0.0872 | 0.4856 | 0.1243 | 29.043 | 8,537 |

## Live feed coverage

- **14 keyless live feeds** across: advisories=2, osint-news=5, situational=4, threat-intel=3
- Adapters: gdelt, ioc_lines, reliefweb, rss, usgs

All numbers are produced by `bench/run_all.py` and gated in CI by `tests/test_bench.py` / `tests/test_sources.py`. See `docs/LIMITATIONS.md`.
