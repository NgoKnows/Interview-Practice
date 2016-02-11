from collections import deque

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def bfs(graph, start):
    visited = set()
    visited_list = []
    q = deque([start])

    while len(q):
        vertex = q.pop()
        if vertex not in visited:
            visited.add(vertex)
            visited_list.append(vertex)

        q.extendleft(graph[vertex] - visited)
    return visited_list

print(bfs(graph, 'A'))