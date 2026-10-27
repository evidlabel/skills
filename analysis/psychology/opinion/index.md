---
name: opinion
description: |
  Use when reading what a psychological report asserts in a disputed-facts case.
  Each opinion sits next to the observation the report cites for it.
---

# opinion

```mermaid
stateDiagram-v2
  state "The observation the report cites for it, both by key" as Paired
  state "An inference the report does not tie to an observation" as Gap

  [*] --> Claim
  state Claim <<choice>>
  Claim --> Paired
  Claim --> Gap
  Paired --> Claim: the next opinion
  Gap --> Claim: the next opinion
  Paired --> [*]: the statement is labelled, not the person. No score, rank, or diagnosis as a finding. Weighing it is authoring.
  Gap --> [*]: the statement is labelled, not the person. No score, rank, or diagnosis as a finding. Weighing it is authoring.
```

- each opinion next to the observation the report cites for it, both by key
- an inference the report does not tie to an observation is a gap
- label the statement, not the person
- no score, rank, or diagnosis adopted as a finding
- the opinion is the examiner's statement.
  Weighing it is authoring
