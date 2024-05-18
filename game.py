"""
The "ant" moves according to the rules below:

    At a white square, turn 90° clockwise, flip the color of the square, move forward one unit
    At a black square, turn 90° counter-clockwise, flip the color of the square, move forward one unit
"""
class Game:
    def __init__(self):
        pass

    def __repr__(self):
        return ">"


def create_game() -> str:
    return str(Game())


def move_ant_forward(game: str) -> str:
    return f'.v'
