from approvaltests import verify, Options
from approvaltests.inline.inline_options import InlineOptions

options = Options().inline(InlineOptions.semi_automatic())

from game import create_game, move_ant_forward


def test_new_game_has_space_to_the_right():
    """
    >.
    """
    game = create_game()
    verify(game, options=options)


def test_move_ant_forward():
    """
    .>
    """
    game = create_game()
    result = move_ant_forward(game=game)
    verify(result, options=options)
