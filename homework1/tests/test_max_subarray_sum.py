from typing import List

import pytest

from homework1.task05.max_subarray_sum import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (([1, 3, -1, -3, 5, 3, 6, 7], 3), 16),
        (([1, 2, 3, 4], 6), 10),
        (([], 6), 0),
        (([1, 2, 3], 0), 0),
        (([1, 2], 2), 3),
        (([1, 0, 0, 0, 0, 0, 1], 4), 1),
        (([1, 0, 0, 1], 4), 2),
        (([-1, 0, 0, 0, 0, 0], 4), 0),
        (([16, 3, -100, -3, 5, 3, 6, 7], 3), 19),
    ],
)
def test_check_sum_of_four(value: (List[int], int), expected_result: int):
    actual_result = find_maximal_subarray_sum(*value)

    assert actual_result == expected_result
