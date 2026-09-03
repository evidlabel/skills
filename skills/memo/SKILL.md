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

## Job

The prompt names the question and the sources. Quotation method is this file.

## Prose

Prose is matter of fact. It asserts. The close answers the question. No hedging.

Attribute the written speech act next to its `#blockq`. Inner state stays in the quote: she wrote that she was frustrated ≠ she was frustrated.

One point per quote. A second clause on the same box is a new exhibit or a drop.

Same wording across parties is data (coordination, uniformity). One `#blockq` of an example. `#multicite((k2, k3, …))` the rest: they enter the bibliography, not the body.

`.typ` prose has no em dashes (U+2014). Quote bodies in `refs.yml` may. Grep the `.typ` before compile.

Every weight-bearing claim sits next to a `#blockq`. That box is the link to the local source. A claim without that neighbour is unfinished. `#cite-ref` is back-reference to a quote already on the page, not a substitute for the box. Near-repeats of that wording are `#multicite`, not more boxes.

After `refs_to_typ.py`: write around the generated keys. Do not replace them. Do not switch to markdown `>`.

## Workflow

labquote gather first (`refs_to_typ.py --write-refs`). Then this style.

1. Keep generated keys. Headings and bullets around them. Do not replace a key with paraphrase or markdown `>`
2. User critiques a quote → drop that `#blockq` first. Recast only if they keep the exhibit
3. `typst compile main.typ`. Failed anchor throws
4. Grep U+2014 in the `.typ`. Zero in prose

## Mistakes
- skip labquote gather / invent `refs.yml`
- replace generated keys
- recast a critiqued quote instead of dropping it
- ten `#blockq` of the same line, or omit the near-repeats from `#multicite` so they miss the bibliography
- infer inner state from a speech act
- wall of text
- claim with no neighbouring `#blockq`
- em dash in `.typ` prose

## Integration
labquote (gather + keys) · evid · output-table last
