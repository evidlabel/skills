// Shell from typst_use. Chapter prose lives in chapters/, not here.
// preamble --preset legal --lang da --sec-numbering "1.1" --running-header "Title"
// title --doc-type book --title "Title" --subtitle "Subtitle" --author "Author" --date "2026"
// outline --title Indhold --depth 2

#set text(font: "DejaVu Serif", size: 12pt, lang: "da")
#set page(paper: "a4", margin: (top: 2.5cm, bottom: 2.5cm, left: 3cm, right: 2.5cm), numbering: "1", number-align: center)
#set par(justify: true, leading: 0.75em, first-line-indent: 0em, spacing: 0.9em)
#set heading(numbering: "1.1")
#set page(header: context {
  if counter(page).get().first() > 1 {
    align(right, text(size: 9pt, fill: luma(35%))[Title])
  }
})
#show heading: set block(above: 1.1em, below: 0.5em)
#show heading.where(level: 1): set text(size: 1.15em, weight: "bold")
#show heading.where(level: 2): set text(size: 1.0em, weight: "bold")

#v(2.5cm)
#align(center, text(size: 22pt, weight: "bold")[Title])
#align(center, text(size: 12pt, style: "italic", fill: luma(20%))[Subtitle])
#v(1.5cm)
#align(center, text(size: 11pt)[Author])
#align(center, text(size: 10pt, fill: luma(35%))[2026])
#pagebreak()

#outline(title: [Indhold], depth: 2)
#pagebreak()

#include "chapters/01.typ"
#include "chapters/02.typ"
