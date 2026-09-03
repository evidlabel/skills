#!/usr/bin/env python3
"""Build a compiling labquote skeleton from evid gather YAML.

Quote slugs (not :main) become #blockq keys. Commentary is left to the agent.
Does not invent entries.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


def prefix(key: str) -> str:
    return key.split(":", 1)[0] if ":" in key else key


def is_main(key: str) -> bool:
    return key == "main" or key.endswith(":main")


def mains(data: dict) -> dict[str, dict]:
    out = {}
    for k, v in data.items():
        if is_main(k) and isinstance(v, dict):
            out[prefix(k)] = v
    return out


def quote_keys(data: dict) -> list[str]:
    return [k for k in data if not is_main(k) and isinstance(data[k], dict)]


def fill_from_main(data: dict) -> dict:
    parent = mains(data)
    for k in quote_keys(data):
        entry = data[k]
        src = parent.get(prefix(k), {})
        for field in ("author", "date", "url"):
            if not entry.get(field) and src.get(field):
                entry[field] = src[field]
    return data


def typst_escape(key: str) -> str:
    return key.replace("\\", "\\\\").replace('"', '\\"')


def render_typ(keys: list[str], font: str, cite_style: str, refs_name: str, lang: str) -> str:
    font_lit = font.replace("\\", "\\\\").replace('"', '\\"')
    blocks = "\n\n".join(f'#blockq("{typst_escape(k)}")' for k in keys)
    return f"""#import "@preview/labquote:0.1.0": *
#set text(font: "{font_lit}", lang: "{lang}")
#setup(yaml("{refs_name}"), cite-style: "{cite_style}")

#align(right)[#datetime.today().display("[day].[month].[year]")]

= Memo

{blocks}

#bibliography-custom()
"""


def comments(raw: str) -> str:
    lines = [ln for ln in raw.splitlines() if ln.startswith("#")]
    return ("\n".join(lines) + "\n") if lines else ""


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("refs", type=Path, help="Hayagriva YAML from evid set gather")
    p.add_argument("-o", "--output", type=Path, default=Path("main.typ"))
    p.add_argument("--font", default="DejaVu Sans")
    p.add_argument("--cite-style", default="short")
    p.add_argument("--lang", default="da")
    p.add_argument("--write-refs", action="store_true", help="write author/date from :main onto quote slugs")
    p.add_argument("--max-quotes", type=int, default=12, help="refuse a dump larger than this; subset refs.yml first")
    args = p.parse_args()
    if yaml is None:
        sys.exit("refs_to_typ.py needs PyYAML")

    raw = args.refs.read_text()
    data = yaml.safe_load(raw)
    if not isinstance(data, dict) or not data:
        sys.exit(f"no entries in {args.refs}")

    data = fill_from_main(data)
    keys = quote_keys(data)
    if not keys:
        sys.exit("no quote slugs in refs.yml (only :main). evid doc quote first, then gather.")
    if len(keys) > args.max_quotes:
        sys.exit(
            f"{len(keys)} quote slugs (max {args.max_quotes}). "
            "Subset refs.yml to the cited keys, or pass --max-quotes."
        )
    docs = {prefix(k) for k in data if is_main(k)}
    quoted = {prefix(k) for k in keys}
    missing = sorted(docs - quoted)
    if missing:
        sys.exit(
            "no quote slug for: "
            + ", ".join(missing)
            + ". evid doc quote each of those docs, then gather."
        )

    if args.write_refs:
        dumped = yaml.safe_dump(data, allow_unicode=True, sort_keys=False)
        args.refs.write_text(comments(raw) + dumped)

    args.output.write_text(
        render_typ(keys, args.font, args.cite_style, args.refs.name, args.lang)
    )
    print("wrote", args.output, "blockq", *keys)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
