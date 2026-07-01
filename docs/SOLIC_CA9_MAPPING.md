# SOLIC Challenge Area 9 (Open Topic) — Capability Mapping

Vanguard addresses a concrete SOF enterprise gap: **trustworthy AI analytics at
the disconnected tactical edge.**

| SOF need | Cognis Vanguard | Module |
|---|---|---|
| Fuse multi-source reporting into one picture | Provenance-tracked knowledge graph from OSINT/SIGINT-meta/MARINT reports | `graph`, `resolve` |
| Operate offline / air-gapped | Zero-dependency, self-hosted; optional local model only | whole package |
| Trustworthy, auditable outputs | Source citations on every entity + full tool execution trace | `model`, `agents` |
| Rapid analyst tasking | Natural-language-style query → source-cited answer | `agents`, `index` |
| Own the AI (no cloud egress) | Deterministic default provider; optional local Ollama model | `llm` |
| Interoperability | STIX 2.1 export with source references | `stix` |

## TRL posture (honest)
- **Components (TRL 5–6):** extraction, resolution, TF-IDF retrieval, graph
  fusion, STIX export, and the orchestration loop are working, tested software
  with reproducible accuracy metrics (`RESULTS.md`).
- **SOF-tailored integration (prototype):** the specific mission use case,
  target-hardware edge packaging, and classified-enclave audit logging are the
  post-award prototype scope, demonstrable at the July 24 event.

As an Open Topic entry, Vanguard is intentionally adaptable to the single
highest-value SOF use case the sponsor identifies.
