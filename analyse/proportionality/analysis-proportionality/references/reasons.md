# reasons

Are the reasons a decision gives supported by the record?

## `proportionality/reasons/reasons@1` (basic)

**In scope:** decisions and the reports they rely on.

**Instruction:** Extract each reason stated for a measure.

**note:** `{"measure": "<slug>", "reason_topic": "<slug>", "reason_kind": "fact|assessment|risk|legal", "confidence": 0.0}`

## `proportionality/reasons/support@1` (composite)

**Inputs:**
- Required: reasons passes, and the newest `analysis/proportionality/measures/inventory-*.json`.
- Optional: the timeline, corroboration, and the credibility composites.

**Procedure:** Link each reason to fact findings on the same topic, and classify its support:
- `supported-independent`
- `supported-aligned-only`
- `contested`
- `unsupported-in-record`

**Finding:**
```json
{"id": "f1", "claim": "reason-support", "sources": [{"uuid": "…", "pass": "…", "key": "…"}],
 "values": {"measure": "m1", "reason_topic": "…", "support": "contested",
            "for": [{"analysis": "…", "finding": "…"}], "against": [{"analysis": "…", "finding": "…"}]}}
```

## Done
- Every stated reason has a support class and its links.
