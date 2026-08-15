# Exodus Metaphor Projection

Reference implementation for an anchor-guided metaphor projection workflow developed for the chapter **"Mapping the Cultural Metaphors of Exodus: A Cross-Textual Contrastive Machine Learning Approach"**.

The chapter is part of the Springer volume **Exodus II in Transdisciplinary Perspectives**, edited by Thomas Schneider, Brad Sparks, Neil Smith, and Thomas Levy.

## Motivation

The Exodus narrative has become a durable cultural model for thinking about bondage, deliverance, law, covenant, and collective freedom. The chapter asks how computational text methods can help compare this narrative structure with philosophical and political texts that discuss liberty in different genres and historical settings.

This repository provides a small, reusable implementation of the chapter's core methodological idea: manually curated metaphor anchors can define an interpretable projection space in which passages from different texts can be compared. The goal is to support methodological transparency and experimentation, not to provide an exact reproduction archive for every exploratory figure in the chapter.

## What This Implements

- chunk plain-text corpora into passages
- embed passages with a sentence-transformer model
- define scholar-curated metaphor anchor pairs
- train a small contrastive projection network
- project additional texts into the learned metaphor space
- generate interactive HTML plots

## Quick Start

See [RUNME.md](RUNME.md).

Minimal run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python scripts/run_baseline_demo.py \
  --manifest corpus_manifest.example.json \
  --output outputs/figures/semantic_baseline.html \
  --seed 42

python scripts/run_metaphor_projection_demo.py \
  --anchors data/anchors/berlin_liberty_anchor_pairs.csv \
  --manifest corpus_manifest.example.json \
  --output outputs/figures/metaphor_projection.html \
  --seed 42
```

## Analysis Example

After running the demo scripts, see [docs/analysis_example.md](docs/analysis_example.md) for an interpretation guide. A local HTML walkthrough is available at [docs/analysis_example.html](docs/analysis_example.html), but the embedded interactive plots require generated files in `outputs/figures/`.

## Scope

The included sample corpus is small and synthetic. To analyze the historical Exodus/Berlin corpus or another research corpus, provide your own local text files through a corpus manifest. See [docs/corpus_notes.md](docs/corpus_notes.md).

Some texts used in the exploratory paper study may not be redistributable. This repository therefore includes scripts, anchor files, and sample texts rather than the full historical corpus.

## Repository Layout

```text
data/anchors/       editable metaphor anchor pairs
data/sample_corpus/ small synthetic corpus for smoke tests
docs/               method, corpus, and analysis notes
scripts/            command-line demos
src/exodus_metaphor reusable implementation modules
tests/              lightweight tests
```

## Citation

See [CITATION.cff](CITATION.cff). The paper citation can be added after publication details are final.
