---
name: labquote
description: |
  Use when the user wants to render quotes, block quotes, bare cites, legal `Id.` back-references, or a grouped bibliography in a Typst document driven from a namespaced Hayagriva YAML file.
  Triggers on "set up labquote", "block quote in Typst", "cite this snippet", "render my refs.yml as quotes", "keys-only Typst", "inline quote with superscript", "legal Id. back-reference", "grouped quote bibliography", "#blockq", "#inlineq", "#cite-ref", "labquote bibliography", or building a citable Typst document from labelled evidence.
  The YAML comes from gather.
license: MIT
compatibility: |
  Requires typst on PATH.
  Package @preview/labquote:0.1.0.
  refs_to_typ.py needs PyYAML.
---

# labquote

Typst package: verbatim quotes from namespaced Hayagriva YAML.
Gather fills `refs.yml`.
This typesets `title:`.
The `.typ` holds keys.
Quote text stays in `refs.yml` until compile.
Cite style is short unless the document asks for another.

## Prior
- quote text stays in the gather output.
  The `.typ` holds keys
- `# generated-by:` comments pass through
- source: <https://github.com/evidlabel/labquote> — `#import "@preview/labquote:0.1.0": *`.
  `typst` on `$PATH`; first compile fetches `@preview`.
  Scaffold: `typst init @preview/labquote:0.1.0 my-doc`.
  Dev: clone + `./local_install.sh install`.
  Syntax: `template/main.typ`
- cite style defaults to `short` (`[1b]`).
  `full` is `[d1, q2]`.
  `brief` is `[d1,2]`.

## Render
`refs.yml` comes from gather.
If it is missing, stop and use gather.

```bash
python3 <skill-dir>/scripts/refs_to_typ.py refs.yml -o main.typ --write-refs
```

`--cite-style` defaults to `short`.
Then write around the generated `#blockq` lines.
The keys stay as gathered.
A quote stays a `#blockq`.

`typst compile main.typ`.
A failed anchor throws.

`title:` is the quote.
Slice it with `start:` and `end:`.

A key missing from `refs.yml` is a gap.
Name it and stop.
A stub `title:` (a heading or a paragraph number) is not a quote.
Package template keys (`0157:tale`) are syntax illustration.
Keys in the `.typ` are gather keys.

`bibliography-custom()` renders **every** store entry — unsubsetted dump = whole dataset on the back page.

Keys and API: `references/api.md`.

```typst
#import "@preview/labquote:0.1.0": *
#set text(font: "…")
#setup(yaml("refs.yml"), blockquote-indent: 1em, cite-style: "short")

#cite-ref("<gather-key>")
#blockq("<gather-key>", start: "<verbatim>", end: "<verbatim>")
Inline: #q("<gather-key>", pin: "p. 5")
#inlineq("<gather-key>", start: "<verbatim>", end: "<verbatim>", mark: ("brace", "italic"))
#id(pin: "¶ 4")
#bibliography-custom()
```

```bash
typst compile main.typ
```

Relative `#import` in shipped docs → `@preview/labquote:0.1.0`.
