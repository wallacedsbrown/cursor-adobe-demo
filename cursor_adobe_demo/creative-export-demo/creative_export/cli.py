"""Command-line entrypoint for the export pipeline."""
import argparse
from pathlib import Path
from .pipeline import export_assets


def main() -> None:
    parser = argparse.ArgumentParser(description='Export mock creative asset previews')
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    records = export_assets(args.source, args.output)
    print(f'Exported {len(records)} asset jobs to {args.output}')
    for record in records:
        print(f"  {record['source']} -> {record['output']}")


if __name__ == '__main__':
    main()
