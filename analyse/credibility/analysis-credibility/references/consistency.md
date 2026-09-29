# consistency

Is one speaker's account of a topic stable across documents and over time?

## `credibility/consistency/consistency@1` (composite)

**Inputs:**
- Required: the newest `analysis/language/contradiction/compare-*.json`.
- Optional: the newest `analysis/language/evasiveness/profile-*.json`, and the newest `analysis/evidence/timeline/build-*.json` (its `knowledge_date` values).

**Procedure:** For each speaker and each core topic:
- Count the number of accounts.
- Count the internal contradictions, split into core and peripheral.
- Say whether the core of the account (who, what, and the outcome) stayed the same from the first account to the latest.
- Say whether the account changed after the speaker could have learned new information, meaning a change dated after the related event's `knowledge_date`.
- Add the evasiveness flag, if the evasiveness profile exists.

**Finding:**
```json
{"id": "f1", "claim": "consistency", "sources": [{"analysis": "analysis/language/contradiction/…json", "finding": "f3"}],
 "values": {"speaker": "#(P1V1)", "topic": "…", "accounts": 4, "internal_core": 1, "internal_peripheral": 2,
            "core_stable": false, "changed_after_knowledge": true, "evasiveness_flag": false}}
```

## Done
- Every speaker on every core topic has a row, including rows with zero accounts.
