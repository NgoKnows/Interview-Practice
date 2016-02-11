from collections import deque, defaultdict

def build_order(build_list, projects):
    dependency_graph = defaultdict(list)
    not_depended = set(projects)
    visited = set()
    project_list = []
    for dependency in build_list:
        dependency_graph[dependency[1]].append(dependency[0])
        if dependency[0] in not_depended:
            not_depended.remove(dependency[0])

    queue = deque()
    for project in not_depended:
        queue.appendleft(project)
        visited.add(project)

    while len(queue):
        current_project = queue.pop()

        project_list.append(current_project)
        for project in dependency_graph[current_project]:
            if project not in visited:
                queue.appendleft(project)
                visited.add(project)
    return project_list

print(build_order([('D', 'A'), ('B', 'F'), ('D','B'), ('A', 'F'), ('C', 'D')],
      set(['A', 'B', 'C', 'D','E', 'F'])))
