"""Plotting helpers."""

from __future__ import annotations

from pathlib import Path


def write_scatter_html(points, labels, hover_texts, output_path: str | Path, title: str, x_label: str, y_label: str):
    import pandas as pd
    import plotly.express as px

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(
        {
            "x": points[:, 0],
            "y": points[:, 1],
            "label": labels,
            "text": [text[:280] for text in hover_texts],
        }
    )
    fig = px.scatter(
        frame,
        x="x",
        y="y",
        color="label",
        hover_data=["text"],
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
):
    import pandas as pd
    import plotly.express as px

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(
        {
            "x": points[:, 0],
            "y": points[:, 1],
            "z": points[:, 2],
            "label": labels,
            "text": [text[:280] for text in hover_texts],
        }
    )
    fig = px.scatter_3d(
        frame,
        x="x",
        y="y",
        z="z",
        color="label",
        hover_data=["text"],
        title=title,
        height=700,
        width=950,
    )
    fig.update_layout(scene=dict(xaxis_title=x_label, yaxis_title=y_label, zaxis_title=z_label))
    fig.write_html(output_path)
    return output_path
