---
name: governing
description: Use when setting the law that governs a disputed-facts case next to the record.
---

# governing

```mermaid
stateDiagram-v2
  state "The statute, what it requires" as Statute
  state "The findings of fact against that" as Findings
  state "The guidance, what it requires" as Guidance
  state "What the record shows was done" as Shown
  state "The judgments" as Judgments
  state "Compared on the factors that decided them" as Compared

  [*] --> split
  state split <<fork>>
  split --> Statute
  split --> Guidance
  split --> Judgments
  Statute --> Findings
  Guidance --> Shown
  Judgments --> Compared
  Findings --> together
  Shown --> together
  Compared --> together
  state together <<join>>
  together --> [*]
```

The statute: what it requires, then the findings of fact against that.

The guidance: what it requires, then what the record shows was done.

The judgments, compared on the factors that decided them.
