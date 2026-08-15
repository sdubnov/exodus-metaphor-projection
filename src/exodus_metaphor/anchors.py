"""Anchor-pair loading."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AnchorPair:
    anchor: str
    positive: str
    notes: str = ""


def load_anchor_pairs(path: str | Path) -> list[AnchorPair]:
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {"anchor", "positive"}
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Anchor CSV is missing required columns: {sorted(missing)}")

        pairs = [
            AnchorPair(
                anchor=(row.get("anchor") or "").strip(),
                positive=(row.get("positive") or "").strip(),
                notes=(row.get("notes") or "").strip(),
            )
            for row in reader
        ]

    pairs = [pair for pair in pairs if pair.anchor and pair.positive]
    if not pairs:
        raise ValueError(f"No valid anchor pairs found in {path}")
    return pairs
