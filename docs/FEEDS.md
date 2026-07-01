# Live Feeds

Cognis Vanguard integrates **14 keyless live feeds** that materialize into
reports (`{id, timestamp, source, text}`) and flow through the full pipeline
(extraction → resolution → knowledge graph → retrieval → orchestration). Every
fetch caches to disk, so ingestion also runs **offline / air-gapped**.

## Feeds

| Category | Feeds |
|---|---|
| osint-news | GDELT (conflict / maritime-security / narcotics), Defense News RSS, DVIDS |
| situational | ReliefWeb, USGS (significant + M4.5), GDACS alerts |
| advisories | CISA advisories, CISA ICS advisories |
| threat-intel | abuse.ch Feodo, URLhaus, ThreatFox (materialized as per-indicator reports) |

## Adapters

- **gdelt** — GDELT DOC 2.0 `artlist` JSON → article reports
- **reliefweb** — ReliefWeb API JSON → report titles
- **usgs** — USGS GeoJSON → event reports
- **rss** — generic RSS/Atom (`<item>`/`<entry>`), HTML stripped
- **ioc_lines** — IOC blocklists; extracts the first URL/IP **by pattern** (robust
  to header rows and differing CSV layouts)

## Usage

```bash
cognis-vanguard sources-list                       # browse feeds
cognis-vanguard sources-stats                       # coverage json
cognis-vanguard sources-ingest --cache .cache       # fetch -> reports
cognis-vanguard sources-ingest --offline --cache .cache   # air-gapped replay
cognis-vanguard demo-live --query "go-fast vessel near port"   # ingest + answer
```

```python
from cognis_vanguard.sources import HttpClient, collect
from cognis_vanguard.agents import Orchestrator
reports, errors = collect(HttpClient(cache_dir=".cache"))
orch = Orchestrator(reports, {})
print(orch.answer("maritime narcotics trafficking")["answer"])
```

## Notes

All 14 feeds are keyless. Respect each provider's terms of use and rate limits.
Feeds are ingested as *reporting* for analysis; corroborate before acting. See
`docs/LIMITATIONS.md` and `NOTICE`.
