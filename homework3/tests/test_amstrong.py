import pytest

from homework3.task04.armstrong import is_armstrong


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (9, True),
        (153, True),
        (1634, True),
        (10, False),
        (155, False),
        (2237, False),
    ],
)
def test_is_armstrong(value: int, expected_result: bool):
    actual_result = is_armstrong(value)
    assert actual_result == expected_result
