from functools import reduce

from approvaltests import verify, Options
from approvaltests.inline.inline_options import InlineOptions

options = Options().inline(InlineOptions.semi_automatic())

from game import Game


def game_after_steps(steps: int):
    game: Game = Game(board=">")
    for s in range(steps):
        game = game.move()
    return game


def test_new_game_has_space_to_the_right():
    """
    >
    """
    game = game_after_steps(steps=0)
    verify(game, options=options)


def test_move_ant_forward_once():
    """
    .v
    """
    result = game_after_steps(steps=1)
    verify(result, options=options)


def test_move_ant_forward_twice():
    """
    ..
     <
    """
    result = game_after_steps(steps=2)
    verify(result, options=options)
