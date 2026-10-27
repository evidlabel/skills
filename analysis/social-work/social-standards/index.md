---
name: social-standards
description: >
  Use when a social-work document has to be read against the rules that
  governed its author and that kind of document.
---

# social-standards

```mermaid
stateDiagram-v2
  state "Whether the author was authorized, noted on the case" as Auth
  state "A source the record treats as binding" as Source
  state "The record names it, and the evid set does not have it" as Gap
  state "What it requires of this author and this kind of document, by key" as Extract
  state "The requirement set next to what the record shows" as Beside

  [*] --> Auth
  Auth --> Source
  Source --> Gap: named by the record, and missing from the evid set
  Gap --> Source: name it, and go back to ingestion
  Source --> Extract: the set has it
  Extract --> Beside
  Beside --> Source: the next binding source
  Source --> [*]: each binding source is extracted, or named as a gap
  Beside --> [*]: what was done, and what the record does not show
```

Note whether the author was authorized, and record that on the case.
Which rules apply, and what recourse exists, depend on it.

## What to get

Take these from the case evid set (add them if not there), and only the ones the record treats as binding:

- the statute the decision applies
- the guidance the document says it followed
- the professional and ethical rules for the profession the document names
- the standard for that kind of document, when the record names one

A source the record names that is not in the set is a gap.
Name it and go back to ingestion.

## How to extract

From each of those documents, take what it requires of this author and this kind of document.
Quote the requirement by key.
Set it next to what the record shows was done, and name what the record does not show.
