#!/usr/bin/env python3
"""Run a semantic embedding baseline demo."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from exodus_metaphor.embeddings import embed_texts, load_sentence_model
from exodus_metaphor.io import load_corpus, load_manifest
from exodus_metaphor.plotting import write_scatter_html
from exodus_metaphor.projection import flatten_loaded_texts


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="corpus_manifest.example.json")
    parser.add_argument("--output", default="outputs/figures/semantic_baseline.html")
    parser.add_argument("--model", default="all-MiniLM-L6-v2")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--hide-hover-text", action="store_true")
    parser.add_argument("--max-chunks-per-text", type=int, default=80)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def main():
    args = parse_args()
    entries = load_manifest(args.manifest)
    loaded = load_corpus(entries)
    texts, labels, counts = flatten_loaded_texts(loaded, args.max_chunks_per_text, args.seed)

    print("Corpus chunks:")
    for label, count in counts.items():
        print(f"  {label}: {count}")

    model = load_sentence_model(args.model, local_files_only=args.local_files_only)
    embeddings = embed_texts(model, texts).detach().cpu().numpy()

    from sklearn.decomposition import PCA

    points = PCA(n_components=2, random_state=args.seed).fit_transform(embeddings)
    output = write_scatter_html(
        points,
        labels,
        texts,
        args.output,
        "Semantic Baseline: Sentence Embeddings + PCA",
        "PC1",
        "PC2",
        include_hover_text=not args.hide_hover_text,
    )
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
