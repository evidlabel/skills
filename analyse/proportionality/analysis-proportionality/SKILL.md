---
name: analysis-proportionality
description: Use when a disputed-facts case held in an evid set involves an intervention in family life (placement, contact restriction, custody change, investigation) and the question is whether it is suitable, necessary, and balanced, whether its stated reasons are supported by the record, and whether parents and child took part in the decision.
---

# analysis-proportionality

Structures the proportionality question for each measure. Evidence for, evidence against, and gaps per limb. No verdict.

## Methods

| Method | Micro-skills | Load |
| --- | --- | --- |
| measures | `proportionality/measures/measures@1` → `…/inventory@1` | `references/measures.md` |
| test | `proportionality/test/alternatives@1` → `…/test@1` | `references/test.md` |
| reasons | `proportionality/reasons/reasons@1` → `…/support@1` | `references/reasons.md` |
| process | `proportionality/process/participation@1` → `…/process@1` | `references/process.md` |

Order: measures first; the others need its inventory.

## Run

1. Check required inputs (listed per method as path patterns). If one is missing, stop: `missing input: <pattern>`.
2. Run basic passes over decisions, proposals, and reports that concern a measure.
3. Run the composite.
4. Report: per measure and limb, evidence for, evidence against, and gaps.

## Rules
- Criteria (what the law requires for each limb) come only from `analysis/legal/law/criteria-*.json` and its Hayagriva keys. Never state a legal test from memory.
- No output field says a measure is or isn't proportionate.

## Conventions

**Commands.** Every evid command is `evid --db evid …`, run from the case root. Bare `evid` writes to `~/.local/share/evid` and never joins the case.

**Where a document lives.** `evid/sets/<slug>/docs/<uuid>/`: `info.yml` (metadata; `dates` is the document date), the source PDF, `label.typ` (ingested text), `machine.hayagriva` (verbatim machine quotes), `machine/` (pass ledger). `text.txt` appears after the first pass; its character offsets are the ones evid records.

**Micro-skill ID.** `<domain>/<method>/<micro>@<version>`, for example `language/contradiction/claims@1`. The ID starts every pass `job` and every composite `step`, so outputs can be found by prefix.

**Basic pass (one document, one micro-skill).**
1. Read the document text (`label.typ`, or `text.txt` if present). Read existing passes first: `evid --db evid doc passes -s <slug> -u <uuid> -f json`. Don't repeat a micro-skill version that already ran unless asked.
2. Write a candidate file as a **new file**: `evid/sets/<slug>/docs/<uuid>/machine/from-<YYYY-MM-DDTHH-MM-SSZ>-<micro>.json`
   ```json
   {
     "job": "<micro-skill ID> — <one-line instruction>",
     "model": "<model id>",
     "quotes": [
       {"candidate": "<span copied from this document, one page>",
        "note": "<compact JSON: the micro-skill's label object>"}
     ]
   }
   ```
   `candidate` is a span from this document only, within one page. `note` carries the labels as a JSON string; its fields are defined by the micro-skill.
3. Run `evid --db evid doc quote -s <slug> -u <uuid> --from <candidate file> --model <model id> --job "<micro-skill ID> — <instruction>"`.
4. Read the printed results. `matched: false` means the span wasn't found verbatim: send a corrected page-local span in a new pass, or drop it. A standalone page number in a matched quote means the span crossed a page break: redo it as a page-local span.

evid records the pass at `machine/<YYYY-MM-DDTHH-MM-SSZ>_<hex>.json` (`job`, `model`, `timestamp`, `quotes[]` with each `note`, `results[]` with `key`, `page`, `score`, `matched`). The verbatim text and its offsets are in `machine.hayagriva` under the same key (`serial-number: "chars <start>-<end>"`, `page-range`). A finding is `(uuid, pass id, key)`; join `quotes[i].note` to `results[i].key` by position. The same span can be matched by several passes and so carry several keys; treat keys with the same `serial-number` as one span.

**Composite step (many inputs).** Write one new JSON file per run: `analysis/<domain>/<method>/<step>-<YYYYMMDDTHHMMSSZ>.json`. Never edit an earlier run; the newest file for a step is current.
```json
{
  "schema": 1,
  "step": "<micro-skill ID>",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ",
  "model": "<model id>",
  "set": "<slug>",
  "inputs": ["evid/sets/<slug>/docs/<uuid>/machine/<pass>.json", "analysis/<...>.json"],
  "inputs_unreviewed": ["<uuid>"],
  "findings": [
    {
      "id": "f1",
      "claim": "<structured label, not prose>",
      "sources": [{"uuid": "<uuid>", "pass": "<pass id>", "key": "<xxxx:qN>", "page": 1}],
      "values": {}
    }
  ],
  "gaps": ["<what is missing and which input pattern would supply it>"]
}
```
Method-specific top-level fields (e.g. `topic_map`) are allowed. Every finding has at least one source that resolves to a key in some `machine.hayagriva`, or to a finding id in an input composite (`{"analysis": "<file>", "finding": "f3"}`), or, for a finding about a whole document, to `{"uuid": "<uuid>"}`, or to an entry in a Hayagriva file in the case (`{"hayagriva": "refs/<file>.yaml", "key": "<key>"}`).

**Inputs missing.** If a required input pattern has no match, stop and report `missing input: <pattern>`. Don't substitute your own reading for a missing pass.

**Unreviewed documents.** evid stores a bare tag as `<slug>.<name>`. `evid --db evid tag assign <uuid> unreviewed` writes `<slug>.unreviewed`. List them with `evid --db evid tag show <slug>.unreviewed -s <slug> -f json`. List their UUIDs in `inputs_unreviewed`, and say so in the report.

**Neutral by construction.**
- Run a micro-skill over every party's documents, not one side's.
- Label statements and documents, never people. No clinical or character terms for persons.
- No single score for a person. Report factors per statement and topic.
- Findings are not conclusions. Weighing belongs to authoring and to the decision-maker.
- Refer to persons by their de-identification tokens (`#(P1V1)`); keep tokens verbatim.

**Scratch and Git.** Drafts, topic lists in progress, and rejected candidate files go in `scratch/` (ignored by Git). Commit `analysis/` and new `machine/` files with each finished step. Identity maps and credentials never enter Git.

## Done
- Every measure is covered by every method that was run.
- Every limb cites evidence or lists a gap.
- `analysis/` and new `machine/` files are committed.
