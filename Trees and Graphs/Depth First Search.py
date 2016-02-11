graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs_iterative(graph, start):
    visited = set()
    visited_list = []
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            visited_list.append(vertex)
            stack.extend(graph[vertex] - visited)
    return visited_list

print(dfs_iterative(graph, 'A'))

def dfs_recursive(graph, start, visited=None, visited_list=None):
    if visited is None:
        visited = set()
        visited_list = []
    visited.add(start)
    visited_list.append(start)

    for next in graph[start]:
        if next not in visited:
            dfs_recursive(graph, next, visited, visited_list)
    return visited_list

print(dfs_recursive(graph, 'A'))