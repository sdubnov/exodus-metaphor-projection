# Run The Exodus Metaphor Projection Demo

## 1. Create Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Run The Semantic Baseline

```bash
python scripts/run_baseline_demo.py \
  --manifest corpus_manifest.example.json \
  --output outputs/figures/semantic_baseline.html \
  --seed 42
```

Expected result:

- chunk counts printed in the terminal
- `outputs/figures/semantic_baseline.html`

Optional 3D baseline:

```bash
python scripts/run_3d_baseline_demo.py \
  --manifest corpus_manifest.example.json \
  --output outputs/figures/semantic_baseline_3d.html \
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

The demo reproduces the workflow, not the exact paper figures. The historical figures were exploratory and depended on local notebook state, random sampling, and manually exported Plotly images.

Some paper texts may not be redistributable. The public implementation therefore uses sample texts and lets users supply their own local corpus.

## 7. Basic Tests

```bash
python -m unittest discover -s tests
```
