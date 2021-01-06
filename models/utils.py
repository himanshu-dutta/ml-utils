import torch


def accuracy(outputs, labels):
    _, preds = torch.max(outputs, dim=1)
    _, labels = torch.max(labels, dim=1)
    return torch.tensor(torch.sum(preds == labels).item() / len(preds))
