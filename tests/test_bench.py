"""Gate the verification claims in RESULTS.md."""

from bench import evaluate


def test_extraction_matches_goldset():
    r = evaluate.evaluate()
    assert r["extraction"]["f1"] == 1.0
    assert r["extraction"]["fp"] == 0
    assert r["extraction"]["fn"] == 0


def test_resolution_perfect():
    assert evaluate.evaluate()["resolution_accuracy"] == 1.0


def test_retrieval_precision_at_1():
    r = evaluate.evaluate()
    assert r["retrieval"]["precision_at_1"] == 1.0
    assert r["retrieval"]["mrr"] == 1.0


def test_determinism():
    assert evaluate.evaluate()["determinism"] is True
