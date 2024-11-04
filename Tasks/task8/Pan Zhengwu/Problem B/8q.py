class NQueensPipeFilter:
    """Solve the n queens puzzle using a Pipes-and-Filters architecture"""
    
    def __init__(self, size):
        self.size = size
        self.solutions = 0  # Track the number of solutions
    
    # Filter 1: Initialize Positions
    def initialize_positions(self):
        """Initialize an empty positions list for the board"""
        yield [-1] * self.size  # Each row is initially empty (-1)

    # Filter 2: Place Queen
    def place_queen(self, board_stream, target_row=0):
        """Attempts to place queens row by row"""
        for positions in board_stream:
            if target_row == self.size:
                yield positions  # Pass complete solution downstream
            else:
                for column in range(self.size):
                    if self.check_place(positions, target_row, column):
                        new_positions = positions[:]
                        new_positions[target_row] = column
                        yield from self.place_queen([new_positions], target_row + 1)
    
    # Filter 3: Check Validity
    def check_place(self, positions, occupied_rows, column):
        """
        Checks if placing a queen at the given row and column is safe.
        """
        for i in range(occupied_rows):
            if positions[i] == column or \
                positions[i] - i == column - occupied_rows or \
                positions[i] + i == column + occupied_rows:
                return False
        return True

    # Filter 4: Collect Solutions
    def collect_solutions(self, solutions_stream):
        """
        Collects and counts valid solutions.
        """
        solutions = []
        for solution in solutions_stream:
            solutions.append(solution)
            self.solutions += 1
            yield solution  # Pass each solution downstream
        return solutions

    # Filter 5: Display Solution
    def display_solutions(self, solutions_stream):
        """
        Display each valid solution on an 8x8 board.
        """
        for positions in solutions_stream:
            print("Solution:")
            for row in range(self.size):
                line = ""
                for column in range(self.size):
                    line += "Q " if positions[row] == column else ". "
                print(line)
            print("\n")

    def solve(self):
        """Pipeline setup to solve the N-Queens problem using the filter chain"""
        initial_stream = self.initialize_positions()  # Start with an empty board
        candidate_stream = self.place_queen(initial_stream)  # Generate candidates
        solutions_stream = self.collect_solutions(candidate_stream)  # Collect valid solutions
        self.display_solutions(solutions_stream)  # Display solutions
        print(f"Found {self.solutions} solutions.")

n_queens = NQueensPipeFilter(8)
n_queens.solve()
