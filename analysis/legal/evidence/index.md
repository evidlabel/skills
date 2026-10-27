---
name: evidence
description: Use when setting out what the record shows in a disputed-facts case.
---

# evidence

```mermaid
stateDiagram-v2
  state "What it is, who wrote it, and whether the writer saw the events or heard them" as Inventory
  state "Each event names its source" as Timeline
  state "How the questions were asked, how it was recorded, how it was conducted" as Interviews
  state "Sources that support the point, and sources that contradict it" as Point

  [*] --> Inventory
  Inventory --> Inventory: the next document
  Inventory --> Timeline: the documents are listed
  Timeline --> Timeline: the next event
  Timeline --> Interviews: each event names its source
  Interviews --> Interviews: the next interview
  Interviews --> Point: the interviews are read
  Point --> Point: the next contested point
  Point --> [*]: each contested point has its sources
```

Inventory first.
For each document: what it is, who wrote it, and whether the writer saw the events or heard them.

Then a timeline.
Each event names its source.

Then the interviews, including a child's.
How the questions were asked, how it was recorded, how it was conducted.

Then each contested point: which sources support it, and which contradict it.
