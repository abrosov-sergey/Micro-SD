# Eight Queens Puzzle Solution

This project solves the Eight Queens Puzzle using a Pipes-and-Filters architecture, where each filter performs an independent task. The goal of the Eight Queens Puzzle is to place eight queens on an 8x8 chessboard so that no two queens threaten each other. This implementation uses the Pipes-and-Filters style, providing modularity and independence for each processing step.

## Solution Structure

The solution is divided into five main filters:

1.	Initialize Positions: Sets up the initial empty positions list.
2.	Place Queen: Attempts to place queens row by row, checking column positions.
3.	Check Validity: Verifies that no two queens can attack each other.
4.	Collect Solutions: Collects valid board configurations as solutions.
5.	Display Solutions: Formats and displays each valid solution.

## Getting Started

### Prerequisites

- Python 3.11+

### Installation

1.	Clone or download this repository to your local machine.
2.	Ensure Python 3 is installed by running `python --version` or `python3 --version`  in your terminal.

### Running the Solution

1.	Save the nqueens_pipe_filter.py file to your project folder.
2.	Open a terminal and navigate to the project folder.
3.	Run the program with the following command: `python 8q.py` or `python3 8q.py` depence on the python you installed

## How It Works

### The solution applies a sequence of filters:

- Each filter acts independently, processing and passing data to the next filter.
- Data flows from Initialize Positions through to Display Solutions, with each filter performing a single task.

### Example Input

No input file is needed. The program initializes an empty board and begins placing queens.

### ample Output

After running the program, the console will display all valid solutions for the Eight Queens puzzle, along with the total count.

### Sample Output:

Solution:
```
Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . Q . . . . .
. . . . . Q . .
. Q . . . . . .
. . . Q . . . .
. . . . . . Q .

... (other solutions)

Found 92 solutions.
```

### Customization

To solve for a different board size (such as the 4x4 queens puzzle), change the size parameter in the main function:

n_queens = NQueensPipeFilter(4)
