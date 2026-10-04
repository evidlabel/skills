# contradiction

Finds where accounts of the same thing differ: within one speaker over time, between parties, or against the documentary record.

## `language/contradiction/claims@1` (basic)

**In scope:** statements, submissions, emails/messages, interview records, reports that quote a person.

**Instruction:** Extract every assertion of fact about an event, a condition, or a person's conduct. One candidate per assertion, copied verbatim, one page. Skip opinions, legal argument, and pleasantries.

**note:**
```json
{"speaker": "#(P1V1)", "topic": "<event-or-condition slug>", "event_date": "YYYY-MM-DD|YYYY-MM|YYYY|unknown",
 "polarity": "affirms|denies", "proposition": "<≤15 words, neutral restatement>", "confidence": 0.0}
```
- `topic`: `<what>-<when>` in lowercase kebab, e.g. `handover-2026-03-04`, `school-absence-2026-spring`. Reuse existing topic slugs from earlier passes in the set (read them from `machine/*.json` notes first).
- `proposition`: a neutral paraphrase for grouping only. Never cite it; cite the key.
- `speaker`: the person making the assertion, not the document author when a report quotes someone.

## `language/contradiction/compare@1` (composite)

**Inputs:** all passes with job prefix `language/contradiction/claims@`. Optional: the newest `analysis/evidence/timeline/*.json` (the record to compare against).

**Procedure:**
1. Gather every claim note with its key. Normalise topics: merge slugs that name the same event (draft the merge map in `scratch/topics.json`; put the final map in a top-level `"topic_map": {"<old slug>": "<canonical slug>"}` field of the composite).
2. Within each topic, compare propositions pairwise. Classify each conflicting pair:
   - `internal` — same speaker, different documents or dates
   - `cross-party` — different speakers
   - `with-record` — a claim against a timeline event sourced from a document that is not that speaker's own account
3. Mark `materiality`: `core` if the topic is one the case turns on (the user or the question names it), else `peripheral`.
4. Record consistent clusters too (`claim: "consistent"`); agreement is evidence as well.

**Finding:**
```json
{"id": "f1", "claim": "contradiction",
 "sources": [{"uuid": "…", "pass": "…", "key": "a1b2:q3"}, {"uuid": "…", "pass": "…", "key": "c3d4:q7"}],
 "values": {"topic": "handover-2026-03-04", "type": "internal|cross-party|with-record", "materiality": "core|peripheral",
            "speakers": ["#(P1V1)"], "dates_asserted": ["2026-03-04", "2026-03-05"]}}
```

**Cautions (put them in the report):** People's accounts of the same event naturally vary in peripheral detail, and accounts change as memory fades. A contradiction on its own is not a finding of untruthfulness. Report the conflict. Weighing it is not part of this step.

## Done
- Every claim with a key belongs to a topic.
- Every conflict found is either classified or listed in `gaps` as unresolvable (for example, a missing date).
