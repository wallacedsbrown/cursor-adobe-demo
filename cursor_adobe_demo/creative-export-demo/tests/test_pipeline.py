import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from creative_export.pipeline import export_assets


class ExportPipelineTests(unittest.TestCase):
    def test_single_asset_exports_preview_and_manifest(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'source'
            output = root / 'output'
            source.mkdir()
            (source / 'banner.asset').write_text('Layer: banner\n', encoding='utf-8')

            records = export_assets(source, output)

            self.assertEqual(1, len(records))
            self.assertTrue((output / 'banner.preview.txt').exists())
            manifest = json.loads((output / 'manifest.json').read_text(encoding='utf-8'))
            self.assertEqual(records, manifest['exports'])

    def test_distinct_basenames_do_not_collide(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'source'
            output = root / 'output'
            source.mkdir()
            (source / 'banner.asset').write_text('Banner\n', encoding='utf-8')
            (source / 'poster.asset').write_text('Poster\n', encoding='utf-8')
            records = export_assets(source, output)
            self.assertEqual(2, len({r['output'] for r in records}))


if __name__ == '__main__':
    unittest.main()
