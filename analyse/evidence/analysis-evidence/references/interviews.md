# interviews

How an interview was conducted and written up. This matters most for interviews with a child, and for authority interviews whose summaries later carry weight. The method analyses the record. It never re-interviews anyone.

## `evidence/interviews/conditions@1` (basic)

**In scope:** interview records, transcripts, and summaries (`type:interview-record`).

**Instruction:** Extract the stated conditions of the interview.

**note:** `{"field": "date|place|present|duration|initiated_by|purpose|prior_contact|recording", "value": "<normalised value>", "confidence": 0.0}`

Examples: `present` = `["caseworker", "#(P1V1)"]`; `recording` = `verbatim|audio|notes|summary-after`.

## `evidence/interviews/questions@1` (basic)

**Instruction:** Extract each question put to the interviewee, where the record shows questions. Label its type.

**note:** `{"asker": "<role>", "topic": "<slug>", "q_type": "open|focused|option-posing|leading|suggestive|repeated", "confidence": 0.0}`

- `open` — invites a free account ("Tell me about…", "Fortæl om…")
- `focused` — asks for a specific detail (who, where, when)
- `option-posing` — offers choices
- `leading` — the wording implies the answer
- `suggestive` — introduces information the interviewee hasn't given
- `repeated` — asks again after an answer was given

## `evidence/interviews/record-form@1` (basic)

**Instruction:** Label each passage of the record by its form.

**note:** `{"form": "verbatim|summary|interpretation|conclusion", "about": "#(P1V1)|child", "topic": "<slug>", "confidence": 0.0}`

- `verbatim` — the interviewee's own words, marked as a quote
- `summary` — the writer restates what was said
- `interpretation` — the writer adds meaning ("the child seemed…", "it is assessed that…")
- `conclusion` — the writer states a finding or recommendation

## `evidence/interviews/quality@1` (composite)

**Inputs:** the three basic passes above, for each interview record (required).

**Procedure:** For each interview, report:
- the conditions
- the share of each question type
- the share of each record form
- **anchored statements**: for each `conclusion`, whether an earlier `verbatim` passage on the same topic supports it, or only `summary` or `interpretation` does
- **question-answer linkage**: for key statements on core topics, whether they came after an open or a leading or suggestive question

**Finding (one per interview):**
```json
{"id": "f1", "claim": "interview-quality", "sources": [{"uuid": "…"}],
 "values": {"conditions": {"present": ["caseworker", "#(P1V1)"], "recording": "summary-after"},
            "q_types": {"open": 3, "leading": 5}, "forms": {"verbatim": 2, "summary": 9, "interpretation": 4, "conclusion": 2},
            "conclusions_without_verbatim": [{"uuid": "…", "pass": "…", "key": "…"}],
            "statements_after_leading": [{"uuid": "…", "pass": "…", "key": "…"}]}}
```

**Cautions:** A summary-only record is common, and it isn't improper in itself. Report the form without adding judgment.

## Done
- Every interview record has all three basic passes and one quality finding.
- Records that show no questions say so in `gaps`.
