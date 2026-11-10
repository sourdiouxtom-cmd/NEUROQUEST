from collections import deque


class Graph:
    def __init__(self, graph_dict=None):
        self.graph = graph_dict or {}

    def neighbors(self, node):
        return self.graph.get(node, [])

    def bfs_shortest_path(self, start, goal):
        queue = deque([start])
        previous = {start: None}

        while queue:
            current = queue.popleft()
            if current == goal:
                break
            for neighbor in self.neighbors(current):
                if neighbor not in previous:
                    previous[neighbor] = current
                    queue.append(neighbor)

        if goal not in previous:
            return []

        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        return path

    def dfs_path(self, start, goal, visited=None):
        if visited is None:
            visited = set()
        if start == goal:
            return [start]
        visited.add(start)
        for neighbor in self.neighbors(start):
            if neighbor in visited:
                continue
            result = self.dfs_path(neighbor, goal, visited)
            if result:
                return [start] + result
        return []
