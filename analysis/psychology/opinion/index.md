---
name: opinion
description: |
  Use when reading what a psychological report asserts in a disputed-facts case.
  Each opinion sits next to the observation the report cites for it.
---

# opinion

```mermaid
stateDiagram-v2
  state Tie <<choice>>
  state Next <<choice>>
  state "One opinion in the report" as Claim
  state "Set it next to the observation the report cites, both by key" as Paired
  state "Mark it as a gap" as Gap

  [*] --> Claim
  Claim --> Tie
  Tie --> Paired: the report cites an observation for it
  Tie --> Gap: the report does not tie it to an observation
  Paired --> Next
  Gap --> Next
  Next --> Claim: an opinion is left
  Next --> [*]: every opinion is set out
```

- each opinion next to the observation the report cites for it, both by key
- an inference the report does not tie to an observation is a gap
- label the statement, not the person
- no score, rank, or diagnosis adopted as a finding
- the opinion is the examiner's statement.
  Weighing it is authoring
