def compute_score(level, attempts):
    base = 100
    if attempts <= 1:
        return {"stars": 3, "xp": base + 40}
    if attempts <= 3:
        return {"stars": 2, "xp": base + 20}
    return {"stars": 1, "xp": base}
