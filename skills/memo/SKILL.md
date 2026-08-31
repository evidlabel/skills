---
name: memo
description: >
  Use when the user wants a dated Typst memo that answers a question with
  labquote block quotes and asserted commentary in sections and bullets.
  Triggers on "write a memo", "legal memo", "does X collide with Y",
  "comment on §", "brief", or a labquote document that concludes.
  Do not use for citatsamling (notat), line-by-line rebuttal (rebut),
  graphical walkthroughs, or gather/keys-only rendering (labquote).
license: MIT
compatibility: Requires the labquote skill and typst on PATH.
---

# memo

Arguing style of a **labquote** document. Gather, keys, `refs.yml` → **labquote**. This file is date, shape, asserted commentary.

## Prior
- gather + keys → **labquote**. No `refs.yml` beside `main.typ` → labquote, stop
- verbatim → **citing**
- citatsamling (exhibit, don't conclude) → **notat**
- line-by-line reply → **rebut**

## Shape

`#datetime.today()` top right. Title names the question. Then:

question → clauses (`#blockq` + unpacking bullets) → analysis headings → one-sentence close → `#bibliography-custom()`

Sections and bullets, not a wall of text. Language from `#set text(lang:)` / `refs_to_typ.py --lang`.

## Prose

Prose asserts. The close answers the question.

Weight-bearing claims sit next to their `#blockq`. `#cite-ref` is back-reference to a quote already on the page, not a substitute for the box.

After `refs_to_typ.py`: write around the generated keys. Do not replace them. Do not switch to markdown `>`.

## Workflow

labquote gather first (`refs_to_typ.py --write-refs`). Then this style.

1. Keep the generated `#blockq` lines; add headings and bullets around them
2. `typst compile main.typ`. Failed anchor throws

## Mistakes
- skip labquote gather / invent `refs.yml`
- replace generated keys
- wall of text

## Integration
labquote (gather + keys) · evid · output-table last
