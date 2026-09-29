# skills

Agent Skills for Typst documents built from an evid set. Format: [Agent Skills](https://agentskills.io/specification).

The directory tree is the workflow. A path says what that step is for. A skill folder keeps the skill `name`, with `SKILL.md` plus optional `scripts/` and `references/` beside it.

```
ingest/     bring a source in
process/    change a document before a model sees it
analyse/    read an evid set
author/     shape a document and argue from it
```

| Skill | Where | What it does |
|-------|-------|----------------|
| [`labquote`](analyse/keys-only-typst/labquote/SKILL.md) | `analyse/keys-only-typst/` | Gather (`evid set gather` → `refs.yml`) and render verbatim quotes in a keys-only Typst document. |
| [`typst_use`](author/page-type-title/typst_use/SKILL.md) | `author/page-type-title/` | Page, type, and title block for a Typst document. |
| [`memo`](author/dated-arguing-memo/memo/SKILL.md) | `author/dated-arguing-memo/` | Dated memo that answers one question from verbatim quotes. |
| [`analysis-language`](analyse/language/analysis-language/SKILL.md) | `analyse/language/` | Contradiction, evasiveness, manipulation, and attribution. |
| [`analysis-evidence`](analyse/evidence/analysis-evidence/SKILL.md) | `analyse/evidence/` | Inventory, timeline, interviews, and corroboration. |
| [`analysis-credibility`](analyse/credibility/analysis-credibility/SKILL.md) | `analyse/credibility/` | Reliability factors per statement and topic. No score for a person. |
| [`analysis-proportionality`](analyse/proportionality/analysis-proportionality/SKILL.md) | `analyse/proportionality/` | Measure-by-measure test: suitability, necessity, balance, reasons, and process. |
| [`analysis-legal`](analyse/legal/analysis-legal/SKILL.md) | `analyse/legal/` | Statute criteria, guidance compliance, and judgment analogues. |

`ingest/` and `process/` name the leaves that live in other repos. The file there is the raw URL of that skill:

| Path | Leaf |
|------|------|
| `ingest/council-of-europe-download/hudoc` | HUDOC |
| `ingest/danish-verdicts/domdb` | Domsdatabasen |
| `ingest/danish-statutes/lawcite` | Danish statutes |
| `process/de-identify/did` | de-identify |

evid is the spine through every stage. Its skill stays in the evid repo. The router names it.

Router: [`SKILL.md`](SKILL.md) at the repo root (name `jura`). [`jura/SKILL.md`](jura/SKILL.md) points at it, so the directory name matches the skill name. jura.sh links to the root file.

## Install

Point `[skills].paths` at the skill folders:

```toml
[skills]
paths = [
  "~/projects/jura/skills/jura",
  "~/projects/jura/skills/analyse/keys-only-typst/labquote",
  "~/projects/jura/skills/author/page-type-title/typst_use",
  "~/projects/jura/skills/author/dated-arguing-memo/memo",
  "~/projects/jura/skills/analyse/language/analysis-language",
  "~/projects/jura/skills/analyse/evidence/analysis-evidence",
  "~/projects/jura/skills/analyse/credibility/analysis-credibility",
  "~/projects/jura/skills/analyse/proportionality/analysis-proportionality",
  "~/projects/jura/skills/analyse/legal/analysis-legal",
]
```

Or symlink each folder into the user skill dir (directory name = skill name):

```bash
for d in jura analyse/keys-only-typst/labquote author/page-type-title/typst_use author/dated-arguing-memo/memo analyse/language/analysis-language analyse/evidence/analysis-evidence analyse/credibility/analysis-credibility analyse/proportionality/analysis-proportionality analyse/legal/analysis-legal; do
  ln -sfn "$PWD/$d" ~/.claude/skills/$(basename "$d")
  ln -sfn "$PWD/$d" ~/.grok/skills/$(basename "$d")
done
```

`typst` on `$PATH`. Package `@preview/labquote:0.1.0` is fetched on first compile, or install locally from [evidlabel/labquote](https://github.com/evidlabel/labquote) via `./local_install.sh`.
