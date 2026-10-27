---
name: procedure
description: Use when a legal document is read against court procedure or the rules on administration of justice.
---

# procedure

```mermaid
stateDiagram-v2
  state "The procedural rules for this court and this kind of document, for this jurisdiction and the date" as Obtain

  [*] --> Obtain
  Obtain --> [*]
```

Obtain the procedural rules for this court and this kind of document, for this jurisdiction and the date of the document.

- court procedural manuals
- law and judicial guidelines on administration of justice
