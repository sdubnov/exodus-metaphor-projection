"""Projection helpers."""

from __future__ import annotations

import random


def flatten_loaded_texts(loaded_texts, max_chunks_per_text: int | None = None, seed: int | None = None):
    rng = random.Random(seed)
    texts = []
    labels = []
    counts = {}
    for loaded in loaded_texts:
        chunks = list(loaded.chunks)
        if max_chunks_per_text is not None and len(chunks) > max_chunks_per_text:
            chunks = rng.sample(chunks, max_chunks_per_text)
        texts.extend(chunks)
        labels.extend([loaded.entry.label] * len(chunks))
        counts[loaded.entry.label] = len(chunks)
    return texts, labels, counts


def project_embeddings(projector, embeddings, device_name: str | None = None):
    import torch

    if device_name:
        device = torch.device(device_name)
    else:
        device = next(projector.parameters()).device
    with torch.no_grad():
        return projector(embeddings.to(device)).detach().cpu().numpy()
