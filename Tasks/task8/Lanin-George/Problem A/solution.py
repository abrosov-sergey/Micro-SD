"""
Created on 04.11.2024
Solution of the "Key Word in Context" (KWIC) problem
with Implicit invocation (event-driven) method.
@author: Geolan84
"""
from blinker import signal

line_signal = signal('line')
keyword_signal = signal('keyword')
display_signal = signal('display')


def process_line(sender, new_line, keywords, result):
    intersection = set(new_line.split()).intersection(keywords)
    if len(intersection) == 0:
        result.append(new_line)
    else:
        keyword_signal.send(
            process_keyword,
            line=new_line,
            keyword=intersection[0],
            result=result
        )


def process_keyword(sender, line, keyword, result):
    words = line.split()
    index = words.index(keyword)
    n_left = (40 - len(keyword)) // 2
    n_right = 40 - len(keyword) - n_left
    left_context = ' '.join(words[max(0, index - n_left):index])
    right_context = ' '.join(words[index + 1:index + 1 + n_right])
    result.append(f"{left_context} {keyword} {right_context}".strip())


def display_result(sender, result):
    print(*result)


line_signal.connect(process_line)


with open("stop_words.txt", "r") as f:
    keywords = {line.strip().lower() for line in f if line.strip()}
    result = []
    with open("text.txt", "r") as f_text:
        for line in f_text:
            line_signal.send(
                new_line=line.strip(),
                keywords=keywords,
                result=result
            )
        display_signal.send(result=result)
