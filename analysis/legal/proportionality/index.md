---
name: proportionality
description: Use when a measure is tested for proportionality.
---

# proportionality

```mermaid
stateDiagram-v2
  state "One measure" as Measure
  state "How proportionality is seen for this kind of measure, on its date" as HowSeen
  state "The statute and the decisions that jurisdiction uses" as Obtain
  state "That reading, applied to the record" as Apply
  state "The reasons the record gives" as Reasons
  state "Evidence for, evidence against, and the gaps" as Sides

  [*] --> Measure
  Measure --> HowSeen
  HowSeen --> Obtain
  Obtain --> Apply
  Apply --> Reasons
  Reasons --> Sides
  Sides --> Measure: the next measure
  Sides --> [*]: no score, and no conclusion on the measure
```

One measure at a time.

Find how proportionality is seen in the jurisdiction that applies, for this kind of measure, on the date of the measure.
Obtain that from the statute and the decisions that jurisdiction uses.
Apply it to the record.

The reasons the record gives.
The evidence for the measure, the evidence against it, and the gaps.

No score.
No conclusion on the measure.
