# Methods & Schemas

## Schemas

**Report:** `{"id": str, "timestamp": ISO8601, "source": str, "text": str}`

**Gazetteer:** `{entity_type: {canonical: [aliases...]}}`

## Extraction
Regex extractors: `ipv4`, `email`, `url`, `sha256`, `crypto-address`
(`bc1…` / `0x…` / `addr-…`), `geo` (`lat,long`). Gazetteer matching is
whole-word, case-insensitive, and maps every alias to its canonical name.

## Resolution
Mentions group by `(type, canonical)`; each resolved entity carries the set of
source reports and observed surface aliases. Regex entities normalize
case-insensitively for email/url/sha256.

## Retrieval
TF-IDF with `tf = count/doc_len` and `idf = ln((1+N)/(1+df)) + 1`, ranked by
cosine similarity. Tokenizer keeps indicator punctuation so `addr-b1` and
`203.0.113.10` remain single tokens.

## Graph & correlation
Entities co-mentioned in a report get a `co-mentioned` edge; edge weight is the
number of shared reports. `correlate(value)` returns neighbors ranked by weight,
each with the shared report IDs.

## Orchestration
`answer(query)` runs a fixed plan — retrieve (TF-IDF) → extract (from the
retrieved reports) → correlate (on the most frequent entity) → summarize
(provider over the retrieved texts) — and returns citations plus a tool-by-tool
execution trace.

## Reasoning backends
`DeterministicProvider` selects the most query-relevant sentences (extractive,
reproducible). `OllamaProvider` calls a locally-served open-weight model and is
used only when reachable; the platform never depends on it.
