---
name: labquote
description: Use when the user wants a keys-only Typst document of verbatim quotes from Hayagriva YAML (`refs.yml`, as from `evid set gather`), including block quotes, inline quotes, bare cites, legal `Id.` back-references, or a grouped bibliography. Triggers on "set up labquote", "render refs.yml as quotes", "#blockq", "#inlineq", "#cite-ref".
license: MIT
compatibility: Requires typst on PATH. Package @preview/labquote:0.1.0. refs_to_typ.py needs PyYAML.
---

# labquote

Quote text lives in `refs.yml`. The `.typ` holds keys. Compile typesets each entry's `title:`.

## Package

`#import "@preview/labquote:0.1.0": *`. First `typst compile` fetches `@preview`.

Read the package for commands, cite styles, and key shape — not this file:

- scaffold: `typst init @preview/labquote:0.1.0 my-doc` → `template/main.typ`
- after fetch: `~/.cache/typst/packages/preview/labquote/` — `README.md`, `lib.typ`
- source: https://github.com/evidlabel/labquote

## Document

1. Put a Hayagriva `refs.yml` next to the `.typ`. Typical producer: `evid set gather` (flags from `evid -h`). Copy entries as they are, comments included. Do not invent keys. Do not rewrite quote `title:` — narrow with `start:`/`end:` in the `.typ`. A `:main` document title may be cleaned as a string replace.
2. Subset to the keys this document cites, plus each of those docs' `:main`. Keys in the `.typ` come from this `refs.yml`, not from the package template. Skeleton:

```bash
python3 <skill-dir>/scripts/refs_to_typ.py -h
python3 <skill-dir>/scripts/refs_to_typ.py refs.yml -o main.typ --write-refs
```

3. Keep the generated keys. Write around them.
4. `typst compile main.typ`. A missing key or a slice that is not in `title:` fails the compile.

Arguing memo: sibling **memo**.
