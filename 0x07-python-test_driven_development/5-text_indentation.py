#!/usr/bin/python3
def text_indentation(text):
    """
    A function that prints a text with 2 newlines after each of the chars:
    '.', '?', ':'
    Parameters:
    text (str): string to print
    Raise:
    TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        char = text[i]
        if text[i - 1] in ['.', '?', ':']:
            continue
        print("{}".format(char), end="")
        if char in ['.', '?', ':']:
            print("\n\n")
