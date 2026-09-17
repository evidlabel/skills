#!/usr/bin/env python3
"""Build a compiling labquote skeleton from evid gather YAML.

Quote slugs (not :main) become #blockq keys. Optional --title heading.
Commentary and document shape are left to the agent. Does not invent entries.
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


def typst_content_escape(text: str) -> str:
    out = text.replace("\\", "\\\\")
    for ch in ("[", "]", "#"):
        out = out.replace(ch, "\\" + ch)
    return out


def memo_block(to: str, sender: str, date: str, subject: str) -> str:
    rows = []
    for label, val in (("To", to), ("From", sender), ("Date", date), ("Subject", subject)):
        if val.strip():
            rows.append(f"[*{label}:*], [{typst_content_escape(val.strip())}]")
    if not rows:
        return ""
    body = ",\n  ".join(rows)
    return (
        "#grid(\n  columns: (auto, 1fr),\n  column-gutter: 1.2em,\n"
        f"  row-gutter: 0.7em,\n  {body},\n)\n\n"
        "#v(0.6em, weak: true)\n#line(length: 100%, stroke: 0.5pt + luma(60%))\n"
        "#v(1em, weak: true)\n\n"
    )


def brev_block(sender: str, recipient: str, date: str, subject: str) -> str:
    parts = []
    sender_lines = [ln.strip() for ln in sender.split("\\n") if ln.strip()]
    if sender_lines:
        inner = " \\\n".join(typst_content_escape(ln) for ln in sender_lines)
        parts.append(f"#align(right)[{inner}]")
    if date.strip():
        parts.append(f"[{typst_content_escape(date.strip())}]")
    recip_lines = [ln.strip() for ln in recipient.split("\\n") if ln.strip()]
    if recip_lines:
        inner = " \\\n".join(typst_content_escape(ln) for ln in recip_lines)
        parts.append(f"[{inner}]")
    if subject.strip():
        parts.append(f"[*Subject:* {typst_content_escape(subject.strip())}]")
    if not parts:
        return ""
    return "\n\n#v(1em, weak: true)\n\n".join(parts) + "\n\n#v(1em, weak: true)\n\n"


def render_typ(
    keys: list[str],
    font: str,
    cite_style: str,
    refs_name: str,
    lang: str,
    title: str = "",
    doc_type: str = "notat",
    to: str = "",
    sender: str = "",
    date: str = "",
    subject: str = "",
    recipient: str = "",
) -> str:
    font_lit = font.replace("\\", "\\\\").replace('"', '\\"')
    sep = "\n\n#v(1.2em, weak: true)\n\n"
    blocks = sep.join(f'#blockq("{typst_escape(k)}")' for k in keys)
    head = ""
    if doc_type == "memo":
        head = memo_block(to, sender, date, subject)
    elif doc_type == "brev":
        head = brev_block(sender, recipient, date, subject)
    elif title:
        safe = typst_content_escape(title)
        head = f'#align(center, text(size: 17pt, weight: "bold")[{safe}])\n\n#v(1em, weak: true)\n\n'
    return f"""#import "@preview/labquote:0.1.0": *
#set text(font: "{font_lit}", size: 12pt, lang: "{lang}")
#set page(paper: "a4", margin: (top: 2.5cm, bottom: 2.5cm, left: 3cm, right: 2.5cm), numbering: "1", number-align: center)
#set par(justify: true, leading: 0.75em, first-line-indent: 0em, spacing: 0.9em)
#setup(yaml("{refs_name}"), cite-style: "{cite_style}")

{head}{blocks}

#v(1em, weak: true)
#bibliography-custom()
"""


def comments(raw: str) -> str:
    lines = [ln for ln in raw.splitlines() if ln.startswith("#")]
    return ("\n".join(lines) + "\n") if lines else ""


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("refs", type=Path, help="Hayagriva YAML from evid set gather")
    p.add_argument("-o", "--output", type=Path, default=Path("main.typ"), help="Typst file to write")
    p.add_argument("--font", default="DejaVu Serif")
    p.add_argument("--cite-style", default="short")
    p.add_argument("--lang", default="da")
    p.add_argument("--title", default="", help="Typst heading (= …); omit for keys only")
    p.add_argument("--doc-type", choices=["notat", "memo", "brev"], default="notat",
                   help="title block preset (default notat: centered title)")
    p.add_argument("--to", default="", help="memo To line")
    p.add_argument("--sender", default="", help="memo From / letter sender (use \\n for line breaks)")
    p.add_argument("--date", default="", help="memo/letter Date line")
    p.add_argument("--subject", default="", help="memo/letter Subject line")
    p.add_argument("--recipient", default="", help="letter recipient (use \\n for line breaks)")
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

    title = " ".join(args.title.split())
    args.output.write_text(
        render_typ(
            keys,
            args.font,
            args.cite_style,
            args.refs.name,
            args.lang,
            title,
            doc_type=args.doc_type,
            to=args.to,
            sender=args.sender,
            date=args.date,
            subject=args.subject,
            recipient=args.recipient,
        )
    )
    print("wrote", args.output, "blockq", *keys)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
