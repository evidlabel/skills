---
name: plain
description: >
  Use when the user wants a Typst document with a centered title and an
  optional date, and no other chrome. Not a memo, brief, letter, booklet, or book.
license: MIT
compatibility: Requires typst on PATH. The title block comes from typst_use.
---

# plain

One file. The title block is a centered title and an optional date.

```bash
python3 <typst_use>/scripts/typst_doc.py title --doc-type plain --title "…" --date "…"
```

The body follows the title. Page and type come from typst_use `preamble`, written inline in the same file. A set of quotes is `quote_summary`.
