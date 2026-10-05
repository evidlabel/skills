---
name: letter
description: >
  Use when the user wants a Typst letter: sender, date, recipient, and subject,
  then the letter. Not a memo and not a brief.
license: MIT
compatibility: Requires typst on PATH. The title block comes from typst_use.
---

# letter

One file. The title block is the sender, the date, the recipient, and the subject.

```bash
python3 <typst_use>/scripts/typst_doc.py title --doc-type letter --sender "…" --date "…" --recipient "…" --subject "…"
```

In `--sender` and `--recipient`, `\n` is a line break. The letter follows the subject line. Page and type come from typst_use `preamble`, written inline in the same file.
