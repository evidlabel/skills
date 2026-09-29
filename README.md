# skills

Agent Skills for Typst documents built from an evid set. Format: [Agent Skills](https://agentskills.io/specification). Repo layout follows [anthropics/skills](https://github.com/anthropics/skills).

Each skill is a folder under [`skills/`](skills/) with a `SKILL.md` (`name` + `description`) plus optional `scripts/`, `references/`, `assets/`.

| Skill | What it does |
|-------|----------------|
| [`labquote`](skills/labquote/SKILL.md) | Gather (`evid set gather` → `refs.yml`) and render verbatim quotes in a keys-only Typst document. |
| [`memo`](skills/memo/SKILL.md) | Dated memo that answers one question from verbatim quotes. |

Router: [`SKILL.md`](SKILL.md) at the repo root (name `jura`). jura.sh links here.

## Install

Point `[skills].paths` at `skills/`:

```toml
[skills]
paths = ["~/projects/jura/skills/skills"]
```

Or symlink into the user skill dir (directory name = skill name):

```bash
for d in skills/*/; do
  [ -f "$d/SKILL.md" ] || continue
  ln -sfn "$PWD/${d%/}" ~/.claude/skills/$(basename "$d")
  ln -sfn "$PWD/${d%/}" ~/.grok/skills/$(basename "$d")
done
```

`typst` on `$PATH`. Package `@preview/labquote:0.1.0` is fetched on first compile, or install locally from [evidlabel/labquote](https://github.com/evidlabel/labquote) via `./local_install.sh`.
