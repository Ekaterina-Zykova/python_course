"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def del_backspace(string: str) -> list[str]:
    list_str = []
    for symbol in string:
        if symbol != "#":
            list_str.append(symbol)
        elif list_str:
            list_str.pop()
    return list_str


def backspace_compare(first: str, second: str) -> bool:
    return del_backspace(first) == del_backspace(second)
