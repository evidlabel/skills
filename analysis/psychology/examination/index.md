---
name: examination
description: Use for psychological examinations.
---

# examination

```mermaid
stateDiagram-v2
  state "Who asked, and the question that was asked" as Mandate
  state "Who was seen, who was not, and how many times" as Seen
  state "The questions, tests, and observations the report says were used" as Used
  state "What the report says it did not do" as NotDone
  state "The procedure in the words of the report, quoted by key" as Procedure
  state "The conclusion of the examiner, read under opinion" as Conclusion

  [*] --> split
  state split <<fork>>
  split --> Mandate
  split --> Seen
  split --> Used
  split --> NotDone
  split --> Procedure
  Mandate --> together
  Seen --> together
  Used --> together
  NotDone --> together
  Procedure --> together
  state together <<join>>
  together --> Conclusion
  Conclusion --> [*]
```

- the mandate: who asked, and the question that was asked
- who was seen, who was not, and how many times
- the questions, tests, and observations the report says were used
- what the report says it did not do
- the procedure in the report's words, quoted by key
- the examiner's conclusion is a separate statement.
  It is read under `opinion`
