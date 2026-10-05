---
name: orgnet
description: >
  Use when a document needs a map of how organisations connect: membership,
  shared members, or who sits with whom. Neato for an undirected net, D2 for
  a directed step, Mermaid for a small graph in a note. Not a timeline, not a
  quantity flow (sankey), and not a statistical chart.
license: MIT
compatibility: Graphviz neato, d2, or a Mermaid renderer on PATH.
---

# orgnet

Orgs only. One node per organisation. An edge only where a source names the pair. People are not nodes. A shared member is one node, not a copy in each source.

| Graph | Tool | Command |
|-------|------|---------|
| Undirected membership net. Bridges sit in the middle. | Graphviz neato | `neato -Tsvg net.dot -o net.svg` |
| Directed steps, read left to right: sequence, membership, or money. | D2 | `d2 --layout=elk steps.d2 steps.svg` |
| A small graph in a Markdown note or a slide. | Mermaid | a fenced `mermaid` block |

The print document takes the SVG. A Mermaid fence is not Typst. `anno d2` edits a graph; the print file is the `d2 --layout=elk` SVG.

Drop an edge that no source names. Read the SVG before placing it. If the net is unreadable, restack it. Do not delete a named org to make it pretty.
