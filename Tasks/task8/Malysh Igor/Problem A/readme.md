# Malysh Igor | Task 8 | Problem A | Method 1: Abstract Data Types


# Key Word in Context (KWIC) Solution

This project implements a Key Word in Context (KWIC) index generator using modularization principles inspired by David Parnas’ approach to decomposing systems into modules. The program processes lines of text, generates all circular shifts of each line (with stop word filtering), sorts these shifts alphabetically, and displays a KWIC index.

## Modules

The solution is divided into five modules:<br/>

1. **Input**: Reads and stores lines of text.<br/>
2. **Circular Shift**: Generates all circular shifts for each line, excluding those that start with specified stop words.<br/>
3. **Alphabetizing**: Sorts the circular shifts alphabetically.<br/>
4. **Output**: Displays the KWIC index in alphabetical order.<br/>
5. **Master Control**: Coordinates the execution of all other modules.

## Getting Started

### Prerequisites

- Python 3.7 or later

### Installation

1. Clone or download this repository to your local machine.<br/>
2. Ensure you have Python 3 installed. Run `python --version` or `python3 --version` in your terminal to verify.

## Running the Solution

### How to Execute the Script

1. Ensure that the `problem_a.py` file is saved in your project folder.<br/>
2. Open a terminal or command prompt and navigate to the project folder.<br/>
3. Run the script with the following command:
   ```bash
   python3 problem_a.py


# Comparision with [Aleksandr Anisin](https://github.com/abrosov-sergey/Micro-SD/tree/main/Tasks/task8/aleksandr-anisin)


| Criteria                                       | Abstract Data Types Solution                                        | Main/Subroutine Solution                  | Explanation                                                                                                                                                                                                                     |
|------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **a) Ease of Changing Implementation**         | High                                                     | High                                                | Both solutions are modular, with distinct responsibilities for each processing step. Either solution can have individual parts modified without impacting others.                                                              |
| **b) Ease of Changing Data Representation**    | High                                                     | Moderate                                            | Abstract Data Types solution encapsulates data within classes, allowing easier changes to data representation in each class. In the Main/Subroutine Solution, data is shared across functions, which may require changes in multiple functions. |
| **c) Ease of Adding Functions**                | High                                                     | Moderate                                            | Additional functionality (e.g., more processing steps) can be added more easily in Abstract Data Types solution due to encapsulated Abstract Data Types. The Main/Subroutine Solution may require more refactoring to add new functionalities.                     |
| **d) Performance**                             | Moderate                                                 | Moderate                                            | Both solutions involve multiple steps of processing data through modular functions/classes, introducing similar levels of computational overhead.                                                                               |
| **e) Reusability Preference**                  | High                                                     | Moderate                                            | Abstract Data Types-based structure and encapsulated classes offer greater reusability for other text-processing tasks, while main/subroutine structure could be adapted but with less flexibility.           |

### Justifications

1. **Ease of Changing Implementation**: Both solutions achieve modularity, making it possible to alter individual components (like shifting or sorting) without affecting the rest of the program. Abstract Data Types solution leverages object-oriented principles for modularity, while Main/Subroutine solution uses function-based modularity, which is similarly flexible for changes.

2. **Ease of Changing Data Representation**: Abstract Data Types solution encapsulates data within specific classes (`CircularShift` and `Alphabetizer`), making it easier to modify data structures within each Abstract Data Types without affecting other parts. In the Main/Subroutine solution, data is passed between functions, requiring careful coordination if any change is made to data representation across functions.

3. **Ease of Adding Functions**: With the Abstract Data Types approach, adding new functionality (e.g., filtering certain shifts or adding advanced sorting) is simpler due to encapsulated methods and properties. In the Main/Subroutine approach, adding new functionality could be more complex, as it may require changes across multiple interdependent functions.

4. **Performance**: Both solutions achieve similar performance, with the main difference being method of modularization. There’s slight overhead in both due to modularization, but neither implementation has a distinct advantage over the other in terms of speed.

5. **Reusability Preference**: The Abstract Data Types approach is more reusable in the sense that each class is self-contained and can be reused independently for other text processing applications. The Main/Subroutine solution also has reusable functions but may require adjustments if the problem or data structure changes significantly. 
