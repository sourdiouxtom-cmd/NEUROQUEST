from flask import Flask, render_template, request, jsonify, redirect
from database.database import init_db, get_progression, update_progression
from engine.levels import get_level, list_levels
from algorithms.bfs import shortest_path, validate_path, score_level

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/levels")
def levels_page():
    return render_template("levels.html", levels=list_levels())


@app.route("/game/<int:level_id>")
def game_page(level_id):
    level = get_level(level_id)
    if not level:
        return redirect("/levels")
    progress = get_progression()
    return render_template("game.html", level=level, progress=progress)


@app.route("/settings")
def settings_page():
    return render_template("settings.html")


@app.route("/encyclopedia")
def encyclopedia_page():
    return render_template("encyclopedia.html")


@app.route("/api/level/<int:level_id>")
def api_level(level_id):
    level = get_level(level_id)
    if not level:
        return jsonify({"error": "Niveau introuvable."}), 404
    return jsonify(level)


@app.route("/api/validate", methods=["POST"])
def validate_level():
    payload = request.get_json(force=True)
    level_id = int(payload.get("level_id", 1))
    selection = payload.get("selection", [])

    level = get_level(level_id)
    if not level:
        return jsonify({"ok": False, "message": "Niveau inconnu."}), 404

    result = validate_path(level["graph"], selection, level["start"], level["goal"])
    if result["ok"]:
        score = score_level(level, selection)
        update_progression(level_id, score["stars"], score["xp"])
        return jsonify({
            "ok": True,
            "message": "Connexion restaurée. Le réseau est stable.",
            "score": score,
            "solution": result["solution"]
        })

    return jsonify({
        "ok": False,
        "message": result["message"],
        "hint": level.get("hint", "Suivre les connexions les plus stables.")
    })


@app.route("/api/progression")
def progression_api():
    return jsonify(get_progression())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
