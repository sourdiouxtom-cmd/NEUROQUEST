from engine.scoring import compute_score


def test_score_stars():
    score = compute_score({"id": 1}, 1)
    assert score["stars"] >= 2
    assert score["xp"] > 0
