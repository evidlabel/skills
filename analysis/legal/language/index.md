---
name: language
description: Use when reading how things are said in a disputed-facts case — contradiction, evasiveness, manipulation, or whether a claim was witnessed or passed on.
---

# language

```mermaid
stateDiagram-v2
  state Method <<choice>>
  state "references/contradiction.md" as Contradiction
  state "references/evasiveness.md" as Evasiveness
  state "references/manipulation.md" as Manipulation
  state "references/attribution.md" as Attribution
  state "One party, read with that method. Label the span, not the person" as Party

  [*] --> Method
  Method --> Contradiction: claims that differ
  Method --> Evasiveness: answers that do not answer
  Method --> Manipulation: pressure or distortion in a message
  Method --> Attribution: whether a claim was witnessed or passed on
  Contradiction --> Party
  Evasiveness --> Party
  Manipulation --> Party
  Attribution --> Party
  Party --> Party: a party is left
  Party --> [*]: every party is read with the same method
```

Every party.
Label the span, not the person.
Load only the method in hand.

| Method | What it labels | File |
| --- | --- | --- |
| contradiction | Claims that differ within one speaker, between parties, or against the record | `references/contradiction.md` |
| evasiveness | Answers that do not answer, and hedges, against that speaker's own baseline | `references/evasiveness.md` |
| manipulation | Pressure and distortion in a message. Counts and spans, not a diagnosis | `references/manipulation.md` |
| attribution | Whether the speaker saw it, was told it, read it, or inferred it | `references/attribution.md` |
