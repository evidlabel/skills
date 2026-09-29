# corroboration

For each contested topic, lists which sources support it and which contradict it, and how independent those sources are.

## `evidence/corroboration/corroboration@1` (composite)

**Inputs:**
- Required: the newest `analysis/evidence/inventory/*.json`.
- At least one of: the newest `analysis/language/contradiction/*.json` (its topics) or `analysis/evidence/timeline/*.json` (its conflict entries).
- Optional: passes with job prefix `language/attribution/sources@`.

**Procedure:**
1. Topics are every `core` contradiction topic plus every timeline conflict.
2. For each topic, list the supporting and the contradicting sources. Give each source's `independence` (from the inventory) and `basis` (from attribution, where it exists).
3. Count `independent_support`. It counts only sources that are independent and first-hand. A report repeating what a party said counts as that party's account, not as independent support.

**Finding:**
```json
{"id": "f1", "claim": "corroboration",
 "sources": [{"analysis": "analysis/language/contradiction/…json", "finding": "f4"}],
 "values": {"topic": "…", "supports": [{"uuid": "…", "key": "…", "independence": "independent", "basis": "observed"}],
            "contradicts": [{"uuid": "…", "key": "…", "independence": "aligned", "basis": "reported"}],
            "independent_support": 1, "independent_contradiction": 0}}
```

## Done
- Every core topic has a row.
- Repeated accounts are traced back to where they came from, not counted twice.
