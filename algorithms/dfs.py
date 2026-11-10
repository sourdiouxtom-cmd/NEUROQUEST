from algorithms.graph import Graph


def shortest_path(graph, start, goal):
    return Graph(graph).bfs_shortest_path(start, goal)


def path_exists(graph, start, goal):
    return bool(shortest_path(graph, start, goal))
