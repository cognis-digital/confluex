# Changelog

Adheres to [Semantic Versioning](https://semver.org/).

## [0.1.0] — 2026-07-01

Initial public release.

### Added
- Entity extraction (regex indicators + gazetteer named entities) — `extract`.
- Entity resolution / alias merging with provenance — `resolve`.
- TF-IDF retrieval over reports (stdlib) — `index`.
- Provenance-tracked knowledge graph + correlation — `graph`, `model`.
- Deterministic multi-agent orchestrator (retrieve→extract→correlate→summarize)
  with an auditable execution trace — `agents`.
- Pluggable reasoning backend: deterministic offline provider (default) and
  optional local Ollama provider (self-hosted open-weight models) — `llm`.
- STIX 2.1 export with deterministic IDs and source references — `stix`.
- CLI (`cognis-vanguard`) with `demo`, `query`, `extract`, `correlate`, `graph`.
- Zero-dependency, offline / air-gap capable.
- Verification harness (`bench/`): ground-truth extraction/resolution/retrieval
  metrics + performance benchmarks; results in `RESULTS.md`.
- 20 tests + 4 verification gates; GitHub Actions CI across Python 3.9–3.13.
