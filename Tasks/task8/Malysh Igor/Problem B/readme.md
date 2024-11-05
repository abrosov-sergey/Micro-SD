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



# Comparision with [Pan Zhengwu](https://github.com/abrosov-sergey/Micro-SD/tree/main/Tasks/task8/Pan%20Zhengwu/Problem%20B)


# Comparison of Eight Queens Solutions

| Criteria                                    | Main/Subroutine Solution                          | Pipes-and-Filters Solution                    | Explanation                                                                                                                                                                    |
|---------------------------------------------|--------------------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **a) Ease of Changing Implementation**      | High                                             | Moderate                                      | The Main/Subroutine approach is modular, making it easier to adjust specific subroutines without affecting others. In the Pipes-and-Filters solution, each filter serves a specific function, allowing for straightforward modification, but changes must maintain data flow integrity. |
| **b) Ease of Changing Data Representation** | High                                             | Moderate                                      | The Main/Subroutine solution offers higher flexibility in changing the representation due to its encapsulated state. Both solutions represent queen positions using lists, but in the Pipes-and-Filters solution, any change in data structure requires updates across multiple filters. |
| **c) Ease of Adding Functions**             | Moderate                                        | High                                          | In the Main/Subroutine method, adding new functions may require altering multiple related subroutines. The Pipes-and-Filters architecture facilitates the addition of new filters for functionality without disrupting existing ones. |
| **d) Performance**                          | Moderate                                        | Moderate                                      | Both solutions utilize backtracking, which introduces inherent complexity. The Main/Subroutine method may have overhead due to function calls and checks, while the Pipes-and-Filters approach may have slight performance overhead from inter-filter data passing. |
| **e) Reusability Preference**               | Moderate                                        | High                                          | The Main/Subroutine solution is more tailored to the specific 8Q problem, which may limit its adaptability to other contexts without substantial modification. The Pipes-and-Filters solution is highly reusable across different problems, as filters can be easily adapted for various constraint-based puzzles. |

## Justifications

- **Ease of Changing Implementation**: In the Main/Subroutine solution’s structure allows for easy changes within specific routines, providing high modularity. In the Pipes-and-Filters solution, each filter has a defined role, allowing for independent adjustments; however, the need to maintain a coherent data flow can complicate modifications.

- **Ease of Changing Data Representation**: The Main/Subroutine approach allows for easy changes to the board state as it directly manipulates shared data. The Pipes-and-Filters solution, while still manageable, would require modifications across filters to ensure compatibility if the data representation changes.

- **Ease of Adding Functions**: The Main/Subroutine approach may require more extensive modifications when adding new functionality, particularly if it impacts multiple routines. The architecture of the Pipes-and-Filters solution enables the addition of new features (e.g., filters for specific logging or additional validations) without altering existing filters.

- **Performance**: Both solutions rely on backtracking, introducing similar levels of complexity. The Main/Subroutine method may face performance impacts due to the overhead of multiple function calls, while the Pipes-and-Filters method might incur slight overhead due to passing data through various filters.

- **Reusability**: The Main/Subroutine solution is more specific to the 8Q problem, which may limit its applicability without significant redesign for other problems. The modular design of the Pipes-and-Filters solution makes it easy to adapt for different constraint-based challenges, making it highly reusable.
