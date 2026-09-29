# evasiveness

Finds answers that don't answer, and vagueness on material points. Measured against the same speaker's baseline, not an ideal.

## `language/evasiveness/qa@1` (basic)

**In scope:** interview records and transcripts, hearing transcripts, email or message threads where one party asks a direct question.

**Instruction:** For each direct question put to a person, extract the answer span (verbatim, one page). If the question is in the same document, also extract the question as its own candidate. Label the answer.

**note (answer):**
```json
{"role": "answer", "q_key_hint": "<first 8 words of the question>", "respondent": "#(P1V1)", "asker": "#(P2V1)|<role>",
 "topic": "<slug>", "answer_type": "direct|partial|non-answer|deflection|counter-question|memory-claim|topic-shift|refusal",
 "confidence": 0.0}
```
**note (question):** `{"role": "question", "asker": "…", "respondent": "…", "topic": "<slug>"}`

Types: `direct` answers what was asked; `partial` answers part of it; `non-answer` responds without content; `deflection` redirects to another person's conduct; `counter-question` answers with a question; `memory-claim` ("I don't recall", "kan ikke huske"); `topic-shift` moves to another subject; `refusal` explicitly declines.

## `language/evasiveness/hedges@1` (basic)

**In scope:** any first-person account.

**Instruction:** Extract spans where an assertion about a material fact is qualified or made vague. Label the kind.

**note:** `{"speaker": "…", "topic": "<slug>", "kind": "hedge|vague-time|vague-agent|agentless-passive|approximation", "confidence": 0.0}`

Markers (non-exhaustive): "I think / I believe / maybe / sort of / around then / things happened / mistakes were made"; Danish: "vist nok", "måske", "jeg tror", "på et tidspunkt", "der blev sagt", "det kan godt være". Markers are a starting point. Label what the sentence does, not the word.

## `language/evasiveness/profile@1` (composite)

**Inputs:** passes with job prefix `language/evasiveness/qa@` (required) and `language/evasiveness/hedges@` (optional).

**Procedure:** For each respondent and topic, count answers by `answer_type` and hedges by `kind`. Compute the baseline as the same respondent's rates on topics not in dispute. A topic is flagged only when its non-direct rate clearly exceeds that respondent's baseline, with at least 3 answers on that topic.

**Finding:**
```json
{"id": "f1", "claim": "evasiveness-profile",
 "sources": [{"uuid": "…", "pass": "…", "key": "…"}],
 "values": {"respondent": "#(P1V1)", "topic": "…", "asked": 6, "direct": 1, "non_direct_rate": 0.83,
            "baseline_rate": 0.2, "hedges": 4, "flag": true}}
```

**Cautions:** Memory claims can be genuine, especially for old or routine events. Interview conditions (a leading question, the presence of the other party) can produce non-answers. Report the profile. Don't infer motive.

## Done
- Every respondent with at least one answer has a profile row.
- Flags state their baseline.
- Topics with fewer than 3 answers are listed in `gaps`.
