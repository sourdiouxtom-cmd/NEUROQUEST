from algorithms.bfs import validate_path


def test_validate_path_ok():
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    response = validate_path(graph, ["A", "B", "D"], "A", "D")
    assert response["ok"] is True


def test_validate_path_fail():
    graph = {"A": ["B"], "B": ["C"], "C": []}
    response = validate_path(graph, ["A", "C"], "A", "C")
    assert response["ok"] is False
