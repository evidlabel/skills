---
name: jura
description: Use for social-legal work (family law and similar) where the facts are contested and the law is mostly settled. Routes ingestion, processing, analysis, and authoring across evid, did, hudoc, domdb, lawcite, labquote, typst_use, and memo. Map only; open one leaf per job.
---

# jura

Map only. Pick one row, then open that leaf. One leaf per job. Sibling leaves stay closed. This file is the only place that maps needs to leaves; leaves do not point at each other or back here.

jura is for social-legal work: family law and disputes like it, where the evidence matters much more than the law. In these cases people usually disagree about what happened, not about what the rule says. The law is mostly settled and the facts are contested, so the toolset is built to establish facts, not to cite statutes. Domain knowledge (family law, child welfare, and so on) lives in the leaf instructions, not in this tree.

Flags live in each tool (` -h` / ` -j`). This file does not cache them.

## Two layers

1. **The evid database is the corpus.** It is append-only and nothing expires. Every piece of evidence ever ingested stays. Value compounds over time, because a new case can search years of prior matters.
2. **The case file holds the authored artifacts.** They reference the corpus through Hayagriva exports that carry provenance (UUID, URL, author, year).

A case folder looks like this:

```
<case>/
├── evid/        corpus db for this case (evid --db evid)
├── analysis/    composite analysis JSON (case-local)
├── scratch/     ephemeral working files (not versioned)
└── <authored>   memos, briefs, reports, filings (PDF + source)
```

## Four stages, evid as spine

```
ingestion ──► processing ──► analysis ──► authoring
    ▲                                         │
    └──────────── gaps found in authoring ────┘
```

| Stage | What it covers | evid's role |
| --- | --- | --- |
| Ingestion | Everything entering the corpus: PDFs, correspondence, medical reports, court records, internet material, and material from the prior corpus. | `doc add` |
| Processing | Changing the evidence: de-identifying, labeling, structuring. did cleans documents before evid sees them. | `doc quote` (passes), `#lab` |
| Analysis | Reading the evidence without changing it. It is flexible, not a fixed workflow. There are two tiers, basic and composite. | `search text` / `search vec`, `doc passes` |
| Authoring | Memos, briefs, reports, court filings. Competing angles are expected. | `set gather` → Hayagriva YAML |

evid runs through every stage. Every other leaf feeds into it or reads from it. That is why `evid --db evid` is load-bearing for the whole tree.

The stages are not one-way. When authoring surfaces a gap (a filing needs a fact that has not been sourced yet), go back to ingestion. Get the source, process it, and analyze it again before the filing uses it.

## Hard rules

1. **Always `evid --db evid`.** Never run bare `evid`: it writes to `~/.local/share/evid`, and that set never joins the case. Use the home db only when the user asks for the shared database in so many words.
2. **Set creation.** The first evid call in a case is `evid --db evid set create --dataset <slug>`. Without `--dataset`, the command waits for a typed name. Confirm that `evid/sets/<slug>/` exists in the working directory before reporting the set as created. If a call ran without the flag, re-run it with the flag.
3. **Track the case in Git.** Run `git status` and initialize a repository if none exists. Preserve changes that were already there. Stage only the files created or changed by the current job. Review `git diff`, then commit each coherent milestone with a short description. Report whatever working-tree state remains.
4. **Keep secrets out of Git.** Identity maps, credentials, API keys, and excluded sensitive originals never enter the repo. Add them to `.gitignore` before the first commit. `scratch/` is also ignored.
5. **Install only the tool you opened.**
6. **UUIDs are immutable.** A UUID is a document's identity, not its content. Re-labeling a document or running new passes changes metadata, not identity, so citations still resolve. A document that is genuinely re-ingested as a different file gets a new UUID, because it is a different document.
7. **Deleting a UUID is a rare manual act, never a workflow step.** Never delete one as part of normal work. If you do delete one, search every Hayagriva YAML in the case for that UUID and strip each use.
8. **did review is never skipped silently.** Review uses a local model when one is available (a light model is enough) or a human. If neither is available, did still runs and the output is flagged as unreviewed, so the corpus records the gap. Running did with some leaks is better than not running it at all.
9. **Analysis is local to a case.** There is no shared analysis layer across the corpus. To reuse work from another case, import its composite JSON into this case's `analysis/`, where it becomes a native artifact with its own provenance. Anything borrowed is re-ingested, not referenced.
10. **The scratchpad is disposable.** Composing, condensing, pruning, and trying argument lines all happen in `scratch/`. Don't version the scratchpad, and don't keep failed argument lines as artifacts. Only final authored output earns a place in the case file.
11. **Stages loop.** Gaps found in authoring go back to ingestion.
12. **Verify against the source.** Every quote and every finding must trace back to verbatim text in an ingested document.

## Processing: did

did pseudonymizes a document before evid or any hosted model sees it. did does most of the work. The review step only checks for leaks and for wrongly merged identities.

- **Local model available:** the model reviews did's output and acts as a gate on the ingestion pipeline.
- **No model:** a human reviews. This fallback is perfectly fine.
- **No model and no human:** did runs, and the output is marked unreviewed.

Identity maps stay out of Git (rule 4).

## Analysis

### Structure: domain → method → micro-skill

- A **domain** is an area of practice, such as family law.
- A **method** is a way of reading evidence, such as comparing stated with demonstrated behavior.
- A **micro-skill** is one narrow extraction. It belongs to exactly one domain and one method.

