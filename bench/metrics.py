"""Evaluation metrics (stdlib only)."""

from __future__ import annotations


def prf(pred, truth) -> dict:
    pred, truth = set(pred), set(truth)
    tp = len(pred & truth)
    fp = len(pred - truth)
    fn = len(truth - pred)
    p = tp / (tp + fp) if (tp + fp) else 1.0
    r = tp / (tp + fn) if (tp + fn) else 1.0
    f = (2 * p * r / (p + r)) if (p + r) else 0.0
    return {"precision": round(p, 4), "recall": round(r, 4), "f1": round(f, 4),
            "tp": tp, "fp": fp, "fn": fn}


def precision_at_k(ranked, relevant, k) -> float:
    topk = ranked[:k]
    return round(sum(1 for x in topk if x in relevant) / max(1, len(topk)), 4)


def recall_at_k(ranked, relevant, k) -> float:
    relevant = set(relevant)
    topk = set(ranked[:k])
    return round(len(topk & relevant) / max(1, len(relevant)), 4)


def mrr(ranked, relevant) -> float:
    relevant = set(relevant)
    for i, x in enumerate(ranked, 1):
        if x in relevant:
            return round(1 / i, 4)
    return 0.0
