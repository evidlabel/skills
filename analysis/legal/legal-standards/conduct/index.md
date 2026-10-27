---
name: conduct
description: Use when a legal document is read against the ethical rules for its author.
---

# conduct

```mermaid
stateDiagram-v2
  state "The ethical rules for this author, for this jurisdiction and the date of the document" as Obtain
  state "The duties in that text, parsed out of it" as Parse

  [*] --> Obtain
  Obtain --> Parse
  Parse --> [*]
```

Obtain the ethical rules for this author, for this jurisdiction and the date of the document.

- code of conduct or ethical guidelines for legal professionals
- ethical guidelines for judges

The duties are the ones in that text.
Parse them out of it.
