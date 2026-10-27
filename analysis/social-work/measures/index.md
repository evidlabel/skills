---
name: measures
description: |
  Use when reading the social-work record of a measure in a disputed-facts case: what was proposed or in force, and what the record says it was for.
  The legal test of a measure is proportionality.
---

# measures

```mermaid
stateDiagram-v2
  state split <<fork>>
  state together <<join>>
  state "One measure" as One
  state "Its name, the date it started, and what the record says it was for" as Named
  state "What the record says was offered before it" as Before
  state "The stated views of the child and of the parents, by key" as Views
  state "Whether the measure in the plan matches the measure in force" as Match
  state "Hand the measure to proportionality" as Test

  [*] --> One
  One --> split
  split --> Named
  split --> Before
  split --> Views
  split --> Match
  Named --> together
  Before --> together
  Views --> together
  Match --> together
  together --> Test
  Test --> One: a measure is left
  Test --> [*]: every measure is set out
```

- each measure named, with the date it started and what the record says it was for
- what the record says was offered before it
- the child's and the parents' stated views, by key
- whether the measure in the plan matches the measure in force
- the legal test of a measure is `proportionality`
