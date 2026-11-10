import json
from pathlib import Path

LEVEL_DIR = Path(__file__).resolve().parents[1] / "levels"


def load_levels():
    levels = []
    for file in sorted(LEVEL_DIR.glob("level_*.json")):
        with open(file, "r", encoding="utf-8") as f:
            levels.append(json.load(f))
    return levels


def get_level(level_id):
    path = LEVEL_DIR / f"level_{level_id:02d}.json"
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
