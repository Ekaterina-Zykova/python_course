from collections.abc import Callable
from typing import Tuple

import pytest

from homework2.task04.cached import cache


@pytest.mark.parametrize(
    ["func", "args", "expected_result"],
    [
        ((lambda a, b: (a ** b) ** 2), (100, 200), True),
    ],
)
def test_cache(func: Callable, args: Tuple[int], expected_result: bool):
    cache_func = cache(func)
    val_1 = cache_func(*args)
    val_2 = cache_func(*args)
    actual_result = val_1 is val_2

    assert actual_result == expected_result
