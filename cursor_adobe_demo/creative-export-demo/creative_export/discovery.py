"""Find asset descriptions in an input tree."""
from pathlib import Path


def find_assets(source_root: Path) -> list[Path]:
    """Return all .asset files, including in nested subfolders."""
    return sorted(source_root.rglob('*.asset'))
