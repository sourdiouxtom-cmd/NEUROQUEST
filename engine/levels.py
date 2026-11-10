from pathlib import Path
import json

LEVEL_DIR = Path(__file__).resolve().parents[1] / "levels"


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def list_levels():
    levels = []
    for path in sorted(LEVEL_DIR.glob("level_*.json")):
        data = load_json(path)
        levels.append(data)
    return levels


def get_level(level_id):
    level_path = LEVEL_DIR / f"level_{level_id:02d}.json"
    if not level_path.exists():
        return None
    return load_json(level_path)
