---
name: confidentiality
description: Use when a legal document is read against the rules on secrecy and professional privilege for its author.
---

# confidentiality

```mermaid
stateDiagram-v2
  state "The rules on secrecy and professional privilege for this author, this jurisdiction, and the date" as Obtain
  state "What those rules protect, set next to what the record shows was disclosed" as Pair

  [*] --> Obtain
  Obtain --> Pair
  Pair --> [*]
```

Obtain the rules on secrecy and professional privilege for this author, for this jurisdiction and the date of the document.

Set what those rules protect next to what the record shows was disclosed.
