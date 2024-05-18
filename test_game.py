from approvaltests import verify, Options
from approvaltests.inline.inline_options import InlineOptions

options = Options().inline(InlineOptions.semi_automatic())

from game import create_game, move_ant_forward


def test_new_game_has_space_to_the_right():
    """
    >
    """
    game = create_game()
    verify(game, options=options)


def test_move_ant_forward_once():
    """
    .v
    """
    game = create_game()
    result = move_ant_forward(game=game)
    verify(result, options=options)


def test_move_ant_forward_twice():
    """
    ..
     <
    """
    game1 = create_game()
    game2 = move_ant_forward(game=game1)
    game3 = move_ant_forward(game=game2)
    verify(game3, options=options)
