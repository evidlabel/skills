---
name: did
description: Use when a local model removes PII from a document with did, checks the result, and writes the anonymized form into the case evid set.
---

- drive PII with local model, if available
- let model use did to remove PII
- let model review output, check for 
    - leaked PII
    - entries that are extracted as separate, but which are variants
    - trivial PII (i.e. single numbers, single letters etc) that cause mangling of output if treated as PII
- let model adjust yaml and reoutput, check again, until good output without leak
- then output into case evid in anonymized form
