---
name: booklet
description: |
  Use when the user wants a short Typst booklet in one file: a compact title, then the text.
  A book with separate chapter files is book.
license: MIT
compatibility: |
  Requires typst on PATH.
  The title block comes from typst_use.
---

# booklet

One file.
The title block is a compact centered title, with subtitle, author, and date.

```bash
python3 <typst_use>/scripts/typst_doc.py title --doc-type booklet --title "…" --subtitle "…" --author "…" --date "…"
```

The text follows the title in the same file.
Chapters in separate files are `book`.
Page and type come from typst_use `preamble`, written inline.
