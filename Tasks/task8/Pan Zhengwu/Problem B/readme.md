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

# Comparision with [aleksandr-anisin](https://github.com/abrosov-sergey/Micro-SD/tree/main/Tasks/task8/aleksandr-anisin)


| Criteria                                    | Pipes-and-Filters Solution                    | Implicit Invocation (Event-Driven) Solution     | Explanation                                                                                                                                                                    |
|--|--|--|--|
| **a) Ease of Changing Implementation**      | Moderate                                      | High                                           | The Pipes-and-Filters solution has tightly structured filters, so changing logic within each filter is straightforward but requires maintaining data flow consistency. The Event-Driven solution is modular, with observer classes that can be modified independently, making it easy to change implementation details in response to events. |
| **b) Ease of Changing Data Representation** | Moderate                                      | Moderate                                       | Both solutions use a list-like structure to track queen positions, making changes to data representation manageable in either case. However, the Event-Driven solution might require additional updates to observer and board components if data handling changes. |
| **c) Ease of Adding Functions**             | High                                          | Moderate                                       | Pipes-and-Filters allows for independent addition of new filters (e.g., logging, additional checks) without altering existing filters. The Event-Driven solution could integrate new observers or notifications but might require additional modifications in the `Board` class for more complex interactions. |
| **d) Performance**                          | Moderate                                      | Moderate                                       | Both solutions use backtracking, which has inherent complexity. The Pipes-and-Filters approach has slight overhead from passing data between filters, while the Event-Driven solution can introduce overhead from observer checks, especially if additional observers are added. |
| **e) Reusability Preference**               | High                                          | Moderate                                       | The Pipes-and-Filters solution is highly reusable for other constraint-based puzzles by altering filters. The Event-Driven solution is specific to the observer pattern, which could be adaptable but may require more significant changes to the observer logic and board setup for different problems. |

Justifications

- **Ease of Changing Implementation**: In my Pipes-and-Filters solution, each filter has a specific task, which can be independently modified if necessary. However, because data flows sequentially through filters, changes must respect the data flow. The Event-Driven solution offers higher modularity, as observers like QueenObserver check the board state without altering it, making implementation changes straightforward.
- **Ease of Changing Data Representation**: Both solutions use lists to represent queen positions, and changes in representation are moderate for both. The Event-Driven solution may need updates across observers if queen position data is structured differently, while Pipes-and-Filters would require modifying the data format across filters.
- **Ease of Adding Functions**: In Pipes-and-Filters, new filters can be added without affecting existing filters, making it straightforward to add features. The Event-Driven solution could accommodate new observers or notifications, but more complex functions might need significant changes to the Board class to manage additional events.
- **Performance**: Both solutions involve backtracking and complexity due to constraints. The Event-Driven solution could slow down with multiple observers, especially if each observer performs complex calculations. The Pipes-and-Filters solution has minimal overhead due to data being passed between filters, but the difference in performance between the two is minor overall.
- **Reusability**: Pipes-and-Filters is generally more adaptable to different constraint-based puzzles, as filters can be replaced or modified independently. The Event-Driven solution’s observer pattern is specific to event handling, which makes it less adaptable for problems without an event-driven nature, as each observer and board relationship would require customization.