# Malysh Igor | Task 8 | Problem B | Method 2: Main/Subroutine with stepwise refinement (also Shared Data)


# Eight Queens (8Q) Problem Solution

This project solves the Eight Queens problem, where the goal is to place eight queens on an 8x8 chessboard such that no two queens threaten each other. The solution is implemented using the **Main/Subroutine method with stepwise refinement**, as well as **Shared Data** to store the board state and results.

## Problem Description

The Eight Queens problem requires placing eight queens on a chessboard so that:
- No two queens are in the same row, column, or diagonal.
- There are exactly eight queens on the board in a valid configuration.

This solution provides all possible configurations of the queens on the board.

## Solution Structure

The solution is divided into main subroutines:

1. **Main Function**: Initializes the solver and calls other functions to process and display results.
2. **Solve Function**: Recursively attempts to place queens row by row, ensuring no queens attack each other.
3. **Safety Check (is_safe)**: Checks that a queen placed at a specific row and column is not attacked by any previously placed queens.
4. **Add Solution**: Stores each valid configuration of queens as a list of strings, where each string represents a row.
5. **Print Solutions**: Outputs each solution in a human-readable format and displays the total number of solutions found.

## Getting Started

### Prerequisites

- Python 3.7 or later

### Installation

1. Clone or download this repository to your local machine.
2. Ensure you have Python 3 installed by running `python --version` or `python3 --version` in your terminal.

## Running the Solution

1. Save the `problem_b.py` file to your project folder.
2. Open a terminal or command prompt and navigate to the project folder.
3. Run the program with the command:
   ```bash
   python3 problem_b.py
