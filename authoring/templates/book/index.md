---
name: book
description: |
  Use when the user wants a Typst book or study whose chapters are separate files.
  Triggers on "book", "chapters", "study".
  Not a memo, not a quote collection, and not the page setup itself (typst_use).
license: MIT
compatibility: |
  Requires typst on PATH.
  Page and title come from typst_use.
---

# book

A book is a title page, an outline, and one file per chapter.
Copy `template/` as the starting tree.

```
book/
  main.typ
  chapters/01.typ
  chapters/02.typ
```

`main.typ` holds the page, the type, the title page, the outline, and the `#include` lines, in that order.
Those three blocks come from typst_use.
They are inline.
Do not `#include` a preamble file: `#set` rules inside an include do not apply to the rest of the book.

```bash
python3 <typst_use>/scripts/typst_doc.py preamble --preset legal --lang da --sec-numbering "1.1" --running-header "Title"
python3 <typst_use>/scripts/typst_doc.py title --doc-type book --title "Title" --subtitle "Subtitle" --author "Author" --date "2026"
python3 <typst_use>/scripts/typst_doc.py outline --title Indhold --depth 2
```

A chapter file is body only.
It starts with a level-1 heading.
Its sections stay in that file.
`main.typ` does not contain chapter prose.

Add a chapter by adding `chapters/03.typ` and one `#include` line in reading order.
A page break after the outline starts the first chapter on a new page.

A chapter that calls labquote starts with `#import "@preview/labquote:0.1.0": *`.
`#setup` stays in `main.typ`.
An include does not inherit an import.

`typst compile main.typ`.
