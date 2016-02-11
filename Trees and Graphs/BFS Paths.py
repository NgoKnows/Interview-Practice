from collections import deque

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def bfs_paths(graph, start, goal):
    q = deque([(start, [start])])

    while len(q):
        (vertex, path) = q.pop()

        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                q.appendleft((next, path + [next]))

gen = bfs_paths(graph, 'A', 'D')

print(next(gen))
