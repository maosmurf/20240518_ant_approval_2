from approvaltests import verify, Options
from approvaltests.inline.inline_options import InlineOptions

options = Options().inline(InlineOptions.semi_automatic())

from game import create_game


def test_new_game_has_space_to_the_right():
    """
    >.
    """
    game=create_game()
    verify(game, options=options)