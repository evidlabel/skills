---
name: quote_summary
description: |
  Use when the user wants a Typst document that is only a set of relevant verbatim quotes using labquote.
  Triggers on "quote summary", "the relevant quotes", "citatsamling", "just the quotes".
  Not an arguing memo (memo), and not gather or keys-only rendering (labquote).
license: MIT
compatibility: Requires typst on PATH and the @preview/labquote Typst package.
---

# quote_summary

A document that exhibits the relevant quotes and stops.
It does not answer a question.
Copy `template/main.typ` beside `refs.yml`.

## Precondition
`refs.yml` is already beside the document.
If it is missing, stop and use labquote.
Never write `refs.yml` or keys by hand.

The `#blockq` lines come from labquote:

```bash
python3 <labquote>/scripts/refs_to_typ.py refs.yml -o main.typ --write-refs
```

Put those keys into the template.
Do not replace them.
Do not switch to markdown `>`.

## Shape
A title that names the topic.
Then the quotes, in the order they should be read.
Then `#bibliography-custom()`.

No question heading, no analysis, and no conclusion.
A lead-in may name the source.
It does not say what the quote proves.
The order is the only arrangement.

## Output
`typst compile main.typ`.
A failed anchor throws.
