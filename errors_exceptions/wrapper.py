#! usr/bin/python3
# wrapper.py
# UTF-8

def wrap(text, line_length):
    """Wrap a string to a specified line length.

    Args:
        text: The string to wrap.
        line_length: The line length in characters.

    Returns:
        A wrapped string.
    """
    words = text.split()
    lines_of_words = []
    current_line_length = line_length
    for word in words:
        if current_line_length + len(word) > line_length:

            lines_of_words.append([]) # new line
            current_line_length = 0
        lines_of_words[-1].append(word)
        current_line_length += len(word)
    lines = [' '.join(line_of_words) for line_of_words in lines_of_words]
    return '\n'.join(lines)