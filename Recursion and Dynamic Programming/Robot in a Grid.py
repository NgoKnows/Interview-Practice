maze = [[True, True, True, True],
        [True, True, True, True],
        [False, True, False, True],
        [True, False, True, True]]
def navigate_grid(maze):
    path = []
    check_path(maze, path = path)
    return path


def check_path(maze, position = None, path = None, cache = None):
    if cache is None:
        cache = dict()

    if position is None:
        position = (0, 0)

    if path is None:
        path = []

    rows = len(maze) - 1
    cols = len(maze[0]) - 1
    if position[0] > rows or position[1] > cols or not maze[position[0]][position[1]]:
        return False

    if position == (rows, cols):
        return True

    if check_path(maze, (position[0] + 1, position[1]), path):
        path.append('down')
        cache[position] = (True, 'down')
        return True
    elif check_path(maze, (position[0], position[1] + 1), path):
        path.append('right')
        cache[position] = (True, 'down')
        return True
    else:
        return False

    return path

print(navigate_grid(maze))