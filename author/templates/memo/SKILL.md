---
name: memo
description: >
  Use when the user wants a dated Typst memo that answers a question with
  verbatim block quotes and asserted commentary in sections and bullets.
  Triggers on "write a memo", "legal memo", "does X collide with Y",
  "comment on §", "brief", or a quote document that concludes.
  Not for quote collections that exhibit without concluding, line-by-line
  replies, graphical maps of parties or money, or keys-only rendering.
license: MIT
compatibility: Requires typst on PATH and the @preview/labquote Typst package.
---

# memo

A dated memo that answers one question, built from verbatim quotes. A document that only exhibits the quotes is `quote_summary`.

## Precondition
`refs.yml` and a generated `main.typ` (with `#blockq` lines) sit side by side. If either is missing, stop and say so. Never write `refs.yml` or keys by hand.

## Shape
Date top right. The title names the question. A To/From/Date/Subject grid is the `memo` title block from typst_use, for correspondence. Then:

question → clauses (`#blockq` + unpacking bullets) → analysis headings → one-sentence close → `#bibliography-custom()`

Sections and bullets, not a wall of text. Language from `#set text(lang: …)`.

```typst
#import "@preview/labquote:0.1.0": *
#set text(lang: "da")
#setup(yaml("refs.yml"))

#align(right)[#datetime.today().display()]
= <The question>

== Question
<One paragraph stating what is asked.>

== Clauses
#blockq("<generated key>")
- <what this passage establishes>

== Analysis
- <asserted claim, next to the quote that carries it>

== Conclusion
<One sentence that answers the question.>

#bibliography-custom()
```

## Prose
Prose asserts. The close answers the question. Weight-bearing claims sit next to their `#blockq`. `#cite-ref` is a back-reference to a quote already on the page, not a substitute for the box. Write around the generated keys; do not replace them; do not switch to markdown `>`.

## Output
`typst compile main.typ` → `main.pdf`. A failed anchor throws. The PDF is a dated snapshot: one memo per angle, and competing angles are separate PDFs.

## Mistakes
- Inventing `refs.yml` or keys
- Replacing generated keys
- A wall of text
- Editing an existing memo PDF instead of authoring a new dated one
