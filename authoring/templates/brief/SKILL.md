---
name: brief
description: |
  Use when the user wants a short Typst brief: a description and the date on one line, then the body.
  Not a memo, not a letter, and not a book.
license: MIT
compatibility: |
  Requires typst on PATH.
  The title block comes from typst_use.
---

# brief

One file.
The title block is the description on the left and the date on the right.

```bash
python3 <typst_use>/scripts/typst_doc.py title --doc-type brief --title "…" --date "…"
```

The body follows the hairline.
Page and type come from typst_use `preamble`, written inline in the same file.
