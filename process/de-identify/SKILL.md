---
name: de-identify
description: Use when a local model strips identifiers with did, checks the result, and hands the anonymised document to the case evid set.
---

# de-identify

The tool is the URL in `did`. Open it and follow it. A local model drives it. The router keeps identifiable text on that local model.

- review the output for a leaked identifier
- review entries that are variants of one identifier
- review a trivial token, a single letter or a single number, that mangles the text if it is treated as an identifier
- adjust the yaml and run it again until the output holds
- export a pdf whose placeholders stand in for the people (Person 1, and so on)
- import that pdf into the case evid set the same way as any other document
