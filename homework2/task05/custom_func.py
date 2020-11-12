"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any, List


def custom_range(value, stop: Any, start: Any = None, step: int = 1) -> List[Any]:
    value_list = list(value)
    if start is None:
        return list(value[0 : value_list.index(stop) : step])
    stop, start = start, stop
    start = value_list.index(start)
    stop = value_list.index(stop)
    return list(value[start:stop:step])
