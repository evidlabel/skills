# timeline

A single chronology. Each event keeps every source that mentions it, and disagreements stay visible.

## `evidence/timeline/events@1` (basic)

**In scope:** every document type.

**Instruction:** Extract each span that places an event in time. Events include incidents, meetings, handovers, decisions, contacts, absences, and reports made. Copy verbatim, one page. Resolve relative dates ("last Tuesday", "i sidste uge") against the document date in `info.yml` (`dates`), and record how precise the date is.

**note:**
```json
{"event": "<kind>-<short slug>", "date": "YYYY-MM-DD|YYYY-MM|YYYY", "date_precision": "day|month|year|approx|relative-resolved|unknown",
 "actors": ["#(P1V1)", "child"], "basis": "observed|reported|document|unknown", "recorded_on": "<document date>", "confidence": 0.0}
```
Event kinds: `incident`, `contact`, `handover`, `meeting`, `decision`, `report-made`, `absence`, `health`, `school`, `move`, `other`.

## `evidence/timeline/build@1` (composite)

**Inputs:** passes with job prefix `evidence/timeline/events@` (required).

**Procedure:**
1. Merge candidates that describe the same event (same kind and actors, compatible dates) into one entry. Keep every source.
2. Mark the entry `conflict: true` when its sources give different dates, or give accounts that can't both be true. List which sources say what.
3. Order the entries by best date.
4. Put undated events in a separate list (`undated`).
5. Add each `gap` period: a stretch of more than 30 days (adjustable) inside the case period with no recorded events, or with records from one side only.
6. Record `knowledge_date` for each entry: the earliest `recorded_on` among its sources, meaning when the event first appears in any record.

**Finding (one per event):**
```json
{"id": "f12", "claim": "event",
 "sources": [{"uuid": "…", "pass": "…", "key": "…", "page": 2}],
 "values": {"event": "handover-missed", "date": "2026-03-04", "date_precision": "day", "actors": ["#(P1V1)", "child"],
            "conflict": false, "accounts": [], "knowledge_date": "2026-03-06"}}
```
Top-level fields: `"undated": ["f40", …]` and `"gaps": ["2026-05-01..2026-06-15: no records"]`.

## Done
- Every event pass candidate belongs to exactly one entry.
- Conflicts show every account.
- Gap periods are listed.
