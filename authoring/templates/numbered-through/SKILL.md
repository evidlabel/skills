---
name: numbered-through
description: |
  Use when each paragraph keeps the next number from the start of the document to the end.
  Numbering that starts again on each page is numbered-page.
license: MIT
compatibility: |
  Requires typst on PATH.
  Page and type come from typst_use.
---

# numbered-through

One file.
These are paragraph numbers, not line numbers.
The numbers run through the document.
A heading is not numbered.
The number sits in the left margin.

Page and type come from typst_use `preamble`, written inline.
The fragment below comes after that preamble.

```typst
#let p = counter("para")
#let step = p.step()
#let margin = 2em
#let display = context {
  box(align(right, p.display("1") + h(0.4em)), width: margin)
}
#set par(hanging-indent: margin)
#show par: it => {
  if it.body.at("children", default: ()).at(0, default: none) == step {
    return it
  }
  par(step + display + it.body)
}
```
