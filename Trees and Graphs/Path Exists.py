from collections import deque

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def path_exists(graph, start, goal):
    queue = deque([(start, [start])])

    while len(queue):
        (vertex, path) = queue.pop()
        for next_vertex in graph[vertex] - set(path):
            if next_vertex == goal:
                return True
            else:
                queue.appendleft((next_vertex, path + [next_vertex]))
    return False
print(path_exists(graph, 'D', 'D'))