---
name: charts
description: >
  Use when a document needs a statistical chart: a bar, a line, or a
  distribution. Matplotlib, saved as SVG. Not a narrative timeline, not an
  organisation map (orgnet), and not a flow (sankey).
license: MIT
compatibility: Python with matplotlib on PATH, typically via uv.
---

# charts

One claim per figure. The title states the claim in plain words. Both axes name the unit.

```bash
uv run --with matplotlib python3 chart.py
```

`chart.py` sits next to the document and writes `chart.svg`. A bar chart is sorted by the value it claims, unless the axis is time or an order the source already uses. A line chart uses time on the horizontal axis. No grid that competes with the marks. No second axis unless the claim is the comparison of two units.

Read the SVG before placing it in the Typst document.
