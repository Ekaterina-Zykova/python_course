from typing import Any, Tuple

import pytest

from homework3.task01.decorator import cache


@pytest.mark.parametrize(
    ["times", "args", "expected_result"],
    [(2, (100, 200), True), (10, (100, 200), True)],
)
def test_cache(times: int, args: Tuple[Any], expected_result: bool):
    @cache(times=times)
    def func(a: int, b: int) -> int:
        return a ** b ** 2

    result_for_n_times = [func(*args) for _ in range(times + 1)]
    result_for_more_n_times = func(*args)

    actual_result = True
    for result in result_for_n_times:
        if result is result_for_more_n_times:
            actual_result = False
            break

    assert actual_result == expected_result
