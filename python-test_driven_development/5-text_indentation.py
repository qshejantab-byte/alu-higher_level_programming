#!/usr/bin/python3
"""Defines text_indentation.

Print text with new lines after ., ? and :

"""


def text_indentation(text):
    """Print a text with 2 new lines after ., ? and :

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        if char == " " and len(line) == 0:
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip())
