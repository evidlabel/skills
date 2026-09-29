# process

Did parents and child take part before each decision, and was the timing reasonable?

## `proportionality/process/participation@1` (basic)

**In scope:** decisions, hearing letters, meeting minutes, interview records, and correspondence with the authority.

**Instruction:** Extract records of participation in the decision on a measure.

**note:** `{"measure": "<slug>", "participant": "#(P1V1)|child|<role>", "kind": "heard|informed|consulted|objected|represented|child-views-recorded", "date": "YYYY-MM-DD|unknown", "confidence": 0.0}`

## `proportionality/process/process@1` (composite)

**Inputs:**
- Required: participation passes, and the newest `analysis/proportionality/measures/inventory-*.json`.
- Optional: the timeline, and the newest `analysis/evidence/interviews/quality-*.json`.

**Procedure:** For each measure, report:
- who was heard **before** the decision date, and who only after
- whether the child's views were recorded, and in what form (verbatim or summary, from interview quality)
- elapsed times: from the triggering event to the decision, and from the decision to its first review (from the timeline)

**Finding:**
```json
{"id": "f1", "claim": "process", "sources": [{"analysis": "analysis/proportionality/measures/…json", "finding": "m1"}],
 "values": {"measure": "m1", "heard_before": ["#(P1V1)"], "heard_after": ["#(P2V1)"], "child_views": "summary",
            "days_trigger_to_decision": 12, "days_decision_to_review": null}}
```

## Done
- Every measure has a process row.
- Unknown dates are listed in `gaps`.
