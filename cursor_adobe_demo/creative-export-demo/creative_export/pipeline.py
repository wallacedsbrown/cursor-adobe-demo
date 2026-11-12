"""Export mock previews for a source tree of creative assets."""
from pathlib import Path
from .discovery import find_assets
from .manifest import write_manifest
from .render import render_preview


def export_assets(source_root: Path, output_root: Path) -> list[dict[str, str]]:
    """Export each input .asset file and write a manifest.

    Known limitation: output filenames are derived from the basename only.
    This is intentional for the demonstration exercise.
    """
    source_root = Path(source_root)
    output_root = Path(output_root)
    output_root.mkdir(parents=True, exist_ok=True)
    records = []
    for asset in find_assets(source_root):
        destination = output_root / f'{asset.stem}.preview.txt'
        render_preview(asset, destination)
        records.append({'source': asset.relative_to(source_root).as_posix(),
                        'output': destination.relative_to(output_root).as_posix()})
    write_manifest(output_root, records)
    return records
