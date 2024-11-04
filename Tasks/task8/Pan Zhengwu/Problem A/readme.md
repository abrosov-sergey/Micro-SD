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

## Task A (KWIC)

| Criteria | My Main/Subroutine Solution | Teammate’s Main/Subroutine Solution| Explanation|
|--|--|--|--|
| **a) Ease of Changing Implementation**      | High | High | Both solution has functions with distinct responsibilities for each processing step|
| **b) Ease of Changing Data Representation** | High| High| My solution uses more modular data handling, but changes in representation may need adjustments across functions. The teammate’s solution, which processes lists directly without needing data transformation between functions, allows simpler modifications to data representation. |
| **c) Ease of Adding Functions**             | High | High | Both solution’s modular structure allows for easier integration of new features |
| **d) Performance**                          | Moderate | Moderate | Both solution passes data through several modular steps, introducing slight overhead|
| **e) Reusability Preference**               | High | High | Both solution’s clear modular separation of steps (input processing, shifting, sorting) makes it easier to adapt to similar text processing tasks. |

Justifications

As we use the same approach, there is not much to say.

## Task B (8Q)

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


# Comparision with 