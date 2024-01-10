import random
from colorama import Fore, Style  # Import necessary modules from colorama


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

def print_solution(solution, maze):
    if solution:
        print(Fore.GREEN + "\nSolution:" + Style.RESET_ALL)
        for i in range(len(maze)):
            print("+ ---" * len(maze[0]) + " +")
            for j in range(len(maze[0])):
                if (i, j) == solution[0]:  # Starting point
                    print("|", Fore.GREEN + " S ", end=" " + Style.RESET_ALL)  # Print "S" in green color
                elif (i, j) == solution[-1]:  # End point
                    print("|", Fore.RED + " E ", end=" " + Style.RESET_ALL)  # Print "E" in red color
                elif (i, j) in solution:
                    print("|", Fore.CYAN + "🟢" + Style.RESET_ALL, end=" ")
                elif maze[i][j] == "⭕":
                    print("|", Fore.WHITE + "⭕" + Style.RESET_ALL, end=" ")
                elif maze[i][j] == "▓":
                    print("|", Fore.YELLOW + "▓ " + Style.RESET_ALL, end=" ")
                else:
                    print("|", end=" ")
            print("|")
        print("+ ---" * len(maze[0]) + " +")
        print(Fore.CYAN + f"\nNumber of steps taken to solve the maze: {len(solution) - 1}" + Style.RESET_ALL)

    else:
        print("No solution found")


def create_random_maze(n):
    maze = [["⭕" for _ in range(n)] for _ in range(n)]

    # Add walls
    wall_percentage = 25
    num_walls = int((n * n * wall_percentage) / 100)

    for _ in range(num_walls):
        row, col = random.randint(0, n - 1), random.randint(0, n - 1)
        maze[row][col] = "▓"

    return maze


def print_maze(maze):
    print(Fore.WHITE + "Maze:" + Style.RESET_ALL)
    for i in range(len(maze)):
        print("+ ---" * len(maze[0]) + " +")
        for j in range(len(maze[0])):
            if maze[i][j] == "⭕":
                print("|", Fore.WHITE + "⭕" + Style.RESET_ALL, end=" ")
            elif maze[i][j] == "▓":
                print("|", Fore.YELLOW + "▓ " + Style.RESET_ALL, end=" ")
            else:
                print("|", end=" ")
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
            n = int(input("Enter the number of rows and columns for the maze (n): "))
            maze_data = create_random_maze(n)

            print("\n" + Fore.WHITE + "Original Maze:" + Style.RESET_ALL)
            print_maze(maze_data)

            start_point = (0, 0)
            end_point = (n - 1, n - 1)

            solution = solve_maze(maze_data, start_point, end_point)

            print("\n" + Fore.WHITE + "Maze with Solution:" + Style.RESET_ALL)
            print_solution(solution, maze_data)

        elif choice == "2":
            if not maze_data:
                print("Please create a maze first (Option 1).")
            else:
                print_solution(solution, maze_data)

        elif choice == "3":
            n = int(input("Enter the number of rows and columns for the new maze (n): "))
            maze_data = create_random_maze(n)

            print("\n" + Fore.WHITE + "Original Maze:" + Style.RESET_ALL)
            print_maze(maze_data)

            start_point = (0, 0)
            end_point = (n - 1, n - 1)

            solution = solve_maze(maze_data, start_point, end_point)

            print("\n" + Fore.WHITE + "Maze with Solution:" + Style.RESET_ALL)
            print_solution(solution, maze_data)

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print(Fore.RED + "Invalid choice. Please enter 1, 2, 3, or 4." + Style.RESET_ALL)
