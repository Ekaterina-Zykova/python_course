from typing import List

import pytest

from homework7.task03.task03 import tic_tac_toe_checker


@pytest.mark.parametrize(
    ["board", "expected_result"],
    [
        ([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]], "unfinished"),
        ([["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]], "x wins!"),
        ([["-", "-", "o"], ["-", "x", "o"], ["x", "x", "o"]], "o wins!"),
        ([["o", "x", "o"], ["o", "x", "o"], ["x", "o", "x"]], "draw!"),
    ],
)
def test_tic_tac_toe_checker(board: List[List], expected_result: str):
    actual_result = tic_tac_toe_checker(board)
    assert actual_result == expected_result
