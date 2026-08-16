# Run The Exodus Metaphor Projection Demo

The default commands use the small sample corpus included in GitHub. They are intended as smoke tests for the public reference implementation. They do not reproduce the hosted figures in `docs/figures/`, which were generated from a separate local historical corpus.

The sample corpus is designed for a simple comparison: the unguided embedding baseline shows ordinary sentence-embedding structure, while the anchor-guided metaphor projection shows how the same passages move after training the projection on curated Exodus/liberty anchor pairs. The metaphor projection is not expected to preserve source-label clusters; it may bring passages from different files closer when they express related anchor themes.

Sample-demo caption: The unguided embedding baseline tends to separate the synthetic passages by genre and surface vocabulary: narrative, philosophical, civic, and unrelated control passages form different clouds. The anchor-guided metaphor projection reorganizes the narrative, philosophical, and civic passages around shared Exodus/liberty concerns such as coercion, departure, law, covenant, agency, and collective future. The unrelated control text is included to test whether passages outside this metaphorical field remain peripheral.

## 1. Create Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Run The Unguided Embedding Baseline

```bash
python scripts/run_baseline_demo.py \
  --manifest corpus_manifest.example.json \
  --output outputs/figures/embedding_baseline.html \
  --seed 42
```

Expected result:

- chunk counts printed in the terminal
- `outputs/figures/embedding_baseline.html`

Optional 3D baseline:

```bash
python scripts/run_3d_baseline_demo.py \
  --manifest corpus_manifest.example.json \
  --output outputs/figures/embedding_baseline_3d.html \
  --seed 42
```

## 3. Run The Metaphor Projection Demo

```bash
python scripts/run_metaphor_projection_demo.py \
  --anchors data/anchors/berlin_liberty_anchor_pairs.csv \
  --manifest corpus_manifest.example.json \
  --output outputs/figures/metaphor_projection.html \
  --seed 42
```

Expected result:

- anchor count and chunk counts printed in the terminal
- `outputs/figures/metaphor_projection.html`

This run uses the small sample corpus included in GitHub. It is a smoke test for the method and code path, not a reproduction of the hosted Exodus-corpus figures.

## 4. Use Your Own Corpus

Copy `corpus_manifest.example.json` and edit each entry:

```json
{
  "label": "MyText",
  "path": "path/to/my_text.txt",
  "source": "citation or local note",
  "redistribution": "local only"
}
```

The scripts accept any UTF-8 `.txt` files.

For the local historical Exodus-corpus workflow used to generate the hosted GitHub Pages figures, see [docs/historical_corpus_workflow.md](docs/historical_corpus_workflow.md).

If the private historical corpus and local manifests are present on this machine, regenerate the hosted figures with:

```bash
bash scripts/run_historical_figures.sh
```

## 5. Offline Model Cache

After the sentence-transformer model has been downloaded once, you can avoid network checks by adding:

```bash
--local-files-only
```

## 6. What This Demo Does Not Claim

The demo reproduces the workflow, not the exact paper figures. The historical figures were exploratory and depended on local notebook state, corpus availability, random sampling, and manually exported Plotly images.

Some paper texts may not be redistributable. The public implementation therefore uses sample texts and lets users supply their own local corpus.

## 7. Basic Tests

```bash
python -m unittest discover -s tests
```
