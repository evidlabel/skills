#!/usr/bin/env python3
"""Emit the document-shape parts of a Typst document.

`preamble` sets page, type, and paragraph defaults. `title` renders a title
block for a document type (plain, memo, brief, letter, book, booklet).
Quote keys and the bibliography are not this script's job. Output is a Typst
fragment: to stdout, or to `-o FILE`.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

PAPER = ("a4", "us-letter")

PRESETS = {
    "plain": {
        "margin": "2.5cm",
        "numbering": None,
        "note": "uniform 2.5cm margin, no page numbers",
    },
    "legal": {
        "margin": "(top: 2.5cm, bottom: 2.5cm, left: 3cm, right: 2.5cm)",
        "numbering": "1",
        "note": "left binding margin, centered page numbers",
    },
}


def content_escape(text: str) -> str:
    out = text.replace("\\", "\\\\")
    for ch in ("[", "]", "#"):
        out = out.replace(ch, "\\" + ch)
    return out


def preamble(preset: str, paper: str, font: str, size: int, lang: str,
             justify: bool, page_numbers: bool | None = None,
             sec_numbering: str | None = None,
             running_header: str | None = None) -> str:
    p = PRESETS[preset]
    numbering = p["numbering"]
    if page_numbers is not None:
        numbering = "1" if page_numbers else None
    num = f', numbering: "{numbering}", number-align: center' if numbering else ""
    just = "true" if justify else "false"
    head = ""
    if sec_numbering:
        head += f'#set heading(numbering: "{sec_numbering}")\n'
    if running_header:
        esc = content_escape(running_header)
        head += (
            "#set page(header: context {\n"
            "  if counter(page).get().first() > 1 {\n"
            f'    align(right, text(size: 9pt, fill: luma(35%))[{esc}])\n'
            "  }\n"
            "})\n"
        )
    return (
        f'#set text(font: "{font}", size: {size}pt, lang: "{lang}")\n'
        f'#set page(paper: "{paper}", margin: {p["margin"]}{num})\n'
        f"#set par(justify: {just}, leading: 0.75em, "
        f"first-line-indent: 0em, spacing: 0.9em)\n"
        + head
        + "#show heading: set block(above: 1.1em, below: 0.5em)\n"
        '#show heading.where(level: 1): set text(size: 1.15em, weight: "bold")\n'
        '#show heading.where(level: 2): set text(size: 1.0em, weight: "bold")\n'
    )


def outline_block(title: str, depth: int | None = None) -> str:
    t = content_escape(title.strip() or "Contents")
    d = f", depth: {depth}" if depth else ""
    return f"#outline(title: [{t}]{d})\n"


def _lines(field: str) -> list[str]:
    return [ln.strip() for ln in field.split("\\n") if ln.strip()]


def memo_block(to: str, sender: str, date: str, subject: str) -> str:
    rows = []
    for label, val in (("To", to), ("From", sender), ("Date", date), ("Subject", subject)):
        if val.strip():
            rows.append(f"[*{label}:*], [{content_escape(val.strip())}]")
    if not rows:
        return ""
    body = ",\n  ".join(rows)
    return (
        "#grid(\n  columns: (auto, 1fr),\n  column-gutter: 1.2em,\n"
        f"  row-gutter: 0.7em,\n  {body},\n)\n\n"
        "#v(0.6em, weak: true)\n#line(length: 100%, stroke: 0.6pt + black)\n"
        "#v(1em, weak: true)\n"
    )


def letter_block(sender: str, recipient: str, date: str, subject: str) -> str:
    parts = []
    sender_lines = _lines(sender)
    if sender_lines:
        inner = " \\\n".join(content_escape(ln) for ln in sender_lines)
        parts.append(f"#align(right)[{inner}]")
    if date.strip():
        parts.append(f"[{content_escape(date.strip())}]")
    recip_lines = _lines(recipient)
    if recip_lines:
        inner = " \\\n".join(content_escape(ln) for ln in recip_lines)
        parts.append(f"[{inner}]")
    if subject.strip():
        parts.append(f"[*Subject:* {content_escape(subject.strip())}]")
    if not parts:
        return ""
    return "\n\n#v(1em, weak: true)\n\n".join(parts) + "\n"


def plain_block(title: str, date: str) -> str:
    parts = []
    if title.strip():
        parts.append(
            f'#align(center, text(size: 17pt, weight: "bold")'
            f"[{content_escape(title.strip())}])"
        )
    if date.strip():
        parts.append(
            f'#align(center, text(size: 11pt, fill: luma(30%))'
            f"[{content_escape(date.strip())}])"
        )
    return "\n".join(parts) + ("\n" if parts else "")


def brief_block(title: str, date: str) -> str:
    """Brief top line: short description left, date right, hairline beneath."""
    left = content_escape(title.strip())
    right = content_escape(date.strip())
    if not left and not right:
        return ""
    return (
        "#grid(\n  columns: (1fr, auto),\n  column-gutter: 1em,\n"
        f'  [#text(size: 1.2em, weight: "bold")[{left}]], [{right}],\n)\n\n'
        "#v(0.5em, weak: true)\n#line(length: 100%, stroke: 0.6pt + black)\n"
        "#v(0.9em, weak: true)\n"
    )


def book_block(title: str, subtitle: str, author: str, date: str) -> str:
    """Title page for a book or study, ending with a page break."""
    parts = ["#v(2.5cm)"]
    if title.strip():
        parts.append(f'#align(center, text(size: 22pt, weight: "bold")[{content_escape(title.strip())}])')
    if subtitle.strip():
        parts.append(f'#align(center, text(size: 12pt, style: "italic", fill: luma(20%))[{content_escape(subtitle.strip())}])')
    parts.append("#v(1.5cm)")
    if author.strip():
        parts.append(f'#align(center, text(size: 11pt)[{content_escape(author.strip())}])')
    if date.strip():
        parts.append(f'#align(center, text(size: 10pt, fill: luma(35%))[{content_escape(date.strip())}])')
    parts.append("#pagebreak()")
    return "\n".join(parts) + "\n"


def booklet_block(title: str, subtitle: str, author: str, date: str) -> str:
    """Compact centered title for a short self-contained booklet."""
    parts = []
    if title.strip():
        parts.append(f'#align(center, text(size: 16pt, weight: "bold")[{content_escape(title.strip())}])')
    if subtitle.strip():
        parts.append(f'#align(center, text(size: 11pt, style: "italic", fill: luma(20%))[{content_escape(subtitle.strip())}])')
    if author.strip():
        parts.append(f'#align(center, text(size: 10pt)[{content_escape(author.strip())}])')
    if date.strip():
        parts.append(f'#align(center, text(size: 9pt, fill: luma(35%))[{content_escape(date.strip())}])')
    return "\n".join(parts) + ("\n" if parts else "")


def title_block(doc_type: str, title: str, subtitle: str, author: str, to: str,
                sender: str, date: str, subject: str, recipient: str) -> str:
    if doc_type == "memo":
        return memo_block(to, sender, date, subject)
    if doc_type == "letter":
        return letter_block(sender, recipient, date, subject)
    if doc_type == "brief":
        return brief_block(title, date)
    if doc_type == "book":
        return book_block(title, subtitle, author, date)
    if doc_type == "booklet":
        return booklet_block(title, subtitle, author, date)
    return plain_block(title, date)


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        epilog="presets: " + ", ".join(f"{k} ({v['note']})" for k, v in PRESETS.items()),
    )
    sub = ap.add_subparsers(dest="part", required=True)

    pp = sub.add_parser("preamble", help="page + type + paragraph setup")
    pp.add_argument("--preset", choices=list(PRESETS), default="legal")
    pp.add_argument("--paper", choices=PAPER, default="a4")
    pp.add_argument("--font", default="DejaVu Serif")
    pp.add_argument("--size", type=int, default=12, help="body text size in pt")
    pp.add_argument("--lang", default="da")
    pp.add_argument("--no-justify", dest="justify", action="store_false",
                    help="leave paragraphs ragged-right")
    pp.add_argument("--page-numbers", action=argparse.BooleanOptionalAction,
                    default=None, help="force page numbers on/off (default: preset)")
    pp.add_argument("--sec-numbering", default=None,
                    help='number section headings, e.g. "1.1" or "1."')
    pp.add_argument("--running-header", default=None,
                    help="text in the top-right of pages after the first")
    pp.add_argument("-o", "--output", type=Path, help="write here (default stdout)")

    tp = sub.add_parser("title", help="per-doc-type title block")
    tp.add_argument("--doc-type", choices=["plain", "memo", "brief", "letter", "book", "booklet"], default="plain")
    tp.add_argument("--title", default="", help="plain/book/booklet title / brief short description")
    tp.add_argument("--subtitle", default="", help="book/booklet subtitle")
    tp.add_argument("--author", default="", help="book/booklet author or organisation")
    tp.add_argument("--to", default="", help="memo: To line")
    tp.add_argument("--sender", default="", help="memo From / letter sender (use \\n for line breaks)")
    tp.add_argument("--date", default="", help="memo/letter/brief/book/booklet Date line")
    tp.add_argument("--subject", default="", help="memo/letter Subject line")
    tp.add_argument("--recipient", default="", help="letter recipient (use \\n for line breaks)")
    tp.add_argument("-o", "--output", type=Path, help="write here (default stdout)")

    op = sub.add_parser("outline", help="table of contents")
    op.add_argument("--title", default="Contents")
    op.add_argument("--depth", type=int, default=None, help="max heading level")
    op.add_argument("-o", "--output", type=Path, help="write here (default stdout)")

    args = ap.parse_args()
    if args.part == "preamble":
        out = preamble(args.preset, args.paper, args.font, args.size,
                       args.lang, args.justify, args.page_numbers,
                       args.sec_numbering, args.running_header)
    elif args.part == "outline":
        out = outline_block(args.title, args.depth)
    else:
        out = title_block(args.doc_type, args.title, args.subtitle, args.author,
                          args.to, args.sender, args.date, args.subject,
                          args.recipient)

    if args.output:
        args.output.write_text(out)
    else:
        sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
