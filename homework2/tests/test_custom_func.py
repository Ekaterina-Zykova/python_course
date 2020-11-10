from collections.abc import Sequence
from string import ascii_lowercase
from typing import Any, List

import pytest

from homework2.task05.custom_func import custom_range


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ((ascii_lowercase, "g"), ["a", "b", "c", "d", "e", "f"]),
        ((ascii_lowercase, "g", "p"), ["g", "h", "i", "j", "k", "l", "m", "n", "o"]),
        ((ascii_lowercase, "p", "g", -2), ["p", "n", "l", "j", "h"]),
    ],
)
def test_custom_range(value: Sequence[Any], expected_result: List[Any]):
    actual_result = custom_range(*value)

    assert actual_result == expected_result
