# evasiveness

```mermaid
stateDiagram-v2
  state Kind <<choice>>
  state Size <<choice>>
  state Above <<choice>>
  state Next <<choice>>
  state "Copy the answer verbatim with its page, and the question where it is in the same document" as Answer
  state "One answer, one kind" as Labelled
  state "Mark each vague or qualified assertion about a material fact" as Hedges
  state "For one person and one topic, count the answers by kind, and the hedges" as Count
  state "That speaker's rate on topics that are not in dispute" as Baseline
  state "A gap, not a flag" as Gap
  state "Report the pattern. Do not infer a motive" as Flag

  [*] --> Answer
  Answer --> Kind
  Kind --> Labelled: direct
  Kind --> Labelled: partial
  Kind --> Labelled: non-answer
  Kind --> Labelled: deflection
  Kind --> Labelled: counter-question
  Kind --> Labelled: memory claim
  Kind --> Labelled: topic shift
  Kind --> Labelled: refusal
  Labelled --> Answer: an answer is left
  Labelled --> Hedges: every answer is labelled
  Hedges --> Count
  Count --> Size
  Size --> Gap: fewer than three answers on the topic
  Size --> Baseline: three or more
  Baseline --> Gap: no topic out of dispute to compare with
  Baseline --> Above
  Above --> Flag: the share that is not direct is clearly above the baseline
  Above --> Next: it is not
  Gap --> Next
  Flag --> Next
  Next --> Count: a person and topic is left
  Next --> [*]: every person and topic is counted
```

An evasive answer does not answer the question.
Vagueness on a point that matters is the same kind of thing.
The comparison is with that speaker's own usual way of answering, not with a perfect answer.

Questions and answers come from interviews, hearings, and message threads where someone asks a direct question.
The answer is copied verbatim, with its page.
When the question is in the same document, the question is copied too.

An answer is one of these.

- Direct: it answers what was asked.
- Partial: it answers only part.
- Non-answer: it responds without the content that was asked for.
- Deflection: it turns to someone else's conduct.
- Counter-question: it answers with a question.
- Memory claim: "I don't recall", "kan ikke huske", and the like.
- Topic shift: it moves to another subject.
- Refusal: it declines to answer.

A separate reading marks a vague or qualified assertion about a material fact.
The kinds are a hedge, a vague time, a vague actor, a passive with no actor, and an approximation.
Phrases such as "I think", "maybe", "around then", "mistakes were made", "vist nok", "måske", "jeg tror", "på et tidspunkt", and "der blev sagt" are only a start.
The label follows what the sentence does, not the single word.

For each person and each topic, the answers are counted by kind, and so are the hedges.
The baseline is that person's rate on topics that are not in dispute.
A topic stands out only when the share of answers that are not direct is clearly above that baseline, and there are at least three answers on the topic.
Fewer than three answers is a gap, not a flag.

A memory claim can be genuine, especially for an old or routine event.
A leading question, or the other party being in the room, can produce a non-answer.
The pattern is reported.
A motive is not inferred.
