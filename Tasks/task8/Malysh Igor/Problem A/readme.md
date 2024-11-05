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
