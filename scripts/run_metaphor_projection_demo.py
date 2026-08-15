#!/usr/bin/env python3
"""Run the anchor-guided metaphor projection demo."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from exodus_metaphor.anchors import load_anchor_pairs
from exodus_metaphor.contrastive import train_contrastive_projector
from exodus_metaphor.embeddings import embed_texts, load_sentence_model
from exodus_metaphor.io import load_corpus, load_manifest
from exodus_metaphor.plotting import write_scatter_html
from exodus_metaphor.projection import flatten_loaded_texts, project_embeddings


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--anchors", default="data/anchors/berlin_liberty_anchor_pairs.csv")
    parser.add_argument("--manifest", default="corpus_manifest.example.json")
    parser.add_argument("--output", default="outputs/figures/metaphor_projection.html")
    parser.add_argument("--model", default="all-MiniLM-L6-v2")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--hide-hover-text", action="store_true")
    parser.add_argument("--epochs", type=int, default=250)
    parser.add_argument("--max-chunks-per-text", type=int, default=80)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def main():
    args = parse_args()
    anchor_pairs = load_anchor_pairs(args.anchors)
    print(f"Loaded {len(anchor_pairs)} anchor pairs.")

    entries = load_manifest(args.manifest)
    loaded = load_corpus(entries)
    texts, labels, counts = flatten_loaded_texts(loaded, args.max_chunks_per_text, args.seed)
    print("Corpus chunks:")
    for label, count in counts.items():
        print(f"  {label}: {count}")

    model = load_sentence_model(args.model, local_files_only=args.local_files_only)
    anchor_embeddings = embed_texts(model, [pair.anchor for pair in anchor_pairs])
    positive_embeddings = embed_texts(model, [pair.positive for pair in anchor_pairs])
    projector = train_contrastive_projector(
        anchor_embeddings,
        positive_embeddings,
        epochs=args.epochs,
        seed=args.seed,
    )

    corpus_embeddings = embed_texts(model, texts)
    points = project_embeddings(projector, corpus_embeddings)
    output = write_scatter_html(
        points,
        labels,
        texts,
        args.output,
        "Anchor-Guided Metaphor Projection",
        "Metaphor axis 1",
        "Metaphor axis 2",
        include_hover_text=not args.hide_hover_text,
    )
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
