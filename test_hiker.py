from hiker import global_answer, Hiker

from approvaltests import verify, Options
from approvaltests.inline.inline_options import InlineOptions

options = Options().inline(InlineOptions.semi_automatic())


def test_global():
    """
    48
    ***** DELETE ME TO APPROVE *****
    """
    result = str(global_answer())
    verify(result, options=options)


def test_global_square():
    """
    110592
    """
    result = str(global_answer(power=3))
    verify(result, options=options)

