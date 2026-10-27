---
name: goal-setting
description: Use when reading the goals in a social-work record against the manuals for that professional class.
---

# goal-setting

```mermaid
stateDiagram-v2
  state "The manuals this professional class uses for setting goals, for this jurisdiction and this date" as Manuals
  state "Gather that manual into the evid set" as Gather
  state "A goal, read against that manual" as Read

  [*] --> Manuals
  Manuals --> Gather: a manual the record relies on is missing from the evid set
  Gather --> Read
  Manuals --> Read: the manuals are in the set
  Read --> Read: the next goal
  Read --> [*]: each goal has been read
```

Find whether this professional class has manuals for setting goals.
SMART is one form those manuals take.
Obtain the manuals this class uses, for this jurisdiction and this date.
Gather them into the evid set when the record relies on them and they are missing.

Read each goal against that manual.
Note a goal the manual treats as vague, open-ended, trivial, or out of line with the interest of the person helped.
