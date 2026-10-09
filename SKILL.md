---
name: jura
description: |
  Use for social-legal work where the facts are contested.
  Run tree in this repo and open one leaf.
  The leaf page is index.md.
  The directories are the workflow: ingestion, processing, analysis, authoring.
---

# jura

Run this from the repo root.
Read the output.
That is the workflow.
Open one leaf.
Read `index.md` there.
If the leaf has no `index.md`, read `SKILL.md`.

This file is the skill for the tree.
`labquote` and `memo` keep `SKILL.md` because each is installed alone.
A folder that only holds other folders is the path to a leaf.

```bash
tree --gitignore --dirsfirst -I '.git|.gitkeep' ingestion
tree --gitignore --dirsfirst -I '.git|.gitkeep' processing
tree --gitignore --dirsfirst -I '.git|.gitkeep' analysis
tree --gitignore --dirsfirst -I '.git|.gitkeep' authoring
```

**ingestion** brings a source in.
**processing** changes a document before a model sees it.
**analysis** reads the evid set.
**authoring** shapes a document and argues from it.
A gap in authoring goes back to ingestion.

**setup** is the harness.
Open `setup/harness`.

## Rules

- **PII stays local.**
  The local agent holds the source.
  A remote model gets only the stripped handoff.
  If this session is not local, track back.
- **The set persists.**
  From the case root, `evid --db evid`.
  Bare `evid` writes `~/.local/share/evid`.
  A document's UUID stays.
  Deleting one is not a step.
- **Passes add on.**
  A new file each time.
  A pass is one document.
  A composite is many passes, at `analysis/<domain>/<method>/` in the case.
  Newest for a step is current.
  Missing input: stop and name the pattern.
- **Quotes are clipped from the source, never paraphrased.**
  Statute, judgment, and guidance the same way.
  No span and no key: it is a gap.
  The text in force is the text on the date of the act.
  A later revision is a different document.
  A statute that is not yet paragraph-level is lawcite.
- **Label statements, not people.**
  Every party.
  No score for a person.
  No conclusion.
  Weighing is authoring.
- **Keys and credentials stay out of Git.**
  `scratch/` is disposable.

Flags from the leaf you opened: `-h`, `-j`.
