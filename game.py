"""
The "ant" moves according to the rules below:

    At a white square, turn 90° clockwise, flip the color of the square, move forward one unit
    At a black square, turn 90° counter-clockwise, flip the color of the square, move forward one unit
"""


def create_game() -> str:
    return ">"


def move_ant_forward(game: str) -> str:
    return f'.{game}'
