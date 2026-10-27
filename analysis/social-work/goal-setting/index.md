---
name: goal-setting
description: Use when reading the goals in a social-work record against the manuals for that professional class.
---

# goal-setting

```mermaid
stateDiagram-v2
  state "Whether this professional class has manuals for setting goals, for this jurisdiction and this date" as Manuals
  state "Note on the case that the class has none" as None
  state "Gather the manual into the evid set" as Gather
  state "One goal, read against the manual" as Read

  [*] --> Manuals
  Manuals --> None: the class has none
  Manuals --> Gather: the record relies on a manual missing from the evid set
  Manuals --> Read: the manuals are in the set
  None --> [*]
  Gather --> Read
  Read --> Read: a goal is left
  Read --> [*]: every goal is read
```

Find whether this professional class has manuals for setting goals.
Where it has none, note that on the case.
SMART is one form those manuals take.
Obtain the manuals this class uses, for this jurisdiction and this date.
Gather them into the evid set when the record relies on them and they are missing.

Read each goal against that manual.
Note a goal the manual treats as vague, open-ended, trivial, or out of line with the interest of the person helped.
