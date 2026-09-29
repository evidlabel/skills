# measures

## `proportionality/measures/measures@1` (basic)

**In scope:** decisions, proposals, authority reports, and court documents (`type:decision`, `type:professional-report`, `type:judgment`).

**Instruction:** Extract each span that proposes, decides, implements, extends, or ends a measure affecting family life.

**note:**
```json
{"measure": "<slug>", "status": "proposed|decided|implemented|extended|ended", "decided_by": "<role>",
 "date": "YYYY-MM-DD|unknown", "stated_aim": "<≤15 words>", "legal_basis_as_written": "<as written>|null",
 "duration": "<as written>|null", "confidence": 0.0}
```
Measure slugs: `out-of-home-placement`, `supervised-contact`, `contact-suspension`, `contact-reduction`, `custody-transfer`, `residence-change`, `investigation`, `support-measure`, `other`.

## `proportionality/measures/inventory@1` (composite)

**Inputs:** measures passes (required).

**Procedure:** Merge the passes into one entry per measure, holding its lifecycle (the status changes, with dates) and all its sources.

**Finding:**
```json
{"id": "m1", "claim": "measure", "sources": [{"uuid": "…", "pass": "…", "key": "…"}],
 "values": {"measure": "supervised-contact", "lifecycle": [{"status": "decided", "date": "2026-04-02", "decided_by": "<role>"}],
            "stated_aim": "…", "legal_basis_as_written": "…"}}
```

## Done
- Every measure pass candidate belongs to one entry.
- An entry with no stated aim is listed in `gaps`.
