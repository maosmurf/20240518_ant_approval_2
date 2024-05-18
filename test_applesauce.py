import pytest
from pytest_bdd import when, then, scenarios, parsers

from game import Game

scenarios("applesauce.feature")


@pytest.fixture(name="game")
def fixture_game():
    return Game(board=">")


@when("the game starts")
def step_impl(game):
    pass


@then(parsers.parse('the board looks like "{expected}"'))
def step_impl(game, expected: str):
    assert expected == str(game)
