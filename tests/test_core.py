import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from exodus_metaphor.anchors import load_anchor_pairs
from exodus_metaphor.chunking import smart_paragraph_split
from exodus_metaphor.io import load_corpus, load_manifest


class CoreTests(unittest.TestCase):
    def test_smart_paragraph_split(self):
        text = "First paragraph has enough words to pass the length threshold.\n\nSecond paragraph also has enough words to pass the threshold."
        chunks = smart_paragraph_split(text, min_chars=20)
        self.assertEqual(len(chunks), 2)

    def test_load_anchor_pairs(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "anchors.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=["anchor", "positive", "notes"])
                writer.writeheader()
                writer.writerow({"anchor": "bondage", "positive": "constraint", "notes": "demo"})
            pairs = load_anchor_pairs(path)
            self.assertEqual(pairs[0].anchor, "bondage")
            self.assertEqual(pairs[0].positive, "constraint")

    def test_load_manifest_and_corpus(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            text_path = root / "sample.txt"
            text_path.write_text("A paragraph long enough to pass the minimum chunk length for this test.", encoding="utf-8")
            manifest = root / "manifest.json"
            manifest.write_text(
                json.dumps({"entries": [{"label": "Sample", "path": "sample.txt"}]}),
                encoding="utf-8",
            )
            entries = load_manifest(manifest)
            loaded = load_corpus(entries, min_chars=10)
            self.assertEqual(entries[0].label, "Sample")
            self.assertEqual(len(loaded[0].chunks), 1)


if __name__ == "__main__":
    unittest.main()
