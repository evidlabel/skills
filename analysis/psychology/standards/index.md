---
name: standards
description: Use when a psychologist is involved and the report is read against the rules for that psychologist and that kind of report.
---

# standards

```mermaid
stateDiagram-v2
  state InSet <<choice>>
  state NextDoc <<choice>>
  state "Whether the psychologist was authorized for this work, noted on the case" as Auth
  state "One document that governs the work, for this jurisdiction and the date" as Doc
  state "Name it as a gap, and send it back to ingestion" as Gap
  state "The diagnostic system the report uses, and the system in force at the time" as System
  state "The duties parsed from the ethical and professional guideline, set next to the report" as Duties
  state "Hand the terms to professionalism" as Terms

  [*] --> Auth
  Auth --> Doc
  Doc --> InSet
  InSet --> NextDoc: in the evid set
  InSet --> Gap: missing from the evid set
  Gap --> NextDoc
  NextDoc --> Doc: a governing document is left
  NextDoc --> System: every governing document is gathered, or named as a gap
  System --> Duties
  Duties --> Terms
  Terms --> [*]
```

Where a psychologist is involved, find whether they were authorized for this work.
Note that on the case.
Which rules apply, and what recourse exists, depend on it.

Read the report against the documents that govern the work.
Take them from the evid set for this jurisdiction and the date of the work:

- the statute
- the professional guidelines
- the ethical guidelines
- the licensing board
- the guideline for that procedure or that kind of report, such as a custody evaluation

A document that is not in the set is a gap.
Name it and go back to ingestion.

Note the diagnostic system the report uses.
Obtain which system was in force at the time of the matter, and whether the report used that one.

The full list of professional duties is the one in the ethical and professional guideline that governs this psychologist.
Parse it out of that guideline.
Look for at least:

- correct procedure
- correct handling of information
- being up to date in the field, and having the professional knowledge
- keeping professional distance
- disclosing conflicts of interest
- disclosing insufficient specialisation, and dealing with it by consultation
- correct use of professional terminology, and whether a lay reader is told what the term means

`professionalism` reads the terms in the document against that guideline.
