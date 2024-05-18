"""
The "ant" moves according to the rules below:

    At a white square, turn 90° clockwise, flip the color of the square, move forward one unit
    At a black square, turn 90° counter-clockwise, flip the color of the square, move forward one unit
"""
from typing import Self


class Game:
    def __init__(self, board):
        self.board = board

    def __repr__(self):
        return self.board

    def move(self) -> Self:
        return move_ant_forward(self)


def move_ant_forward(game: Game) -> Game:
    """"""
    if len(str(game)) == 2:
        s = """
..
 <
         """
        return Game(board=s.strip())
    return Game(board='.v')
