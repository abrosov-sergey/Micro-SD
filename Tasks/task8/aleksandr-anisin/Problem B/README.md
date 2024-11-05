# Eight Queens (8Q)

This solution is based on **Method 4: Implicit Invocation (Event-Driven)**:

1. **Observer Pattern**: A `QueenObserver` validates board positions reactively.
2. **Event-Driven Placement**: `Board` triggers events when queens are added or removed, notifying observers asynchronously.
3. **Backtracking**: Uses a recursive approach to place queens while satisfying constraints.

## Comparison

| Criteria                                     | My Solution               | Pan Z.'s Solution                     | Igor M.'s Solution |
|----------------------------------------------|----------------------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------|
| **Easier to change implementation**       | Moderate: The event-driven design can handle changes to event triggers, but updating core logic requires adjustments across listeners and the board class. | Easiest: Each filter is independent, allowing isolated changes within each filter. | Moderate: Stepwise refinement allows modular changes, but shared data may create dependencies between functions. |
| **Easier to change data representation**  | Moderate: Event-driven design requires updating listeners if the board’s data structure changes. | Easiest: Data representation changes are isolated within filters without affecting the rest of the pipeline. | Moderate: Shared data structure may limit flexibility, as changing board format impacts all functions. |
| **Easier to add additional functions**    | Moderate: New event listeners or observers can be added, but core event handling may need modification to integrate additional features. | Easiest: Additional filters can be added to the pipeline without affecting existing filters, allowing extensibility. | Moderate: Functions can be added but may require adjustments to shared data, impacting other functions. |
| **More performant**                       | Moderate performance: Event-driven systems may have minor overhead due to asynchronous calls. | Slightly less performant: Pipes-and-filters design may add minor delays due to multiple filter processing stages. | Highest performance: Direct recursive and iterative steps reduce overhead, leading to faster execution. |
| **Preferred solution for reuse**          | Good for reuse: Event-driven design is flexible and allows component reuse, particularly for reactive or interactive programs. | Most reusable: Pipes-and-Filters allow new filters or configurations with minimal adjustments, ideal for modular expansions. | Suitable: Direct and efficient, suitable for scenarios where performance is prioritized over modular extensibility. |

Pan's solution offers the most flexibility for modular changes, data representation adjustments, and additional functions, making it ideal for extensible solutions. Igor's solution provides a highly efficient and direct implementation, well-suited for applications requiring performance optimization. My solution is suitable for reactive designs, offering reusability and adaptability, especially for event-based applications.

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python 3 installed.

## Usage

Run the program to solve the Eight Queens puzzle and print one valid solution:

    ```bash
    python eight_queens.py
    ```
