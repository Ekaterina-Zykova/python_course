from time import time

import pytest

from homework3.task02.slow_calculator import slow_calc_with_mp


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (500, 60),
    ],
)
def test_slow_calc_with_mp(value: int, expected_result: int):
    start_time = time()
    slow_calc_with_mp(value)
    end_time = time()
    actual_result = end_time - start_time
    assert actual_result <= expected_result
