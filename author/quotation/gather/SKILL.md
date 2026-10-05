---
name: gather
description: |
  Use when labelled evidence should become a namespaced Hayagriva refs.yml for labquote.
  Triggers on "gather", "refs.yml", "evid set gather", "doc quote", "quote the sources".
  Not typesetting the quotes (labquote).
license: MIT
compatibility: |
  evid on PATH.
  From the case root, every evid command runs as `evid --db evid`.
---

# gather

Gather fills `refs.yml`.
Labquote typesets `title:`.
Quote text stays in the gather output.
The `.typ` holds keys.

Every evid command runs as `evid --db evid` from the case root.
`scratch/` is ephemeral and in `.gitignore`.

1. Label: `evid --db evid doc quote` / `#lab`.
   Print keys only.
   Quote every source the `.typ` will exhibit, before gather
2. `evid --db evid set gather <slug> -o scratch/gather.yml` — keys; quote bodies in `title:`
3. Subset `refs.yml`: every cited key plus that doc's `:main`.
   Copy entries verbatim, watermarks included.
   Quote slugs carry `author:` and `date:` from that doc's `:main` (block headers read the quote entry).
   Later keys from a fresh gather
4. `:main` `url:` comes from the doc `info.yml`.
   Empty after a local PDF add → write the source URL into `info.yml`, then gather

Read-only discovery; the only bare evid call in any skill: `evid set gather litc -o scratch/litc.yml`.
Copy what you need into `evid/sets/<slug>/docs/` and gather the local set.

`title:` is the quote.
`:main` title may be cleaned (filename slug → readable) as a string replace.

A key missing from `refs.yml` is a gap.
Name it and stop.
A stub `title:` (a heading or a paragraph number) is not a quote.
Package template keys (`0157:tale`) are syntax illustration.
Keys in the `.typ` are gather keys.

Then labquote.
