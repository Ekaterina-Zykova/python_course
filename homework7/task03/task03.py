"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    for coord in range(3):
        if board[coord][0] == board[coord][1] == board[coord][2]:
            return f"{board[coord][0]} wins!"
        elif board[0][coord] == board[1][coord] == board[2][coord]:
            return f"{board[0][coord]} wins!"
    if board[0][0] == board[1][1] == board[2][2]:
        return f"{board[0][0]} wins!"
    elif board[2][0] == board[1][1] == board[0][2]:
        return f"{board[2][0]} wins!"
    return "draw!" if str(board).count("-") == 0 else "unfinished"
