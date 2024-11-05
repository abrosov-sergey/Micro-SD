# Malysh Igor | Task 8 | Problem A | Method 1: Abstract Data Types

from typing import List


class CircularShift:
    """
    CircularShift ADT generates circular shifts of lines, excluding shifts that start with stop words.
    """

    def __init__(self, lines: List[str], stop_words: List[str]):
        self.lines = lines
        self.stop_words = stop_words
        self.shifted_lines = self.generate_shifts()

    def generate_shifts(self) -> List[str]:
        """
        Generates all circular shifts for each line, excluding those that start with stop words.
        """
        shifted_lines = []
        for line in self.lines:
            words = line.split()
            for i in range(len(words)):

                shifted = " ".join(words[i:] + words[:i])

                if words[i].lower() not in self.stop_words:
                    shifted_lines.append(shifted)
        return shifted_lines

    def get_shifts(self) -> List[str]:
        return self.shifted_lines


class Alphabetizer:
    """
    Alphabetizer ADT sorts lines alphabetically.
    """

    def __init__(self, lines: List[str]):
        self.lines = lines
        self.sorted_lines = self.sort_lines()

    def sort_lines(self) -> List[str]:
        """
        Sorts the lines alphabetically.
        """
        return sorted(self.lines)

    def get_sorted_lines(self) -> List[str]:
        return self.sorted_lines


class KWIC:
    """
    KWIC ADT integrates circular shifts and alphabetizes them, with stop word filtering.
    """

    def __init__(self, lines: List[str], stop_words: List[str]):
        self.lines = lines
        self.stop_words = stop_words

    def generate_kwic_index(self) -> List[str]:
        """
        Generates the KWIC index with stop word filtering.
        """

        circular_shift = CircularShift(self.lines, self.stop_words)
        shifted_lines = circular_shift.get_shifts()

        alphabetizer = Alphabetizer(shifted_lines)
        sorted_lines = alphabetizer.get_sorted_lines()

        return sorted_lines


if __name__ == "__main__":
    # Provided text
    text = """
    Python is a multi-paradigm programming language. 
    Object-oriented programming and structured programming are fully supported, 
    and many of their features support functional programming and aspect-oriented programming 
    (including metaprogramming and metaobjects). 
    Many other paradigms are supported via extensions, 
    including design by contract and logic programming. 
    Python is known as a glue language, 
    able to work very well with many other languages with ease of access.
    """

    stop_words = ["is", "a", "the", "in", "and", "of", "to", "with", "for"]

    lines = [sentence.strip() for sentence in text.split(".") if sentence.strip()]

    kwic = KWIC(lines, stop_words)
    kwic_index = kwic.generate_kwic_index()

    print("KWIC Index:")
    for line in kwic_index:
        print(line)
