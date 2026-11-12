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
            self.assertEqual('banner.preview.txt', records[0]['output'])
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

    def test_same_basename_in_different_folders_do_not_collide(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'source'
            output = root / 'output'
            campaign = source / 'campaign'
            social = source / 'social'
            campaign.mkdir(parents=True)
            social.mkdir()
            (campaign / 'hero.asset').write_text('Layer: Campaign hero\n', encoding='utf-8')
            (social / 'hero.asset').write_text('Layer: Social hero\n', encoding='utf-8')

            records = export_assets(source, output)

            campaign_preview = output / 'campaign' / 'hero.preview.txt'
            social_preview = output / 'social' / 'hero.preview.txt'
            self.assertTrue(campaign_preview.parent.is_dir())
            self.assertTrue(social_preview.parent.is_dir())
            self.assertIn('Layer: Campaign hero', campaign_preview.read_text(encoding='utf-8'))
            self.assertIn('Layer: Social hero', social_preview.read_text(encoding='utf-8'))
            self.assertFalse((output / 'hero.preview.txt').exists())

            outputs = [record['output'] for record in records]
            self.assertEqual(
                ['campaign/hero.preview.txt', 'social/hero.preview.txt'],
                outputs,
            )
            self.assertEqual(len(outputs), len(set(outputs)))
            manifest = json.loads((output / 'manifest.json').read_text(encoding='utf-8'))
            self.assertEqual(records, manifest['exports'])


if __name__ == '__main__':
    unittest.main()