Micro-skills compose. For example, a parental alienation brief is a chain of micro-skills, and each one produces a pass. Micro-skill output is structured (labels, quotes, confidence), never prose, because structured output can be aggregated across a corpus.

For example, take the method of comparing stated with demonstrated collaboration:

- The **stated collaboration** micro-skill catches claims of virtue ("I always put the child first").
- The **demonstrated collaboration** micro-skill catches actions: whether the parent attended the meeting, responded, and followed the schedule.
- The composite step compares the two, and that comparison is the analysis. High stated collaboration with low demonstrated collaboration is the virtue-signaling pattern.

### Two tiers

| Tier | Reads | Writes | Lives |
| --- | --- | --- | --- |
| Basic (pass) | One document, one instruction | JSON sidecar | Beside the document in `evid/` (`machine/`) |
| Composite | Many sidecars across documents | JSON file | `analysis/` in the case |

### Pass sidecar (basic)

A pass is the extraction, not the analysis. It is a JSON sidecar attached to one document, and it records:

- when the pass ran (timestamp);
- which model ran it;
- what it looked for (the instruction, as a string);
- its findings, each with start and end offsets into the document's verbatim text, so the finding can be extracted exactly.

Read the document's existing passes (`evid --db evid doc passes`) before running another. The evid leaf defines the file naming.

### Composite JSON

A composite result cannot be attached to a single document, so it lives in `analysis/`:

```json
{
  "step": "stated-vs-demonstrated-collaboration",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ",
  "model": "<model id>",
  "inputs": ["<uuid>/machine/<pass>.json", "..."],
  "findings": [
    {
      "claim": "<structured label>",
      "sources": [
        {"pass": "<uuid>/machine/<pass>.json", "start": 0, "end": 0}
      ],
      "values": {"stated": 0.0, "demonstrated": 0.0, "gap": 0.0}
    }
  ]
}
```

The citation chain makes the result auditable. Any finding traces back through the composite and the pass to the original verbatim text. Because the result is a file rather than a chat session, it persists and can be re-run when a new pass lands.

## Case file

- **Provenance comes from the export.** `evid --db evid set gather` writes Hayagriva YAML that already carries the UUID, URL, author, and year. Do not add provenance metadata to authored documents.
- **Authored artifacts are immutable snapshots.** Each carries its own date or timestamp. Changing labels inside a document does not change its UUID. A snapshot is simply a snapshot, so staleness needs no tracking.
- **Competing angles are expected.** Author each angle as a finished PDF so the angles can be reviewed side by side. Whoever reviews them (a human or an agent) decides which angle wins. The router stays neutral.

## Map

| Need | Stage | Tool | Open | Next |
| --- | --- | --- | --- | --- |
| Corpus: ingest, pass, label, search, gather | all (spine) | `evid` | https://raw.githubusercontent.com/evidlabel/evid/master/SKILL.md | The row for the stage in hand |
| De-identify before a model sees the file | processing | `did` | https://raw.githubusercontent.com/evidlabel/did/main/SKILL.md | `evid --db evid doc add <out>/anon/` |
| HUDOC / Council of Europe download | ingestion | `hudoc` | https://raw.githubusercontent.com/evidlabel/hudoc/master/SKILL.md | `evid --db evid doc list -s <slug>` after import |
| Danish verdicts (Domsdatabasen) | ingestion | `domdb` | https://raw.githubusercontent.com/evidlabel/domdb/master/SKILL.md | `evid --db evid doc list -s <slug>` after import |
| Danish statutes as paragraph cites | ingestion | `lawcite` | https://raw.githubusercontent.com/evidlabel/lawcite/master/SKILL.md | Hayagriva `.yaml` beside the case's `refs.yml` |
| Keys-only Typst from an evid set | analysis | `labquote` | analyse/keys-only-typst/labquote/SKILL.md | memo, or a composite step in `analysis/` |
| Page, type, and title block | authoring | `typst_use` | author/page-type-title/typst_use/SKILL.md | the authored document |
| Dated arguing memo | authoring | `memo` | author/dated-arguing-memo/memo/SKILL.md | PDF snapshot in the case file; go back to ingestion for any gap |

## Install the picked tool

```bash
uv tool install "evid @ git+https://github.com/evidlabel/evid.git"
uv tool install "did[models] @ git+https://github.com/evidlabel/did.git"
uv tool install git+https://github.com/evidlabel/hudoc.git
uv tool install git+https://github.com/evidlabel/lawcite.git
uv tool install git+https://github.com/evidlabel/domdb.git
```

labquote, typst_use, and memo are skills in this repo, under `analyse/` and `author/`. They need `typst` on PATH, and the `@preview/labquote` package is fetched on first compile.

Install only the one you opened. evid's label and gather commands need `typst` on PATH. did needs a desktop for its GUI, and a local model if the review should be automated. domdb needs Domsdatabasen API credentials, which stay out of Git.

## Done

- A leaf is open, or the user has the install command for the row they picked.
- Wherever evid ran, `evid/sets/` exists in the working directory.
- Any did output that was not reviewed is flagged as unreviewed.
- Composite results are in `analysis/`, and only final authored output is in the case file.
- The job's changes are in a scoped commit, and the remaining working-tree state has been reported.
- Every output has been checked against the original source.
