---
name: sources
description: Use when a public statute, Danish judgment, or Council of Europe document is fetched into the local evid set.
---

# sources

lawcite, domdb, and hudoc obtain public legal documents.

These generally do not contain the case's PII, so they go straight into the local evid set.
From the case root, `evid --db evid`.

The file of the same name is the URL of that tool's skill.
Open it and follow it.

- lawcite: Danish statutes from retsinformation (`ingest/danish-statutes/lawcite`)
- domdb: Danish judgments from Domsdatabasen (`ingest/danish-verdicts/domdb`)
- hudoc: Council of Europe documents from a HUDOC subsite (`ingest/council-of-europe-download/hudoc`)
