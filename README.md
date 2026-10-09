# skills

Work from an evid set.
The directory tree is the workflow.

From the repo root:

```bash
tree --gitignore --dirsfirst -I '.git|.gitkeep'
```

The router is [`SKILL.md`](SKILL.md) at the repo root (name `jura`).
Point `[skills].paths` at this repo.
That loads the router.

A leaf page is `index.md`.
Open that page from the router.
`labquote` and `memo` are installed as their own skills, so those leaves keep `SKILL.md`.
A folder that only holds other folders is the path to a leaf.

A file with no extension is the raw URL of a skill that lives in another repo.

`typst` on `$PATH`.
Package `@preview/labquote:0.1.0` is fetched on first compile, or install locally from [evidlabel/labquote](https://github.com/evidlabel/labquote) via `./local_install.sh`.
