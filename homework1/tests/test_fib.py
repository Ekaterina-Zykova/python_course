from collections.abc import Sequence

import pytest

from homework1.task02.check_fib import check_fibonacci


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], True),
        ([0, 1, 1], True),
        ([8, 13, 21], True),
        ([0, 1, 1, 3, 4], False),
        ([0, 1], False),
    ],
)
def test_check_fib(data: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(data)

    assert actual_result == expected_result
