from approvaltests import verify, Options
from approvaltests.inline.inline_options import InlineOptions

from hiker import global_answer

options = Options().inline(InlineOptions.semi_automatic())


def test_global():
    """
    48
    ***** DELETE ME TO APPROVE *****
    """
    result = str(global_answer())
    verify(result, options=options)
