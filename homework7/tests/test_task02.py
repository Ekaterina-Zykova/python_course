import pytest

from homework7.task02.task02 import backspace_compare


@pytest.mark.parametrize(
    ["first", "second", "expected_result"],
    [
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
    ],
)
def test_backspace_compare(first: str, second: str, expected_result: bool):
    actual_result = backspace_compare(first, second)
    assert actual_result == expected_result
