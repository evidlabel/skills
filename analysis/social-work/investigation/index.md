---
name: investigation
description: |
  Use when reading a social-work investigation in a disputed-facts case.
  What was looked at, who was spoken to, and what the record is missing.
---

# investigation

```mermaid
stateDiagram-v2
  state split <<fork>>
  state together <<join>>
  state "What the investigation looked at" as Looked
  state "Who was spoken to, and who was not" as Spoken
  state "What the record contains, and what the investigation says is missing" as Contents
  state "The statements of the child, by key, separate from the summary of the caseworker" as Child

  [*] --> split
  split --> Looked
  split --> Spoken
  split --> Contents
  split --> Child
  Looked --> together
  Spoken --> together
  Contents --> together
  Child --> together
  together --> [*]
```

- what the investigation looked at: the child, the home, school, health, the network
- who was spoken to, and who was not
- what the record contains, and what the investigation says is missing
- the child's statements by key, separate from the caseworker's summary
- no score for a parent or a child

