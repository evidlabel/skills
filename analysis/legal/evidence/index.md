---
name: evidence
description: Use when setting out what the record shows in a disputed-facts case.
---

# evidence

```mermaid
stateDiagram-v2
  state "One document: what it is, who wrote it, and whether the writer saw the events or heard them" as Inventory
  state "One event on the timeline, with its source" as Timeline
  state "One interview: how the questions were asked, how it was recorded, how it was conducted" as Interviews
  state "One contested point: the sources that support it, and the sources that contradict it" as Point

  [*] --> Inventory
  Inventory --> Inventory: a document is left
  Inventory --> Timeline: every document is listed
  Timeline --> Timeline: an event is left
  Timeline --> Interviews: every event names its source
  Timeline --> Point: the record has no interviews
  Interviews --> Interviews: an interview is left
  Interviews --> Point: every interview is read
  Point --> Point: a contested point is left
  Point --> [*]: every contested point has its sources
```

Inventory first.
For each document: what it is, who wrote it, and whether the writer saw the events or heard them.

Then a timeline.
Each event names its source.

Then the interviews, including a child's.
How the questions were asked, how it was recorded, how it was conducted.

Then each contested point: which sources support it, and which contradict it.
