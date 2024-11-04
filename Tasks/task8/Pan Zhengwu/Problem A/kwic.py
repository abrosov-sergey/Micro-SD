# Module 1: Input
def input_module():
    """
    Reads input lines from 'input_phrases.txt' and stop words from 'stop_words.txt'.
    Returns a tuple:
    - line_storage: a list of lines from the input file.
    - index: an index showing the start position of each line.
    - stop_words: a set of stop words.
    """
    
    # Read stop words from "stop_words.txt" and store them in a set
    with open("stop_words.txt", "r") as f:
        stop_words = {line.strip().lower() for line in f if line.strip()}
    
    # Read lines from "input_phrases.txt" and store each line in a list
    line_storage = []
    index = []  # Stores start positions of each line
    with open("input_phrases.txt", "r") as f:
        for i, line in enumerate(f):
            cleaned_line = line.strip()
            if cleaned_line:  # Ensure the line is not empty
                line_storage.append(cleaned_line)
                index.append(i)  # Use line index as the starting address
    
    return line_storage, index, stop_words


# Module 2: Circular Shift
def circular_shift_module(lines, index):
    """
    Generates all circular shifts for each line.
    Returns a list of tuples with (original line index, shifted words).
    """
    shifts = []
    for line_num, start in enumerate(index):
        words = lines[start].split()
        for i in range(len(words)):
            shifted = words[i:] + words[:i]  # Perform circular shift
            shifts.append((line_num, shifted))  # Store with original line number
    return shifts

# Module 3: Alphabetizing
def alphabetizing_module(shifts):
    """
    Sorts the circular shifts alphabetically by the first word of each shift.
    Returns the sorted list of shifts.
    """
    return sorted(shifts, key=lambda shift: shift[1][0].lower())

# Module 4: Output
def output_module(sorted_shifts, lines):
    """
    Formats and outputs the KWIC index.
    Uses the original lines and sorted shifts for display.
    """
    output_lines = []
    for line_num, words in sorted_shifts:
        context = " ".join(words)
        original_line = lines[line_num]
        output_lines.append(f"index: {line_num}, {context}   (original line: {original_line})")
    return output_lines

# Module 4.5 Filter out rotations starting with stop words
def filters_shifts(rotations, stop_words):
    """
    Filter out rotations that start with a stop word.

    Args:
    - rotations: A list of rotations (list of lists).
    - stop_words: A set of words to exclude.
        
    Returns:
    - A list of valid rotations without stop words at the start.
    """
    return [rotation for rotation in rotations if rotation[1][0].lower() not in stop_words]

# Module 5: Master Control
def master_control():
    """
    Manages the overall sequence of operations for KWIC.
    Orchestrates the interaction between input, shift, alphabetize, and output modules.
    """
    # Step 1: Input Module
    line_storage, index, stop_words = input_module()
    
    # Step 2: Circular Shift Module
    shifts = circular_shift_module(line_storage, index)
    
    filtered_shifts = filters_shifts(shifts, stop_words)
    # Step 3: Alphabetizing Module
    sorted_shifts = alphabetizing_module(filtered_shifts)
    
    # Step 4: Output Module
    formatted_output = output_module(sorted_shifts, line_storage)
    
    # Display output
    print("KWIC Index:")
    for line in formatted_output:
        print(line)

# Execute the KWIC process
master_control()