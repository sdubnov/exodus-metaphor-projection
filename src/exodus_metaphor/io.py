"""Manifest and corpus loading."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from .chunking import smart_paragraph_split


@dataclass(frozen=True)
class CorpusEntry:
    label: str
    path: Path
    source: str = ""
    redistribution: str = ""


@dataclass(frozen=True)
class LoadedText:
    entry: CorpusEntry
    chunks: list[str]


def load_manifest(path: str | Path) -> list[CorpusEntry]:
    manifest_path = Path(path)
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    base_dir = manifest_path.parent
    entries = []
    for item in data.get("entries", []):
        label = str(item.get("label", "")).strip()
        rel_path = str(item.get("path", "")).strip()
        if not label or not rel_path:
            continue
        file_path = Path(rel_path)
        if not file_path.is_absolute():
            file_path = base_dir / file_path
        entries.append(
            CorpusEntry(
                label=label,
                path=file_path,
                source=str(item.get("source", "")).strip(),
                redistribution=str(item.get("redistribution", "")).strip(),
            )
        )
    if not entries:
        raise ValueError(f"No corpus entries found in {manifest_path}")
    return entries


def load_corpus(entries: list[CorpusEntry], min_chars: int = 50) -> list[LoadedText]:
    loaded = []
    missing = []
    for entry in entries:
        if not entry.path.exists():
            missing.append(str(entry.path))
            continue
        text = entry.path.read_text(encoding="utf-8")
        chunks = smart_paragraph_split(text, min_chars=min_chars)
        if chunks:
            loaded.append(LoadedText(entry=entry, chunks=chunks))

    if missing:
        print("Warning: skipped missing corpus files:")
        for path in missing:
            print(f"  - {path}")
    if not loaded:
        raise ValueError("No corpus text could be loaded.")
    return loaded
