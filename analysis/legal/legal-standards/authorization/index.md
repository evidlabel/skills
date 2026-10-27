---
name: authorization
description: Use when checking whether the author of a legal document was entitled to do that work.
---

# authorization

```mermaid
stateDiagram-v2
  state "Authorized for this role, in this jurisdiction, on the date of the document" as Find
  state "Noted on the case" as OnCase

  [*] --> Find
  Find --> OnCase
  OnCase --> [*]: which rules apply, and what recourse exists, depend on it
```

Find whether this author was authorized for this role, in this jurisdiction, on the date of the document.

Note that on the case.
Which rules apply, and what recourse exists, depend on it.
