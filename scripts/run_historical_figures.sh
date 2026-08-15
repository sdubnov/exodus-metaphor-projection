#!/usr/bin/env bash
set -euo pipefail

PYTHON="${PYTHON:-.venv/bin/python}"

"$PYTHON" scripts/run_metaphor_projection_demo.py \
  --anchors data/anchors/berlin_liberty_anchor_pairs.csv \
  --manifest local_manifests/religious.local.json \
  --output docs/figures/religious_metaphor_projection.html \
  --seed 42 \
  --epochs 250 \
  --local-files-only \
  --max-chunks-per-text 300 \
  --hide-hover-text

"$PYTHON" scripts/run_metaphor_projection_demo.py \
  --anchors data/anchors/berlin_liberty_anchor_pairs.csv \
  --manifest local_manifests/modern.local.json \
  --output docs/figures/modern_metaphor_projection.html \
  --seed 42 \
  --epochs 250 \
  --local-files-only \
  --max-chunks-per-text 300 \
  --hide-hover-text

"$PYTHON" scripts/run_3d_baseline_demo.py \
  --manifest local_manifests/full.local.json \
  --output docs/figures/embedding_baseline_3d.html \
  --seed 42 \
  --local-files-only \
  --max-chunks-per-text 300 \
  --hide-hover-text
