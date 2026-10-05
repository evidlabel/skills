# manipulation

Labels observable pressure and distortion tactics in messages between parties, or aimed at the child.
It describes messages.
It does not diagnose people.

The labels in the table are how this pass records a span.
Which of them this case can use comes from the statute and the guidance in the evid set: coercive control, psychological violence, or the definition the record itself uses.

## `language/manipulation/tactics@1` (basic)

**In scope:** messages, emails, letters, and recorded statements addressed from one person to another (party to party, party to child, party to authority).

**Instruction:** Extract spans that use one of the tactics below.
One candidate per span, one tactic label per candidate (the strongest).
Skip ordinary disagreement and firm but plain refusals.

**note:**
```json
{"from": "#(P1V1)", "to": "#(P2V1)|child|<authority role>", "tactic": "<label>", "target_topic": "<slug>",
 "date": "YYYY-MM-DD|unknown", "confidence": 0.0}
```

| Label | What the span does |
| --- | --- |
| `threat` | States a harm, explicit or implied, unless the recipient complies |
| `ultimatum` | Forces a deadline or a single choice ("either … or …") on an open matter |
| `guilt` | Makes the recipient responsible for the sender's or child's feelings in order to obtain compliance |
| `minimisation` | Shrinks the sender's own reported conduct ("it was only…", "overreacting") |
| `blame-shift` | Answers a point about the sender's conduct by moving responsibility to the recipient or others |
| `reality-denial` | Denies that an event or statement happened ("that never happened", "I never said…") |
| `child-as-messenger` | Routes adult conflict through the child, or asks the child to carry messages |
| `loaded-characterisation` | Describes the other party with a charged label instead of conduct |
| `false-dilemma` | Presents two options as the only ones when others are plainly available |

## `language/manipulation/pattern@1` (composite)

**Inputs:** passes with job prefix `language/manipulation/tactics@` (required).
Optional: the newest `analysis/evidence/timeline/*.json` and `analysis/language/contradiction/*.json`.

**Procedure:**
1. Count tactics per `from`→`to` direction, per month.
2. Report the trend: `rising`, `falling`, `stable`, or `episodic`.
3. Check each `reality-denial` against the optional inputs.
   If the record shows the denied event, add `values.record_conflict` with the source of that event.
   If no record exists either way, list it under `gaps`.
4. Always report both directions for every pair of parties, including zero counts.

**Finding:**
```json
{"id": "f1", "claim": "tactic-pattern",
 "sources": [{"uuid": "…", "pass": "…", "key": "…"}],
 "values": {"from": "#(P1V1)", "to": "#(P2V1)", "counts": {"guilt": 5, "threat": 1}, "by_month": {"2026-03": 4},
            "trend": "rising", "record_conflict": [{"analysis": "analysis/evidence/timeline/…json", "finding": "f12"}]}}
```

**Rules:** Never use clinical or syndrome terms (e.g. "narcissist", "parental alienation syndrome") for a person.
Findings are counts and spans.
Whether a pattern matters legally is decided in authoring.

## Done
- Both directions are reported for every pair of parties.
- Every `reality-denial` has either a record check or a gap.
