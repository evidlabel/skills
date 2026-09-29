## Keys
- `<doc>:<slug>` — first colon groups sources (`0157:tale`)
- `<doc>:main` — document metadata (title, author, date, url). Bibliography parent; `#cite-ref` of the work. Not a quote body
- `#blockq` / `#q` / `#inlineq` take a quote slug (`:q1`, `:tale`). Quote `title:` is the passage. Missing slug → `doc quote`, gather again
- quote body in **`title:`** (not `note:`)
- `d1, d2, …` / `q1, q2, …` assigned in order of first appearance — never hand-assign
- no colon → `<key>:main` (metadata only, bare `[d]`)
- flat keys (`slug_q1`) or quotes in `note:` will not group

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
