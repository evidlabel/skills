---
name: proportionality
description: Use when a measure is tested for proportionality.
---

# proportionality

```mermaid
stateDiagram-v2
  state "One measure" as Measure
  state "How the jurisdiction reads proportionality for this kind of measure on its date, from the statute and the decisions it uses" as Reading
  state "The reasons the record gives for the measure" as Reasons
  state "Under that reading: the evidence for, the evidence against, and the gaps" as Sides

  [*] --> Measure
  Measure --> Reading
  Reading --> Reasons
  Reasons --> Sides
  Sides --> Measure: a measure is left
  Sides --> [*]: every measure is set out
```

One measure at a time.

Find how proportionality is seen in the jurisdiction that applies, for this kind of measure, on the date of the measure.
Obtain that from the statute and the decisions that jurisdiction uses.
Apply it to the record.

The reasons the record gives.
The evidence for the measure, the evidence against it, and the gaps.

No score.
No conclusion on the measure.
