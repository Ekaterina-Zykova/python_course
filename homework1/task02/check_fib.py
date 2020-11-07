"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from collections.abc import Sequence


def _check_window(x: int, y: int, z: int) -> bool:
    return (x + y) == z


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) >= 3:
        a, b, c = data[0], data[1], data[2]
        while len(data) > 2:
            if not _check_window(a, b, c):
                return False
            a, b, c = data[0], data[1], data[2]
            data = data[1:]
        return True
    return False
