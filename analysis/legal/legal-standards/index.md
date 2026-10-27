---
name: legal-standards
description: Use when a legal document is read against the professional and procedural rules for its author and that kind of document.
---

# legal-standards

```mermaid
stateDiagram-v2
  state Open <<choice>>
  state "authorization" as Authorization
  state "conduct" as Conduct
  state "impartiality" as Impartiality
  state "confidentiality" as Confidentiality
  state "procedure" as Procedure
  state "burden-of-proof" as Burden

  [*] --> Authorization
  Authorization --> Open
  Open --> Conduct: the ethical rules
  Open --> Impartiality: independence, conflicts of interest, or bias
  Open --> Confidentiality: secrecy or professional privilege
  Open --> Procedure: court procedure
  Open --> Burden: which burden applies
  Conduct --> Open
  Impartiality --> Open
  Confidentiality --> Open
  Procedure --> Open
  Burden --> Open
  Open --> [*]: no other rule is in question
```

Start with `authorization`.
Which rules apply depend on it.
Then open one sub at a time.

- `authorization` — whether this author was entitled to do the work
- `conduct` — the ethical rules for this author
- `impartiality` — independence, conflicts of interest, and bias
- `confidentiality` — secrecy and professional privilege
- `procedure` — court procedure and administration of justice
- `burden-of-proof` — which burden this matter uses
