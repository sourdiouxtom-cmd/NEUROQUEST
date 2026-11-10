import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "database" / "saves.db"


def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS progression (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT DEFAULT 'NEO',
            unlocked_level INTEGER DEFAULT 1,
            xp INTEGER DEFAULT 0,
            best_level INTEGER DEFAULT 1,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    cursor.execute(
        "SELECT COUNT(*) FROM progression WHERE id = 1"
    )
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO progression (player_name, unlocked_level, xp, best_level) VALUES (?, ?, ?, ?)",
            ("NEO", 1, 0, 1)
        )
    connection.commit()
    connection.close()


def get_progression():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    row = connection.execute("SELECT * FROM progression WHERE id = 1").fetchone()
    connection.close()
    if row is None:
        return {"player_name": "NEO", "unlocked_level": 1, "xp": 0, "best_level": 1}
    return dict(row)


def update_progression(level_id, stars, xp_amount):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    current = get_progression()
    unlocked = max(current["unlocked_level"], min(level_id + 1, 8))
    best_level = max(current["best_level"], level_id)
    xp = current["xp"] + xp_amount
    cursor.execute(
        "UPDATE progression SET unlocked_level = ?, xp = ?, best_level = ?, updated_at = CURRENT_TIMESTAMP WHERE id = 1",
        (unlocked, xp, best_level)
    )
    connection.commit()
    connection.close()
    return get_progression()
