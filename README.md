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

python scripts/run_metaphor_projection_demo.py \
  --anchors data/anchors/berlin_liberty_anchor_pairs.csv \
  --manifest corpus_manifest.example.json \
  --output outputs/figures/metaphor_projection.html \
  --seed 42
```

## Analysis Example

After running the demo scripts, see [docs/analysis_example.md](docs/analysis_example.md) for an interpretation guide. A local HTML walkthrough is available at [docs/analysis_example.html](docs/analysis_example.html), but the embedded interactive plots require generated files in `outputs/figures/`.

GitHub's normal file viewer does not execute HTML or Plotly. For online interactive viewing, enable GitHub Pages for this repository using the `main` branch and `/docs` folder, then open:

- <https://sdubnov.github.io/exodus-metaphor-projection/analysis_example.html>
- <https://sdubnov.github.io/exodus-metaphor-projection/figures/semantic_baseline_3d.html>
- <https://sdubnov.github.io/exodus-metaphor-projection/figures/religious_metaphor_projection.html>
- <https://sdubnov.github.io/exodus-metaphor-projection/figures/modern_metaphor_projection.html>

The hosted figures use the local Exodus research corpus but hide passage hover text to avoid redistributing source texts that may not be licensed for republication. Running the code on the limited sample data included in this repository will verify the workflow, but it will not reproduce the hosted Exodus-corpus figures. See [docs/historical_corpus_workflow.md](docs/historical_corpus_workflow.md) for the exact commands used to generate them.

## Related Presentation

[![Exodus II presentation video](https://img.youtube.com/vi/7ndC6G7HyCU/hqdefault.jpg)](https://www.youtube.com/live/7ndC6G7HyCU)

Click the image to open the Exodus II presentation video.

## Scope

The included sample corpus is small and synthetic. To analyze the historical Exodus/Berlin corpus or another research corpus, provide your own local text files through a corpus manifest. See [docs/corpus_notes.md](docs/corpus_notes.md) and [docs/historical_corpus_workflow.md](docs/historical_corpus_workflow.md).

Some texts used in the exploratory paper study may not be redistributable. This repository therefore includes scripts, anchor files, and sample texts rather than the full historical corpus.

## Historical Corpus Access

Due to copyright and licensing restrictions, the complete historical corpus is not publicly redistributed with this code repository. Researchers interested in reproducing or extending the historical corpus analysis may contact Shlomo Dubnov at <sdubnov@ucsd.edu>.

Requests will be handled case by case. Where redistribution is not permitted, the repository provides corpus manifests, source notes, and scripts so that researchers can reconstruct comparable analyses from legally obtained copies of the relevant texts.

## Repository Layout

```text
data/anchors/       editable metaphor anchor pairs
data/private_corpus/ ignored local historical texts, if supplied by the user
data/sample_corpus/ small synthetic corpus for smoke tests
docs/               method, corpus, and analysis notes
scripts/            command-line demos
src/exodus_metaphor reusable implementation modules
tests/              lightweight tests
```

Historical-corpus manifest templates are provided as `corpus_manifest.exodus.*.local.example.json`. They are examples only; complete private text files should remain outside Git unless their redistribution status has been verified.

## Citation

See [CITATION.cff](CITATION.cff). The paper citation can be added after publication details are final.
