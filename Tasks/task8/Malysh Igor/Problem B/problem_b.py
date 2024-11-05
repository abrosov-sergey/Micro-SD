# Malysh Igor | Task 8 | Problem B | Method 2: Main/Subroutine with stepwise refinement (also Shared Data)


N = 8
board = [-1] * N
solutions = []


def solve(row):
    """
    Recursive function to place queens on the board, one row at a time.
    :param row: Current row to place the queen
    """
    if row == N:
        add_solution()
    else:
        for col in range(N):
            if is_safe(row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1


def is_safe(row, col):
    """
    Check if placing a queen at (row, col) is safe from attack.
    :param row: Row to place the queen
    :param col: Column to place the queen
    :return: True if safe, False otherwise
    """
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def add_solution():
    """
    Add the current board configuration to the solutions list.
    """
    solution = []
    for i in range(N):
        row = ["."] * N
        row[board[i]] = "Q"
        solution.append("".join(row))
    solutions.append(solution)


def print_solutions():
    """
    Print all valid solutions for the Eight Queens problem.
    """
    print(f"Total Solutions: {len(solutions)}")
    for index, solution in enumerate(solutions):
        print(f"\nSolution {index + 1}:")
        for row in solution:
            print(row)


def main():
    """Main function to start the Eight Queens solver."""
    solve(0)
    print_solutions()


main()
