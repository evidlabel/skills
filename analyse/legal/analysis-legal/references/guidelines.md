# guidelines

Guidance (vejledninger, circulars, authority practice notes): what the authority was meant to do, set against what the record shows it did.

## Get the text

Ingest the guidance so it can be quoted by pass:

    evid --db evid doc add <guidance.pdf|url> -s <slug>
    evid --db evid tag assign <uuid> type:guidance

For a reading copy only: `lawcite other <pdf-url> -f scratch/<short>.md`.

## `legal/guidelines/requirements@1` (basic)

**In scope:** `type:guidance`.

**Instruction:** Extract each requirement or recommendation addressed to an actor in the case.

**note:** `{"requirement": "<slug>", "actor": "authority|caseworker|court|parent|other", "modality": "must|should|may", "applies_when": "<≤15 words>", "confidence": 0.0}`

## `legal/guidelines/compliance@1` (composite)

**Inputs:**
- Required: requirements passes, and the newest `analysis/evidence/timeline/build-*.json`.
- Optional: the proportionality process composite.

**Procedure:** For each requirement that applies to the case, report `evidence_done`, `evidence_not_done`, or `no_record`, with sources.

**Finding:**
```json
{"id": "f1", "claim": "guideline-compliance", "sources": [{"uuid": "…", "pass": "…", "key": "…"}],
 "values": {"requirement": "…", "modality": "must", "status": "evidence_done|evidence_not_done|no_record",
            "record": [{"analysis": "analysis/evidence/timeline/…json", "finding": "f12"}]}}
```

## Done
- Every applicable `must` requirement has a row.
- Requirements judged not to apply are listed in `gaps` with the reason.
