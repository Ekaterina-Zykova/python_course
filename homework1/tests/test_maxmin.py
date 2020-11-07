import os
from typing import Tuple

import pytest
from task03.find_maxmin import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        (os.path.join(r"homework1\tests\test_file.txt"), (1, 5)),
    ],
)
def test_find_max_and_min(file_name: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result
