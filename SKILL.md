---
name: jura
description: |
  Use for social-legal work where the facts are contested.
  Run tree in this repo and open one leaf.
  The directories are the workflow: ingest, process, analyse, author.
---

# jura

Run this from the repo root.
Read the output.
That is the workflow.
Open one leaf.

```bash
tree --gitignore --dirsfirst -I '.git|.gitkeep' ingest
tree --gitignore --dirsfirst -I '.git|.gitkeep' process
tree --gitignore --dirsfirst -I '.git|.gitkeep' analyse
tree --gitignore --dirsfirst -I '.git|.gitkeep' author
```

**ingest** brings a source in.
**process** changes a document before a model sees it.
**analyse** reads the evid set.
**author** shapes a document and argues from it.
A gap in authoring goes back to ingest.

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
