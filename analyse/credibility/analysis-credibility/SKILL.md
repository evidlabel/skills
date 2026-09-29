---
name: analysis-credibility
description: Use when assembling reliability factors for accounts in a disputed-facts case held in an evid set — internal and external consistency, whether stated conduct matches recorded conduct, and how well professional or third-party statements are grounded. Produces factor tables, never a verdict or a score for a person.
---

# analysis-credibility

Factors, per statement and topic, that bear on reliability. Symmetric across parties. No verdicts.

## Methods

| Method | Micro-skills | Load |
| --- | --- | --- |
| consistency | `credibility/consistency/consistency@1` | `references/consistency.md` |
| external consistency | `credibility/external/external@1` | `references/external.md` |
| stated vs demonstrated | `credibility/stated-vs-demonstrated/stated@1`, `…/demonstrated@1` → `…/gap@1` | `references/stated-vs-demonstrated.md` |
| source reliability | `credibility/source-reliability/grounds@1` → `…/reliability@1` | `references/source-reliability.md` |

## Run

1. Check the method's required inputs exist (the method file lists them as path patterns). If one is missing, stop: `missing input: <pattern>`.
2. Run any basic micro-skills as passes over every party's in-scope documents.
3. Run the composite. Produce the same factor rows for every party.
4. Report: factor table per party and topic, sources, gaps, unreviewed inputs.

## Rules
- No overall credibility score, rank, or label for any person.
- Demeanour, tone of voice, and impressions are not factors.
- A factor row is not a conclusion. Weighing is for authoring and the decision-maker.

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
- Every party has rows for the same factors and topics.
- Every row cites composite findings or keys.
- Missing inputs are reported, not worked around.
- `analysis/` and new `machine/` files are committed.
