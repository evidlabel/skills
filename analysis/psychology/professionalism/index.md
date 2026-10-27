---
name: professionalism
description: |
  Use when reading a psychologist's document for its terms.
  Whether they are the professional terms, whether they are used correctly, and whether a lay reader is told what they mean.
---

# professionalism

```mermaid
stateDiagram-v2
  state "A term in the document" as Term
  state "Whether it is the professional term" as Professional
  state "Whether it is used correctly" as Used
  state "Where a layperson has to read the document, whether the term is explained" as Lay

  [*] --> Term
  Term --> Professional
  Professional --> Used
  Used --> Lay
  Lay --> Term: the next term
  Lay --> [*]
```

When reading a document written by a psychologist, look at the terminology.

Are the terms the correct professional terms?
Are they used correctly?
Where a layperson has to read the document, does the psychologist explain the term?
