"""Embedding helpers."""

from __future__ import annotations


def load_sentence_model(model_name: str = "all-MiniLM-L6-v2", local_files_only: bool = False):
    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(model_name, local_files_only=local_files_only)


def embed_texts(model, texts: list[str]):
    return model.encode(texts, convert_to_tensor=True)
