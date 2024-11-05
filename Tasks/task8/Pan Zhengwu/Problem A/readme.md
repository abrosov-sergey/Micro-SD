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


# Comparision with [aleksandr-anisin](https://github.com/abrosov-sergey/Micro-SD/blob/main/Tasks/task8/aleksandr-anisin/t1-m2.py)

| Criteria | My Main/Subroutine Solution | Teammate’s Main/Subroutine Solution| Explanation|
|--|--|--|--|
| **a) Ease of Changing Implementation**      | High | High | Both solution has functions with distinct responsibilities for each processing step|
| **b) Ease of Changing Data Representation** | High| High| My solution uses more modular data handling, but changes in representation may need adjustments across functions. The teammate’s solution, which processes lists directly without needing data transformation between functions, allows simpler modifications to data representation. |
| **c) Ease of Adding Functions**             | High | High | Both solution’s modular structure allows for easier integration of new features |
| **d) Performance**                          | Moderate | Moderate | Both solution passes data through several modular steps, introducing slight overhead|
| **e) Reusability Preference**               | High | High | Both solution’s clear modular separation of steps (input processing, shifting, sorting) makes it easier to adapt to similar text processing tasks. |

Justifications

As we use the same approach, there is not much to say.

# Comparision with [Malysh Igor](https://github.com/abrosov-sergey/Micro-SD/tree/main/Tasks/task8/Malysh%20Igor/Problem%20A)

| Criteria                                    | Main/Subroutine Solution                    | Abstract Data Types Solution                  | Explanation                                                                                                                                                                    |
|--|---|--|--|
| **a) Ease of Changing Implementation**      | High                                        | Moderate                                      | The Main/Subroutine solution is broken into simple, sequential functions (e.g., `process_input`, `circular_shift`), making it easy to change specific steps without impacting other parts. The ADT solution requires modifying methods within class definitions, which may involve changes across interdependent classes if the design is tightly coupled. |
| **b) Ease of Changing Data Representation** | Moderate                                    | High                                          | The ADT solution encapsulates data in classes (e.g., `KWICIndex`, `Word`, `Context`), so changing data representation is more straightforward as it only affects specific class properties and methods. Main/Subroutine may require adjustments across functions that handle the data directly, making changes more effortful. |
| **c) Ease of Adding Functions**             | Moderate                                    | High                                          | ADT’s structure supports adding new methods to classes without affecting existing ones, providing flexibility. The Main/Subroutine solution is function-based and would require more restructuring to integrate new functionalities. |
| **d) Performance**                          | High                                        | Moderate                                      | Main/Subroutine functions directly manipulate data, reducing the overhead associated with complex class interactions. The ADT solution may have additional overhead due to class instantiation and method calls, making it slightly less performant for large inputs. |
| **e) Reusability Preference**               | Moderate                                    | High                                          | The ADT solution encapsulates related data and behaviors within reusable classes, making it ideal for reuse in similar indexing or text-processing applications. The Main/Subroutine solution is less reusable for diverse applications, as functions are tightly coupled to the KWIC process. |

## Justifications

- Ease of Changing Implementation: The Main/Subroutine solution isolates each step in a separate function, making it easier to adjust individual functions without impacting others. In ADT, modifying one class method could affect how other classes interact, potentially requiring more extensive adjustments.
- Ease of Changing Data Representation: ADT encapsulates data within specific classes, making it easier to change how data is represented (e.g., using different data structures within classes) without affecting the entire program. Main/Subroutine handles data directly in functions, so changing representation might require more adjustments across multiple functions.
- Ease of Adding Functions: The ADT approach provides high flexibility for adding new functionalities as new methods or classes without disrupting the existing structure. For Main/Subroutine, adding functions typically requires integrating them into an existing flow, which could involve additional restructuring.
- Performance: Main/Subroutine performs well because each function works directly on data without extra layers. ADT may introduce slight overhead due to class instantiation and complex method interactions, especially if the data size grows.
- Reusability: ADT structures are highly reusable, as classes can be repurposed in similar projects that require data encapsulation and modularity. Main/Subroutine is more specific to the KWIC flow, making it less adaptable for other projects without modification.
