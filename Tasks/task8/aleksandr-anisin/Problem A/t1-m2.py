def process_input(text):
    return [line.strip() for line in text.splitlines() if line]

def circular_shift(lines):
    shifts = []
    for line in lines:
        words = line.split()
        for i in range(len(words)):
            shifts.append(' '.join(words[i:] + words[:i]))
    return shifts

def alphabetize(shifts):
    return sorted(shifts)

def display_result(alphabetized_shifts):
    for shift in alphabetized_shifts:
        print(shift)

def kwic(text):
    lines = process_input(text)
    shifts = circular_shift(lines)
    alphabetized_shifts = alphabetize(shifts)
    display_result(alphabetized_shifts)

sample_text = "The quick brown fox\njumps over the lazy dog"
kwic(sample_text)
