"""Export mock previews for a source tree of creative assets."""
from pathlib import Path
from .discovery import find_assets
from .manifest import write_manifest
from .render import render_preview


def _preview_destination(source_root: Path, output_root: Path, asset: Path) -> Path:
    """Map an asset to a preview path that keeps its source-relative directory.

    The destination is built from the logical path under source_root, not from
    the basename alone, so campaign/hero.asset and social/hero.asset do not
    overwrite each other. Symlinks are not resolved: following them would move
    the preview to the target's directory.
    """
    relative = asset.relative_to(source_root)
    if relative.is_absolute() or any(part == '..' for part in relative.parts):
        raise ValueError(f'asset path escapes source root: {relative.as_posix()}')
    return output_root / relative.with_name(f'{relative.stem}.preview.txt')


def export_assets(source_root: Path, output_root: Path) -> list[dict[str, str]]:
    """Export each input .asset file and write a manifest.

    Preview paths mirror the source-relative directory, so assets that share
    a filename in different folders stay distinct.
    """
    source_root = Path(source_root)
    output_root = Path(output_root)
    output_root.mkdir(parents=True, exist_ok=True)
    records = []
    for asset in find_assets(source_root):
        destination = _preview_destination(source_root, output_root, asset)
        render_preview(asset, destination)
        records.append({'source': asset.relative_to(source_root).as_posix(),
                        'output': destination.relative_to(output_root).as_posix()})
    write_manifest(output_root, records)
    return records
