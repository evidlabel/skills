---
name: labquote
description: Use when the user wants to render quotes, block quotes, bare cites, legal `Id.` back-references, or a grouped bibliography in a Typst document driven from a namespaced Hayagriva YAML file (as produced by `evid set gather`). Triggers on "set up labquote", "block quote in Typst", "cite this snippet", "render my refs.yml as quotes", "keys-only Typst", "inline quote with superscript", "legal Id. back-reference", "grouped quote bibliography", "#blockq", "#inlineq", "#cite-ref", "labquote bibliography", or building a citable Typst document from labelled evidence.
license: MIT
compatibility: Requires typst on PATH. Package @preview/labquote:0.1.0. refs_to_typ.py needs PyYAML.
---

# labquote

Typst package: verbatim quotes from namespaced Hayagriva YAML. Gather fills `refs.yml`; this typesets `title:`. The `.typ` holds keys. Quote text stays in `refs.yml` until compile.

## Prior
- never write quote text into `refs.yml` or the `.typ`
- `# generated-by:` comments pass through
- source: <https://github.com/evidlabel/labquote> — `#import "@preview/labquote:0.1.0": *`. `typst` on `$PATH`; first compile fetches `@preview`. Scaffold: `typst init @preview/labquote:0.1.0 my-doc`. Dev: clone + `./local_install.sh install`. Syntax: `template/main.typ`

## Gather
Every evid command runs as `evid --db evid` from the case root. `scratch/` is ephemeral and in `.gitignore`.

1. Label: `evid --db evid doc quote` / `#lab`. Print keys only. Quote every source the `.typ` will exhibit, before gather
2. `evid --db evid set gather <slug> -o scratch/gather.yml` — keys; quote bodies in `title:`
3. Subset `refs.yml`: every cited key plus that doc's `:main`. Copy entries verbatim, watermarks included. Quote slugs carry `author:` and `date:` from that doc's `:main` (block headers read the quote entry). Later keys from a fresh gather
4. `:main` `url:` comes from the doc `info.yml`. Empty after a local PDF add → write the source URL into `info.yml`, then gather
5. Skeleton from gather (do not hand-write keys):

```bash
python3 <skill-dir>/scripts/refs_to_typ.py refs.yml -o main.typ --write-refs
```

`--font` / `--cite-style` / `--lang` as needed. Then write around the generated `#blockq` lines. Do not replace those keys. Do not switch to markdown `>`.
6. `typst compile main.typ`. Failed anchor throws

Shared db, read-only discovery: `evid set gather litc -o scratch/litc.yml`. This is the only bare `evid` allowed; copy what you need into `evid/sets/<slug>/docs/` and gather the local set.

`title:` is sacred — slice with `start:`/`end:`, never edit the body. `:main` title may be cleaned (filename slug → readable) as a string replace.

Missing from `refs.yml` → name the gap and stop. Never invent YAML (no stub `title:` that is a heading or paragraph number). Package template keys (`0157:tale`) are syntax illustration — keys in the `.typ` are gather keys.

`bibliography-custom()` renders **every** store entry — unsubsetted dump = whole dataset on the back page.

Keys and API: `references/api.md`.

```typst
#import "@preview/labquote:0.1.0": *
#set text(font: "…")
#setup(yaml("refs.yml"), blockquote-indent: 1em)

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
