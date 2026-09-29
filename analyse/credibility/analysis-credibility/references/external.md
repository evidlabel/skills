# external consistency

Does a speaker's account agree with independent sources and the documentary record?

## `credibility/external/external@1` (composite)

**Inputs:**
- Required: the newest `analysis/evidence/corroboration/corroboration-*.json`.
- Optional: the newest `analysis/language/contradiction/compare-*.json` (its `with-record` conflicts).

**Procedure:** For each speaker and each core topic, report:
- the independent support and independent contradiction counts
- the number of `with-record` conflicts
- whether the only support comes from sources aligned with that speaker

**Finding:**
```json
{"id": "f1", "claim": "external-consistency", "sources": [{"analysis": "analysis/evidence/corroboration/…json", "finding": "f2"}],
 "values": {"speaker": "#(P1V1)", "topic": "…", "independent_support": 0, "independent_contradiction": 2,
            "with_record_conflicts": 1, "support_only_aligned": true}}
```

## Done
- Every speaker on every core topic has a row.
