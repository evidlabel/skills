---
name: impartiality
description: Use when a legal document is read against the rules on independence, conflicts of interest, and bias for its author.
---

# impartiality

```mermaid
stateDiagram-v2
  state "The rules on independence, conflicts of interest, and bias for this author, this jurisdiction, and the date" as Obtain
  state "What those rules require, set next to what the record shows" as Pair

  [*] --> Obtain
  Obtain --> Pair
  Pair --> [*]
```

Obtain the rules on independence, conflicts of interest, and bias for this author, for this jurisdiction and the date of the document.

Set what those rules require next to what the record shows.
