# law

## Get the text

    lawcite law <name|year/number> -p <paragraphs> -f refs/law-<short>.yaml

Always pass `-f`. `.yaml` is Hayagriva with one key per provision. Check one provision against retsinformation.dk.

## `legal/law/criteria@1` (composite)

**Inputs:** `refs/law-*.yaml` (required).

**Procedure:** Split each provision in scope into its conditions (criteria) and its legal consequence. One finding per criterion. Keep the statute's own wording for the criterion text by pointing to its key. Paraphrase only in `label`.

**Finding:**
```json
{"id": "c1", "claim": "criterion", "sources": [{"hayagriva": "refs/law-<short>.yaml", "key": "<key>"}],
 "values": {"label": "<≤12 words>", "role": "condition|consequence|exception", "limb": "suitability|necessity|balance|null",
            "provision": "<§ and stk. as written>"}}
```
Set `limb` only when the provision states a proportionality requirement.

## `legal/law/fit@1` (composite)

**Inputs:**
- Required: the newest `analysis/legal/law/criteria-*.json`.
- At least one fact composite in `analysis/evidence/`, `analysis/language/`, or `analysis/credibility/`.

**Procedure:** For each criterion, list the fact findings that bear on it, split into evidence for and evidence against, plus gaps.

**Finding:**
```json
{"id": "f1", "claim": "criterion-fit", "sources": [{"analysis": "analysis/legal/law/…json", "finding": "c1"}],
 "values": {"criterion": "c1", "evidence_for": [{"analysis": "…", "finding": "…"}], "evidence_against": [], "gaps": ["…"]}}
```

## Done
- Every provision in scope has at least one criterion.
- Every criterion has a fit row.
