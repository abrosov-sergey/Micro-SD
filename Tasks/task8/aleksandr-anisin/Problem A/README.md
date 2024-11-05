# Key Word in Context (KWIC)

This solution is based on **Method 2: Main/Subroutine with Stepwise Refinement**:

1. **Input Processing**: Reads and processes input text.
2. **Circular Shifting**: Generates all possible keyword-centered phrases.
3. **Alphabetical Sorting**: Sorts the keyword contexts alphabetically.
4. **Output Generation**: Displays the final sorted list.

## Comparison

| Criteria                                     | My Solution | Pan Z.'s Solution            | Igor M.'s Solution                |
|----------------------------------------------|----------------------------------------------|------------------------------------------------------------|--------------------------------------------------------|
| **Easier to change implementation**       | Moderate effort: Stepwise refinement is modular, but shared data may cause dependencies between modules. | Moderate: Modules are independent, making it easier to change specific functions. | Easier: Each function is encapsulated in a class, allowing focused changes within ADTs. |
| **Easier to change data representation**  | Moderate difficulty: Shared data structure limits flexibility in data representation. | Easier: Separate modules make it simpler to alter data within each module. | Easiest: ADT encapsulation provides full control over internal data formats within classes. |
| **Easier to add additional functions**    | Moderate: Functions can be added but may need adjustments to shared data structure. | Easier: Independent modules allow straightforward addition of new functions. | Easiest: ADTs enable easy addition by extending classes without impacting others. |
| **More performant**                       | Efficient: Focuses on basic operations but may slightly slow with more complex data interactions. | Similar: Module-based approach keeps performance consistent, but with some extra file I/O. | Potentially slower: ADTs can introduce overhead due to more objects and encapsulation. |
| **Preferred solution for reuse**          | Moderate: General-purpose, suitable for small to medium data sets. | Suitable: Modular design with clear division, ideal for extending to additional requirements. | Best: ADT-based approach is more extensible and ideal for building on the current solution. |

Igor's solution is the most adaptable and suitable for reuse, ideal for projects needing extensibility and changes. Pan's approach is straightforward and easy to modify, providing a solid foundation for modular adjustments. My solution offers efficiency and simplicity, particularly suited for smaller-scale applications with less need for frequent modifications.

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python 3 installed.

## Usage

1. Place your text in the `sample_text` variable in the following format:

    ```python
    sample_text = "The quick brown fox\njumps over the lazy dog"
    ```

2.	Run the program to see the keyword-in-context list sorted alphabetically.

    ```bash
    python t1-m2.py
    ```
