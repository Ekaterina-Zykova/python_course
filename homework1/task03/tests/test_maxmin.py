import pytest

from find_maxmin.maxmin import find_maximum_and_minimum
from typing import Tuple


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("homework1/task03/tests/test_file.txt", (1, 5)),
    ],
)
def test_find_max_and_min(file_name: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result
