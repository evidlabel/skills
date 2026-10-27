---
name: burden-of-proof
description: Use when checking which burden of proof applies to a legal matter.
---

# burden-of-proof

```mermaid
stateDiagram-v2
  state "The jurisdiction, the type of court, and the burden that applies" as Check

  [*] --> Check
  Check --> Check: another burden on this matter
  Check --> [*]: each burden is named, including where several apply at once
```

Check the jurisdiction and type of court and the burden of proof that applies.
Carefully navigate and explain when multiple BoP are relevant in a case. 
  Example: 
    - Family law matter --> civil BoP
    - False statement to court in above case --> criminal BoP
