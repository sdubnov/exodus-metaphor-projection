"""Small contrastive projection model."""

from __future__ import annotations


def _torch():
    import torch
    import torch.nn as nn
    import torch.nn.functional as F

    return torch, nn, F


def get_device(device_name: str | None = None):
    torch, _, _ = _torch()
    if device_name:
        return torch.device(device_name)
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def make_projector(input_dim: int = 384, projection_dim: int = 2):
    _, nn, _ = _torch()
    return nn.Sequential(
        nn.Linear(input_dim, 256),
        nn.ReLU(),
        nn.Linear(256, projection_dim),
    )


def train_contrastive_projector(
    anchor_embeddings,
    positive_embeddings,
    epochs: int = 250,
    learning_rate: float = 1e-3,
    projection_dim: int = 2,
    seed: int | None = None,
    device_name: str | None = None,
):
    torch, _, F = _torch()
    if seed is not None:
        torch.manual_seed(seed)

    device = get_device(device_name)
    anchors = anchor_embeddings.clone().detach().to(device)
    positives = positive_embeddings.clone().detach().to(device)
    model = make_projector(anchors.shape[1], projection_dim).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    labels = torch.arange(anchors.shape[0], device=device)

    for _ in range(epochs):
        model.train()
        projected_anchors = model(anchors)
        projected_positives = model(positives)
        similarity = F.cosine_similarity(
            projected_anchors.unsqueeze(1),
            projected_positives.unsqueeze(0),
            dim=-1,
        )
        loss = F.cross_entropy(similarity, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    model.eval()
    return model
