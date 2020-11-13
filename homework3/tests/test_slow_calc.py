import pytest

from homework3.task02.slow_calculator import slow_calc_with_mp


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (500, 60),
    ],
)
def test_slow_calc_with_mp(value: int, expected_result: int):
    actual_result = slow_calc_with_mp(value)

    assert actual_result <= expected_result
