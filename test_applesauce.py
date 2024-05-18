import pytest
from pytest_bdd import when, then, scenarios, parsers, given

from game import Game

scenarios("applesauce.feature")


@pytest.fixture(name="foo")
def fixture_foo() -> dict:
    return dict()


@given(parsers.parse('the game starts with "{start}"'))
def fixture_game(foo, start):
    foo['game'] = Game(board=start)


@when(parsers.parse("{steps:d} run"))
def steps_run(foo, steps):
    game = foo['game']
    for s in range(steps):
        game = game.move()
    foo['game'] = game


@when("the game starts")
def step_impl(foo):
    pass


@then(parsers.parse('the board looks like "{expected}"'))
def step_impl(foo, expected: str):
    assert expected == str(foo['game'])
