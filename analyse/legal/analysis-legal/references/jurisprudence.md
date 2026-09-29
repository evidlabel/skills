# jurisprudence

Judgments compared with the case by their decisive factors.

## Get the judgments

Danish verdicts (Domsdatabasen). Find cases with `domdb` (flags: `domdb -h`, `domdb -j`), then:

```bash
domdb -d <cache> output j2e …                 # flags per `domdb output j2e -h`
cp -r <j2e_out>/<uuid> evid/sets/<slug>/docs/
evid --db evid doc list -s <slug>             # confirm
```

ECtHR and other Council of Europe documents:

```bash
hudoc download <feed.xml> -o hudoc_out            # per-doc <uuid>/label.typ + info.yml
cp -r hudoc_out/<uuid> evid/sets/<slug>/docs/     # copy into the case set
evid --db evid doc list -s <slug>                 # confirm the doc is in the set
```

Then tag each judgment: `evid --db evid tag assign <uuid> type:judgment`.

## `legal/jurisprudence/holdings@1` (basic)

**In scope:** `type:judgment`.

**Instruction:** Extract and label the parts of the judgment that carry its reasoning.

**note:** `{"part": "facts|rule|application|outcome|decisive-factor", "topic": "<slug>", "factor": "<slug>|null", "confidence": 0.0}`

Use factor slugs shared with the case's analysis where they fit (e.g. `child-views-recorded`, `less-intrusive-tried`, `contact-maintained`, `risk-documented`).

## `legal/jurisprudence/analogues@1` (composite)

**Inputs:**
- Required: holdings passes.
- Optional: the newest `analysis/legal/law/criteria-*.json`, and fact composites.

**Procedure:** For each judgment, compare its decisive factors with the case's findings. Report:
- `shared`: factors present in both
- `differing`: factors present in one and absent or opposite in the other
- the judgment's `outcome`

Don't rank judgments or predict an outcome.

**Finding:**
```json
{"id": "f1", "claim": "analogue", "sources": [{"uuid": "<judgment uuid>", "pass": "…", "key": "…"}],
 "values": {"judgment": "<uuid>", "outcome": "<≤12 words, keyed>", "shared": ["less-intrusive-tried"],
            "differing": [{"factor": "child-views-recorded", "judgment": true, "case": false}]}}
```

## Done
- Every judgment used has a holdings pass and an analogue row.
- Every outcome cited is keyed.
