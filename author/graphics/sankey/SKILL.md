---
name: sankey
description: >
  Use when a document needs a flow of quantities from one stage to the next:
  money, referrals, caseload, or throughput. Not an organisation map (orgnet),
  not a narrative timeline, and not a bar or line chart.
license: MIT
compatibility: Python with matplotlib, or plotly when the flow has many nodes.
---

# sankey

One figure. Each band is a quantity moving from a source to a target. The width is the quantity. The figure names the unit (kr., sager, personer).

Few nodes, and the inflows balance the outflows: `matplotlib.sankey.Sankey`, saved as SVG. Many nodes, or splits that Sankey cannot lay out: `plotly.graph_objects.Sankey`, written to SVG.

One colour for the flow. A second colour only when two kinds of flow must be told apart. No gradient and no 3D.

Read the SVG back. Drop a band that does not change the claim. Place `sankey.svg` in the Typst document next to the sentence it carries.
