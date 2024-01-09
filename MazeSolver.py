def solve_maze(maze, start, end, path=[]):
    row, col = start
    if start == end:
        return path + [(row, col)]
    if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == "⭕" and start not in path:
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = row + direction[0], col + direction[1]
            new_start = (new_row, new_col)
            new_path = solve_maze(maze, new_start, end, path + [(row, col)])
            if new_path:
                return new_path
    return None