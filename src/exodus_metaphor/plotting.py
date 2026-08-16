"""Plotting helpers."""

from __future__ import annotations

from pathlib import Path


COLOR_MAP = {
    "Narrative": "#1f77b4",
    "Philosophy": "#d62728",
    "Civic": "#2ca02c",
    "RedHerring": "#111111",
    "Exodus": "#1f77b4",
    "Surah": "#d62728",
    "Douglass": "#2ca02c",
    "MLK": "#9467bd",
    "Herzl": "#ff7f0e",
}

SYMBOL_MAP = {
    "Narrative": "circle",
    "Philosophy": "diamond",
    "Civic": "square",
    "RedHerring": "x",
    "Exodus": "circle",
    "Surah": "diamond",
    "Douglass": "square",
    "MLK": "cross",
    "Herzl": "x",
}


def write_scatter_html(
    points,
    labels,
    hover_texts,
    output_path: str | Path,
    title: str,
    x_label: str,
    y_label: str,
    include_hover_text: bool = True,
):
    import pandas as pd
    import plotly.express as px

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    frame_data = {
        "x": points[:, 0],
        "y": points[:, 1],
        "label": labels,
    }
    hover_data = None
    if include_hover_text:
        frame_data["text"] = [text[:280] for text in hover_texts]
        hover_data = ["text"]
    frame = pd.DataFrame(frame_data)
    fig = px.scatter(
        frame,
        x="x",
        y="y",
        color="label",
        symbol="label",
        color_discrete_map=COLOR_MAP,
        symbol_map=SYMBOL_MAP,
        hover_data=hover_data,
        title=title,
        height=650,
        width=900,
    )
    fig.update_layout(xaxis_title=x_label, yaxis_title=y_label)
    fig.write_html(output_path)
    return output_path


def write_scatter_3d_html(
    points,
    labels,
    hover_texts,
    output_path: str | Path,
    title: str,
    x_label: str,
    y_label: str,
    z_label: str,
    include_hover_text: bool = True,
):
    import pandas as pd
    import plotly.express as px

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    frame_data = {
        "x": points[:, 0],
        "y": points[:, 1],
        "z": points[:, 2],
        "label": labels,
    }
    hover_data = None
    if include_hover_text:
        frame_data["text"] = [text[:280] for text in hover_texts]
        hover_data = ["text"]
    frame = pd.DataFrame(frame_data)
    fig = px.scatter_3d(
        frame,
        x="x",
        y="y",
        z="z",
        color="label",
        symbol="label",
        color_discrete_map=COLOR_MAP,
        symbol_map=SYMBOL_MAP,
        hover_data=hover_data,
        title=title,
        height=700,
        width=950,
    )
    fig.update_layout(scene=dict(xaxis_title=x_label, yaxis_title=y_label, zaxis_title=z_label))
    fig.write_html(output_path)
    return output_path
