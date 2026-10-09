---
name: numbered-page
description: |
  Use when paragraph numbers start again at 1 on each page.
  Numbers that run through the whole document are numbered-through.
license: MIT
compatibility: |
  Requires typst on PATH.
  Page and type come from typst_use.
---

# numbered-page

One file.
These are paragraph numbers, not line numbers.
Each page starts its paragraphs at 1.
A heading is not numbered.
The number sits in the left margin.

Page and type come from typst_use `preamble`, written inline.
The fragment below comes after that preamble.
The page header is where the count goes back to zero.
A running header, if the document has one, goes in that same header.

```typst
#let p = counter("para")
#let step = p.step()
#let margin = 2em
#let display = context {
  box(align(right, p.display("1") + h(0.4em)), width: margin)
}
#set par(hanging-indent: margin)
#set page(header: context {
  counter("para").update(0)
})
#show par: it => {
  if it.body.at("children", default: ()).at(0, default: none) == step {
    return it
  }
  par(step + display + it.body)
}
```
