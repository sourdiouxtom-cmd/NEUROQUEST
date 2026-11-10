from algorithms.graph import Graph


def shortest_path(graph, start, goal):
    g = Graph(graph)
    return g.bfs_shortest_path(start, goal)


def path_exists(graph, start, goal):
    g = Graph(graph)
    return bool(g.bfs_shortest_path(start, goal))


def validate_path(graph, selection, start, goal):
    if not selection:
        return {"ok": False, "message": "Aucune connexion choisie.", "solution": []}
    if selection[0] != start:
        return {"ok": False, "message": "Le chemin doit commencer au neurone de départ.", "solution": []}
    if selection[-1] != goal:
        return {"ok": False, "message": "Le chemin ne parvient pas au neurone cible.", "solution": []}

    for index in range(len(selection) - 1):
        current = selection[index]
        next_node = selection[index + 1]
        if next_node not in graph.get(current, []):
            return {"ok": False, "message": "Une synapse est invalide : la connexion n'existe pas.", "solution": []}

    expected = shortest_path(graph, start, goal)
    if selection == expected:
        return {"ok": True, "message": "Chemin valide.", "solution": expected}

    if len(selection) == len(expected):
        return {"ok": False, "message": "Le chemin est possible, mais il n'est pas le plus fiable.", "solution": expected}

    return {"ok": False, "message": "Le chemin n'aboutit pas au bon réseau neuronal.", "solution": expected}


def score_level(level, selection):
    errors = 0
    expected = shortest_path(level["graph"], level["start"], level["goal"])
    if selection != expected:
        errors = abs(len(expected) - len(selection)) + 1

    xp = max(50, 200 - errors * 25)
    stars = 1
    if errors == 0 and len(selection) == len(expected):
        stars = 3
    elif errors <= 1:
        stars = 2

    return {"stars": stars, "xp": xp, "errors": errors}
