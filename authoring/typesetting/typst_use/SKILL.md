---
name: typst_use
description: |
  Use when setting the page, the body text, or a title block in a Typst document: margins, font, language, justification, page numbers, an outline.
  Triggers on "set up the document", "page margins", "A4", "which font", "title block", "letterhead".
  The document is a folder under authoring/templates.
  Not for gathering quotes or writing the argument.
license: MIT
compatibility: Requires typst on PATH.
---

# typst_use

Typst ships with almost no document conventions.
This skill supplies the shell: the page, the body text, the paragraph rules, and a title block.
The document is a folder under `authoring/templates`.
Quotations stay in the Hayagriva file.
The argument is written around those keys.

## Using the script

The script writes a Typst fragment to standard output, or to a file when given `-o`.
Insert the fragment inline into the `.typ` file.
Do not `#include` it: Typst scopes `#set` rules to the included file, so the page and font settings would silently not apply.

```bash
python3 <skill-dir>/scripts/typst_doc.py preamble --preset legal --lang da
python3 <skill-dir>/scripts/typst_doc.py title --doc-type memo --to … --sender … --date … --subject …
python3 <skill-dir>/scripts/typst_doc.py outline --title Contents
```

## Preamble

The preamble sets the text, page, and paragraph defaults:

```bash
python3 <skill-dir>/scripts/typst_doc.py preamble -h
```

There are two base presets:

- `legal` (the default): a wider left margin for binding, and centered page numbers.
- `plain`: a uniform margin and no page numbers.

These flags override the preset:

- `--paper`, `--font`, `--size`, and `--lang` set the body text;
- `--no-justify` leaves paragraphs ragged-right;
- `--page-numbers` and `--no-page-numbers` force page numbering on or off;
- `--sec-numbering "1.1"` numbers section headings, which an outline needs to be useful;
- `--running-header TEXT` adds a small right-aligned header on every page after the first.

The preamble also gives headings a restrained size, so that the title block remains visually dominant.

## Title block

`title --doc-type` prints a title block and nothing else.
The document is the skill under `authoring/templates/` with the same name.
Open that skill for what the document contains and where the block sits.

| `--doc-type` | Template | What the script prints |
|--------------|----------|------------------------|
| `memo` | `authoring/templates/memo` | A To/From/Date/Subject grid under a rule. Flags: `--to`, `--sender`, `--date`, `--subject`. |
| `brief` | `authoring/templates/brief` | A short description on the left and the date on the right, under a hairline. Flags: `--title`, `--date`. |
| `letter` | `authoring/templates/letter` | A right-aligned sender, then the date, the recipient, and a bold Subject. Flags: `--sender`, `--recipient`, `--date`, `--subject`. |
| `book` | `authoring/templates/book` | A title page with title, subtitle, author, and date, followed by a page break. Flags: `--title`, `--subtitle`, `--author`, `--date`. |
| `booklet` | `authoring/templates/booklet` | A compact centered title with subtitle, author, and date. Same flags as `book`. |
| `plain` | `authoring/templates/plain` | A centered bold title with an optional date. Flags: `--title`, `--date`. |

In `--sender` and `--recipient`, the two characters `\n` produce a line break.
A field with no value drops its row, and a block with no fields renders nothing.

## Outline

```bash
python3 <skill-dir>/scripts/typst_doc.py outline --title Contents --depth 2
```

The `outline` command emits `#outline(…)`.
Place it after the title block.
It lists the headings in document order; add `--sec-numbering` to the preamble if you want them numbered.

## Order in the document

```typ
#import "@preview/labquote:0.1.0": *
#set text(…); #set page(…); #set par(…)
#setup(yaml("refs.yml"), …)
…title block…
#blockq("…")
#bibliography-custom()
```
