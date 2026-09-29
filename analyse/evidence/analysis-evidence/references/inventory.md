# inventory

One row per document: what it is, who wrote it, when, and how independent it is of the parties.

## `evidence/inventory/inventory@1` (composite, metadata)

**Inputs:** `evid --db evid doc list -s <slug> -f json`; each document's `info.yml`; the first page of each document (to read its authorship and kind).

**Procedure:** For each document, classify it and tag it. Only use the listed values:
- `doc_type`: `statement|submission|correspondence|interview-record|professional-report|decision|judgment|statute|guidance|other`
- `author_role`: `party|child|authority|professional|third-party|court`
- `independence`: `independent` (no stake, not commissioned by a party), `aligned` (a party, or commissioned by or close to one), `unknown`

Tag each document with `evid --db evid tag assign <uuid> type:<doc_type>`. evid stores that as `<slug>.type:<doc_type>`.

**Finding (one per document):**
```json
{"id": "f1", "claim": "document", "sources": [{"uuid": "…"}],
 "values": {"doc_type": "interview-record", "author_role": "authority", "author": "<role or token>",
            "date": "YYYY-MM-DD", "about": ["#(P1V1)", "child"], "independence": "independent",
            "aligned_with": null, "firsthand": true}}
```

**Top-level `gaps`:** list document types the case would normally have but doesn't. For example: no school record, no record of the child's own views, or a decision whose underlying report is not in the set.

## Done
- Every document has one row and one `type:` tag.
- Every `unknown` independence value is explained in the report.
