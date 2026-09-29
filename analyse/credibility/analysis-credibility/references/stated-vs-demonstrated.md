# stated vs demonstrated

Compares what a person says about their own conduct with what the record shows they did.

## `credibility/stated-vs-demonstrated/stated@1` (basic)

**In scope:** statements, submissions, interview records, and correspondence by the person concerned.

**Instruction:** Extract claims a person makes about their own conduct, intentions, or values ("I always…", "I have supported contact", "jeg har altid samarbejdet").

**note:** `{"actor": "#(P1V1)", "behaviour": "<slug>", "claim_kind": "habitual|specific|value", "confidence": 0.0}`

Behaviour slugs (extend as needed, and reuse the slugs already used in the set): `supports-contact`, `follows-schedule`, `attends-meetings`, `responds-to-contact`, `cooperates-with-authority`, `informs-other-parent`, `shields-child-from-conflict`.

## `credibility/stated-vs-demonstrated/demonstrated@1` (basic)

**In scope:** logs, attendance records, message threads, authority notes, school and health records. Prefer documents not written by the actor.

**Instruction:** Extract records of what a person actually did or did not do.

**note:** `{"actor": "#(P1V1)", "behaviour": "<slug>", "outcome": "done|not-done|partial", "date": "YYYY-MM-DD|unknown", "confidence": 0.0}`

## `credibility/stated-vs-demonstrated/gap@1` (composite)

**Inputs:** passes with job prefixes `credibility/stated-vs-demonstrated/stated@` and `credibility/stated-vs-demonstrated/demonstrated@` (both required). Optional: the newest `analysis/evidence/inventory/*.json`, for authorship.

**Procedure:** For each actor and behaviour:
- `stated`: the number of claims, and the strongest `claim_kind`
- `demonstrated`: done, not-done, and partial counts, with the demonstrated rate done / (done + not-done)
- `self_sourced_share`: how much of the demonstrated evidence comes from the actor's own documents

A high stated level with a low demonstrated rate is the gap pattern. Report it as numbers.

**Finding:**
```json
{"id": "f1", "claim": "stated-vs-demonstrated", "sources": [{"uuid": "…", "pass": "…", "key": "…"}],
 "values": {"actor": "#(P1V1)", "behaviour": "attends-meetings", "stated": 3, "strongest_claim": "habitual",
            "done": 2, "not_done": 5, "partial": 0, "demonstrated_rate": 0.29, "self_sourced_share": 0.0}}
```

## Done
- The same behaviours are assessed for every party who claims them.
- A behaviour with a claim but no records is listed in `gaps`.
