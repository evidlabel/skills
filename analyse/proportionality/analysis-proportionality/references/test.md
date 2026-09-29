# test

For each measure: suitability, necessity, and balance.

## `proportionality/test/alternatives@1` (basic)

**In scope:** the same documents as for measures.

**Instruction:** Extract mentions of less intrusive alternatives to a measure, and what happened to each.

**note:** `{"measure": "<slug>", "alternative": "<slug or ≤10 words>", "status": "considered|tried|rejected|proposed-by-party", "reason_given": "<≤15 words>|null", "confidence": 0.0}`

## `proportionality/test/test@1` (composite)

**Inputs:**
- Required: the newest `analysis/proportionality/measures/inventory-*.json`, and the newest `analysis/legal/law/criteria-*.json`.
- Optional: alternatives passes, the timeline, and the credibility composites.

**Procedure:** For each measure and each limb:
- `suitability`: evidence the measure serves its stated aim, and evidence it does not
- `necessity`: alternatives considered or tried (with outcome), alternatives proposed but not addressed, and alternatives never mentioned (a gap)
- `balance`: the documented impact on the child and on family life, against the documented risk the measure addresses

Link each limb to the legal criteria finding that defines it.

**Finding:**
```json
{"id": "f1", "claim": "proportionality-limb",
 "sources": [{"analysis": "analysis/proportionality/measures/…json", "finding": "m1"}, {"analysis": "analysis/legal/law/…json", "finding": "c4"}],
 "values": {"measure": "m1", "limb": "suitability|necessity|balance",
            "evidence_for": [{"analysis": "…", "finding": "…"}], "evidence_against": [{"uuid": "…", "key": "…"}],
            "gaps": ["no less intrusive alternative mentioned before the decision"]}}
```

## Done
- Every measure has all three limbs.
- Every limb links to a legal criteria finding.
