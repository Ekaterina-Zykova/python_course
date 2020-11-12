"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    result_list = [[]]
    for list_inner in args:
        new_result_list = []
        for i in result_list:
            for j in list_inner:
                new_result_list += [i + [j]]
        result_list = new_result_list
    return result_list
