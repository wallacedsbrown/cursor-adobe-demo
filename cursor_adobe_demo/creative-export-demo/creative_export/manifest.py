"""Record exported files for downstream build steps."""
from pathlib import Path
import json


def write_manifest(output_root: Path, records: list[dict[str, str]]) -> Path:
    manifest_path = output_root / 'manifest.json'
    manifest_path.write_text(json.dumps({'exports': records}, indent=2) + '\n', encoding='utf-8')
    return manifest_path
