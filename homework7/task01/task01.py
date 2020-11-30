"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    count = 0
    for value in tree.values():
        if isinstance(value, dict):
            count += find_occurrences(value, element)
        elif (
            isinstance(value, list)
            or isinstance(value, tuple)
            or isinstance(value, set)
        ):
            for subvalue in value:
                if isinstance(subvalue, dict):
                    count += find_occurrences(subvalue, element)
                elif element == subvalue:
                    count += 1
        elif element == value:
            count += 1
    return count
