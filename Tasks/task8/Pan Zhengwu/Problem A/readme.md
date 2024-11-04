# Key Word in Context (KWIC) Solution

This project implements a Key Word in Context (KWIC) index generator using modularization principles described in David Parnas’ paper, On the Criteria To Be Used in Decomposing Systems into Modules. The program takes lines of text, generates all circular shifts of each line, sorts these shifts alphabetically, and displays a KWIC index.

## Modules

The solution is divided into five modules:

1.	Input Module: Reads and stores lines of text.
2.	Circular Shift Module: Generates all circular shifts for each line.
3.	Alphabetizing Module: Sorts circular shifts alphabetically.
4.	Output Module: Formats and displays the KWIC index.
4.5 A little module for stop word filteration. Not required, but I think its better to add for real life implementation.
5.	Master Control Module: Coordinates the execution of other modules.

## Getting Started

### Prerequisites

Python 3.11+

### Installation

1.	Clone or download this repository to your local machine.
2.	Ensure you have Python 3 installed. Run `python --version` or `python3 --version` in your terminal to check.

### Sample Input

1. input_phrases.txt
Input phrases, seperated by line.
```
KWIC is an acronym for Key Word In Context
the most common format for concordance lines
Wikipedia is the free encyclopedia
```

2. stop_words.txt
Input phrases, seperated by line.
```
the
is
an
for
in
and
a
```

### Running the Solution

1.	Save the kwic.py file to your project folder.
2.  Make sure that input_phrases.txt and stop_word.txt has phrase amd word in it. Seperated by line. Example input a showed in correspond file. 
2.	Open a terminal and navigate to the project folder.
3.	Run the program with the command:
```bash
python kwic.py
# or
python3 kwic.py
```


# Comparision with [aleksandr-anisin](https://github.com/abrosov-sergey/Micro-SD/tree/main/Tasks/task8/aleksandr-anisin)

| Criteria | My Main/Subroutine Solution | Teammate’s Main/Subroutine Solution| Explanation|
|--|--|--|--|
| **a) Ease of Changing Implementation**      | High | High | Both solution has functions with distinct responsibilities for each processing step|
| **b) Ease of Changing Data Representation** | High| High| My solution uses more modular data handling, but changes in representation may need adjustments across functions. The teammate’s solution, which processes lists directly without needing data transformation between functions, allows simpler modifications to data representation. |
| **c) Ease of Adding Functions**             | High | High | Both solution’s modular structure allows for easier integration of new features |
| **d) Performance**                          | Moderate | Moderate | Both solution passes data through several modular steps, introducing slight overhead|
| **e) Reusability Preference**               | High | High | Both solution’s clear modular separation of steps (input processing, shifting, sorting) makes it easier to adapt to similar text processing tasks. |

Justifications

As we use the same approach, there is not much to say.

# Comparision with 