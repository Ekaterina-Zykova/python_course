from typing import Any

import pytest

from homework7.task01.task01 import find_occurrences

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
        },
    },
    "fourth": "RED",
}


@pytest.mark.parametrize(
    ["element", "expected_result"],
    [("RED", 6), ("BLUE", 2), ("value1", 1), ("BLACK", 0)],
)
def test_find_occurrences(element: Any, expected_result: int):
    actual_result = find_occurrences(example_tree, element)
    assert actual_result == expected_result
