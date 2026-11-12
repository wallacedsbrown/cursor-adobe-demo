"""Mock renderer: writes text previews, not actual image files."""
from pathlib import Path


def render_preview(asset: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(f"Preview for {asset.as_posix()}\n" + asset.read_text(), encoding='utf-8')
