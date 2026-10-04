# skills

Agent skills for work from an evid set. The directory tree is the workflow. A skill folder keeps the skill `name`, with `SKILL.md` plus optional `scripts/` and `references/` beside it.

From the repo root:

```bash
tree --gitignore --dirsfirst -I '.git|.gitkeep'
```

**ingest** brings a source in. **process** changes a document before a model sees it. **analyse** reads the evid set. **author** shapes a document and argues from it.

A file with no extension is the raw URL of a skill that lives in another repo.

The router is [`SKILL.md`](SKILL.md) at the repo root (name `jura`). [`jura/SKILL.md`](jura/SKILL.md) points at it, so the directory name matches the skill name.

Point `[skills].paths` at a skill folder. The directory name is the skill name.

`typst` on `$PATH`. Package `@preview/labquote:0.1.0` is fetched on first compile, or install locally from [evidlabel/labquote](https://github.com/evidlabel/labquote) via `./local_install.sh`.
