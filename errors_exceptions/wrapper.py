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

    Raises:
        ValueError: If line_length is not positive.
    """
    if line_length < 1:
        raise ValueError("line_length {} is not positive".format(line_length))
    words = text.split()
    lines_of_words = []
    current_line_length = line_length
    for word in words:
        if current_line_length + len(word) > line_length:

            lines_of_words.append([]) # new line
            current_line_length = 0
        lines_of_words[-1].append(word)
        current_line_length += len(word) + len(' ')
    lines = [' '.join(line_of_words) for line_of_words in lines_of_words]
    result = '\n'.join(lines)
    assert all(len(line) <= line_length for line in result.splitlines()), "Line too long"
    return result