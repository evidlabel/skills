# source reliability

How well professional and third-party statements are grounded.

## `credibility/source-reliability/grounds@1` (basic)

**In scope:** professional reports, authority assessments, and third-party statements (`type:professional-report`, and `type:interview-record` when it states conclusions).

**Instruction:** Extract each conclusion or assessment the author states, and label what it rests on, as the document itself says.

**note:** `{"topic": "<slug>", "grounds": "own-observation|test-or-assessment|party-report|other-report|none-stated", "party_source": "#(P1V1)|null", "method_named": "<as written>|null", "confidence": 0.0}`

## `credibility/source-reliability/reliability@1` (composite)

**Inputs:**
- Required: grounds passes, plus the newest `analysis/evidence/inventory/*.json`.
- Optional: the newest `analysis/evidence/interviews/quality-*.json`.

**Procedure:** For each document, report:
- its conclusion count
- the share of each grounds type
- `single_party_reliance`: the share of conclusions resting on only one party's report
- its independence, from the inventory
- whether both parties were heard, from the interview conditions where available
- the conclusions that rest on interpretation and have no verbatim anchor, from interview quality

**Finding:**
```json
{"id": "f1", "claim": "source-reliability", "sources": [{"uuid": "…"}],
 "values": {"conclusions": 6, "grounds": {"own-observation": 2, "party-report": 3, "none-stated": 1},
            "single_party_reliance": 0.5, "independence": "independent", "both_parties_heard": false,
            "unanchored_conclusions": 2}}
```

## Done
- Every in-scope document has a row.
- Every `none-stated` count is backed by the conclusions' keys.
