---
name: labquote
description: Use when the user wants to render quotes, block quotes, bare cites, legal `Id.` back-references, or a grouped bibliography in a Typst document driven from a namespaced Hayagriva YAML file (as produced by `evid set gather`). Triggers on "set up labquote", "block quote in Typst", "cite this snippet", "render my refs.yml as quotes", "keys-only Typst", "inline quote with superscript", "legal Id. back-reference", "grouped quote bibliography", "#blockq", "#inlineq", "#cite-ref", "labquote bibliography", or building a citable Typst document from labelled evidence.
license: MIT
compatibility: Requires typst on PATH. Package @preview/labquote:0.1.0. refs_to_typ.py needs PyYAML.
---

# labquote

Typst package: verbatim quotes from namespaced Hayagriva YAML. Gather fills `refs.yml`; this typesets `title:`. The `.typ` holds keys. Quote text stays in `refs.yml` until compile.

## Prior
- verbatim → **citing** — never write quote text into `refs.yml` or the `.typ`
- `# generated-by:` comments pass through
- source: <https://github.com/evidlabel/labquote> — `#import "@preview/labquote:0.1.0": *`. `typst` on `$PATH`; first compile fetches `@preview`. Scaffold: `typst init @preview/labquote:0.1.0 my-doc`. Dev: clone + `./local_install.sh install`. Syntax: `template/main.typ`
- styles of this document → **memo** (argues) · **notat** (citatsamling) · **rebut** (line-by-line) · **walkthrough** (graphs). Open one only when that is the form

## Gather
Local `./evid` from the first command (`evid -d ./evid` / `evid --db evid`). Global db is discovery only. No `./evid` beside the `.typ` ⇒ broken.

1. Label: `evid doc quote` / `#lab`. Print keys only. Quote every source the `.typ` will exhibit, before gather
2. `evid -d ./evid set gather <slug> -o /tmp/gather.yml` — keys; quote bodies in `title:`
3. Subset `refs.yml`: every cited key plus that doc's `:main`. Copy entries verbatim, watermarks included. Quote slugs carry `author:` and `date:` from that doc's `:main` (block headers read the quote entry). Later keys from a fresh gather
4. `:main` `url:` comes from the doc `info.yml`. Empty after a local PDF add → write the source URL into `info.yml`, then gather
5. Skeleton from gather (do not hand-write keys):

```bash
python3 <skill-dir>/scripts/refs_to_typ.py refs.yml -o main.typ --write-refs
```

`--font` / `--cite-style` / `--lang` as needed. Then open the style (**memo** / **notat** / **rebut** / **walkthrough**) around the generated `#blockq` lines. Do not replace those keys. Do not switch to markdown `>`.
6. `typst compile main.typ`. Failed anchor throws

Standing collection (`litc`) is discovery: `evid set gather litc -o /tmp/litc.yml`, `grep -niE "title:.*<phrase>"`, copy `docs/<uuid>` into `./evid/sets/<slug>/docs/` (resolve uuid from the 4hex prefix; watch collisions), then gather the local set. Unlabelled quote: `evid -d ./evid doc label|quote`. Outside evid: precise-quoter `--labquote` into `docs/`

`title:` is sacred — slice with `start:`/`end:`, never edit the body. `:main` title may be cleaned (filename slug → readable) as a string replace.

Missing from `refs.yml` → citing tool for that type. No tool → name the gap, offer to build, stop. Never invent YAML (no stub `title:` that is a heading or paragraph number). Package template keys (`0157:tale`) are syntax illustration — keys in the `.typ` are gather keys.

`bibliography-custom()` renders **every** store entry — unsubsetted dump = whole dataset on the back page.

## Keys
- `<doc>:<slug>` — first colon groups sources (`0157:tale`)
- `<doc>:main` — document metadata (title, author, date, url). Bibliography parent; `#cite-ref` of the work. Not a quote body
- `#blockq` / `#q` / `#inlineq` take a quote slug (`:q1`, `:tale`). Quote `title:` is the passage. Missing slug → `doc quote`, gather again
- quote body in **`title:`** (not `note:`)
- `d1, d2, …` / `q1, q2, …` assigned in order of first appearance — never hand-assign
- no colon → `<key>:main` (metadata only, bare `[d]`)
- flat keys (`slug_q1`) or quotes in `note:` will not group — precise-quoter `--labquote`

## API

| Fn | Job |
|---|---|
| `setup(data, blockquote-indent: 1em, cite-style: "full")` | once, near top. `"full"` `[d1, q2]` · `"brief"` `[d1,2]` · `"short"` `[1b]`. Legacy `cite-brief: true` = `"brief"` |
| `multicite(keys)` | one bracket around a list |
| `setup-bib(src, …)` | biblatex string instead |
| `q(key, ..)` | inline quote trailing `[d, q]`; slice `start:`/`end:`/`pin:` |
| `inlineq(key, .., mark: …)` | in-sentence; attribution as one clickable superscript. `mark:` token or array (`"quote"` default · `"brace"` · `"plain"` + `"italic"` `"underline"` `"color"` `"ellipsis"`) |
| `blockq(key, ..)` | block quote + header |
| `cite-ref(key, pin: …)` | bare `[d, q]`, no body |
| `id(pin: …)` | legal `Id.` — last cite |
| `bibliography-custom(brief: false, title: auto)` | grouped back page; slice italicised. Heading from `text.lang` (da → "Referencer") |

`start:`/`end:` = verbatim substrings. Gather generously; slice tightly. Back page reprints the whole entry with the slice italicised.

Page font is Typst `#set text(font: "…")`, not a `setup()` argument.

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

## Integration
- **evid** — ingest, label, `set gather`
- **precise-quoter** — `--labquote`
- **lawcite** — `law … --file refs.yaml` same colon contract
- **hudoc** — ingest only
- styles: **memo** · **notat** · **rebut** · **walkthrough**
- **output-table** last

Relative `#import` in shipped docs → `@preview/labquote:0.1.0`.
