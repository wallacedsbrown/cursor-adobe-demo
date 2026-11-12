# Creative Export Demo (fictional)

This is a tiny **mock** image-production pipeline for a Cursor interview demonstration. `.asset` files are plain text placeholders; this does **not** parse PSDs or render images and is not Adobe code.

## What it does

- `discovery.py` finds `.asset` files recursively.
- `pipeline.py` orchestrates exports.
- `render.py` writes text previews to disk.
- `manifest.py` creates a JSON manifest of source-to-output mappings.
- `cli.py` provides the command-line interface.
- `.cursor/rules/export-quality.mdc` describes project-specific standards.

## Run baseline tests

```bash
python -m unittest discover -s tests -v
```

## Reproduce the known bug

```bash
python -m creative_export.cli sample_assets demo_output
cat demo_output/manifest.json
```

Both `campaign/hero.asset` and `social/hero.asset` export to `hero.preview.txt`, causing one preview to silently overwrite the other. The manifest has two jobs but only one output pathname.

## Desired improvement (do NOT implement before the demo)

Preserve the input directory structure in the output, e.g. `campaign/hero.preview.txt` and `social/hero.preview.txt`, without changing the public CLI. Add a regression test that proves both contents survive, that manifest paths are unique, and that nested directories are created. Consider backwards compatibility for flat inputs and the risk of path traversal when taking input paths. Avoid unrelated changes.

## Reset for another practice run

The source is a Git repository once you run `git init && git add . && git commit -m 'baseline'`. Then you can restore the baseline via Git. Don't use destructive resets without checking for wanted work.
