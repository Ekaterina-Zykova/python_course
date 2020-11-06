import pytest

from find_max_sum.max_subarray_sum import find_maximal_subarray_sum
from typing import List


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (([1, 3, -1, -3, 5, 3, 6, 7], 3), 16),
    ],
)
def test_check_sum_of_four(value: (List[int], int), expected_result: int):
    actual_result = find_maximal_subarray_sum(*value)

    assert actual_result == expected_result
