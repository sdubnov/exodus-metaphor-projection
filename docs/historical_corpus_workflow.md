# Historical Corpus Workflow

This repository does not currently include the original Exodus research corpus.

The public figures in `docs/figures/` were generated on the local machine from text files under:

```text
/Users/sdubnov/Documents/Research/Work/Exodus/exodus_corpus
```

Those files were referenced through private manifests under `local_manifests/`. That directory is intentionally ignored by Git because several texts in the exploratory corpus are not clearly redistributable as full text.

## How The Hosted Figures Were Generated

The religious projection was generated with:

```bash
python scripts/run_metaphor_projection_demo.py \
  --anchors data/anchors/berlin_liberty_anchor_pairs.csv \
  --manifest local_manifests/religious.local.json \
  --output docs/figures/religious_metaphor_projection.html \
  --seed 42 \
  --epochs 250 \
  --local-files-only \
  --max-chunks-per-text 300 \
  --hide-hover-text
```

The modern political projection was generated with:

```bash
python scripts/run_metaphor_projection_demo.py \
  --anchors data/anchors/berlin_liberty_anchor_pairs.csv \
  --manifest local_manifests/modern.local.json \
  --output docs/figures/modern_metaphor_projection.html \
  --seed 42 \
  --epochs 250 \
  --local-files-only \
  --max-chunks-per-text 300 \
  --hide-hover-text
```

The `--hide-hover-text` flag is important for the public GitHub Pages version. It removes passage text from Plotly hover labels, so the committed HTML files contain point coordinates and source labels but not the full underlying corpus passages.

The same two commands are also packaged as:

```bash
bash scripts/run_historical_figures.sh
```

## Local Corpus Setup

To rerun the historical demo locally, place legally obtained text files in:

```text
data/private_corpus/
```

Then copy the manifest templates:

```bash
cp corpus_manifest.exodus.local.example.json local_manifests/exodus.local.json
cp corpus_manifest.exodus.religious.local.example.json local_manifests/religious.local.json
cp corpus_manifest.exodus.modern.local.example.json local_manifests/modern.local.json
```

Edit the paths and source notes if your local filenames differ. For the two figures currently shown in the analysis page, create two manifests:

```text
local_manifests/religious.local.json
local_manifests/modern.local.json
```

The religious manifest should include Exodus and Surah Al-Qasas. The modern manifest should include Herzl, MLK, and Douglass.

## Redistribution Notes

This is a practical rights summary, not legal advice.

- The King James Version is generally treated as public domain in the United States, though there are jurisdiction-specific caveats in the United Kingdom. See the CrossWire KJV copyright note: <https://www.crosswire.org/sword/copyright/ModInfoCopyright.jsp?modName=KJVPCE>.
- Frederick Douglass's 1845 *Narrative* is public domain in the United States. See Project Gutenberg eBook 23: <https://www.gutenberg.org/ebooks/23>.
- The Clear Quran translation states that reproduction requires prior written consent except for limited licensed excerpts by qualifying organizations. See: <https://mail.theclearquran.org/copyright-information/>.
- Martin Luther King Jr.'s writings and speeches are administered by rights holders; Stanford's King Institute says it cannot grant reproduction permission and directs users to the estate's licensor. See: <https://kinginstitute.stanford.edu/information-researchers>.
- Isaiah Berlin's *Two Concepts of Liberty* remains under copyright in modern editions. See Oxford Academic's copyright page for *Liberty*: <https://academic.oup.com/book/7968/chapter-abstract/153273212>.
- Herzl's *Altneuland* is public domain in the original German; the redistributability of an English text depends on the specific translation. The 1941 Lotta Levensohn translation is marked `PD-US-not-renewed` on Wikimedia Commons: <https://commons.wikimedia.org/wiki/File:Old-New_Land.djvu>.

For that reason, the repository should keep the complete research corpus out of Git unless each file's redistribution status is verified and documented.

## Recommended Public Position

For the paper and GitHub README, describe this repository as a reference implementation with an optional local historical-corpus demo, not as a complete reproducibility archive. The public smoke test can use the synthetic corpus, while the historical demo can be rerun locally by users who provide their own permitted copies of the texts.
