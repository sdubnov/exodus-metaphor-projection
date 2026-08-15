"""Text chunking utilities."""

from __future__ import annotations

import re


def smart_paragraph_split(text: str, min_chars: int = 50) -> list[str]:
    """Split plain text into paragraph-like chunks.

    The historical notebooks used a similar fallback sequence because corpus files
    varied in formatting.
    """
    text = text.replace("\r\n", "\n").replace("\r", "\n").strip()
    if not text:
        return []

    candidates = re.split(r"\n\s*\n", text)
    if len(candidates) <= 2:
        candidates = re.split(r"\n(?=\S)", text)
    if len(candidates) <= 2:
        candidates = re.split(r"(?<=[.!?])\s+(?=[A-Z])", text)

    chunks = [" ".join(part.split()) for part in candidates]
    return [chunk for chunk in chunks if len(chunk) >= min_chars]
