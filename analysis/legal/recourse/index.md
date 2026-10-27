---
name: recourse
description: Use when a matter needs the routes of recourse, and which of them are commonly used.
---

# recourse

```mermaid
stateDiagram-v2
  state "Legal routes, for this jurisdiction and this date" as Legal
  state "Routes through other professionals" as Professional
  state "Restrictions on the media in legal cases" as Media
  state "The routes most commonly used, and their potential effectiveness" as Common

  [*] --> split
  state split <<fork>>
  split --> Legal
  split --> Professional
  split --> Media
  Legal --> together
  Professional --> together
  Media --> together
  state together <<join>>
  together --> Common
  Common --> [*]
```

For a matter, identify the routes of recourse for the jurisdiction and the date.

- Legal
  - Appeal a case.
  - A complaint about the case, or about the behavior of a professional in the case.
  - Start a case in another system, such as criminal, civil, or human rights.
- Other professionals
  - Appeals boards of professional bodies.
  - Ethics committees.
  - Legal action.
- Media
  - Restrictions on the media in legal cases.

When working with the user on recourse, identify the routes most commonly used, their potential effectiveness, and so on.
