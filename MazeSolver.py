import random




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


def create_random_maze(rows, cols):
    maze = [["⭕" for _ in range(cols)] for _ in range(rows)]

    # Add walls
    wall_percentage = 25
    num_walls = int((rows * cols * wall_percentage) / 100)

    for _ in range(num_walls):
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        maze[row][col] = "▓"

    return maze

def print_maze(maze):
    print("maze:")
    for i in range(len(maze)):
        print("+ ---" * len(maze[0]) + " +")
        for j in range(len(maze[0])):
            if maze[i][j] == "⭕":
                print("| ⭕", end=" ")
            elif maze[i][j] == "▓":
                print("| ▓ ", end=" ")
            else:
                print("| ", end=" ")
        print("|")
    print("+ ---" * len(maze[0]) + " +")


if __name__ == "__main__":
    maze_data = []

    while True:
        print("\nOptions:")
        print("1. Create random maze")
        print("2. Solve and display solution")
        print("3. Create and solve a new maze")
        print("4. Exit")

        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == "1":
            rows = int(input("Enter the number of rows for the maze: "))
            cols = int(input("Enter the number of columns for the maze: "))
            maze_data = create_random_maze(rows, cols)

            print("\nOriginal Maze:")
            print_maze(maze_data)

            start_point = (0, 0)
            end_point = (rows - 1, cols - 1)

            solution = solve_maze(maze_data, start_point, end_point)

            print("\nMaze with Solution:")
            print_solution(solution, maze_data)

        elif choice == "2":
            if not maze_data:
                print("Please create a maze first (Option 1).")
            else:
                print_solution(solution, maze_data)

        elif choice == "3":
            rows = int(input("Enter the number of rows for the new maze: "))
            cols = int(input("Enter the number of columns for the new maze: "))
            maze_data = create_random_maze(rows, cols)

            print("\nOriginal Maze:")
            print_maze(maze_data)

            start_point = (0, 0)
            end_point = (rows - 1, cols - 1)

            solution = solve_maze(maze_data, start_point, end_point)

            print("\nMaze with Solution:")
            print_solution(solution, maze_data)

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


pritn("final out put as complet the project");           