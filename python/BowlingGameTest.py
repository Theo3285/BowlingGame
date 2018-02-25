import pytest

from Game import Game

@pytest.fixture
def game():
    return Game()

def test_dummy_gutter(game):
    roll_many(game, 20, 0)
    assert 0 == game.score()

def test_all_ones(game):
    roll_many(game, 20, 1)
    assert 20 == game.score()

def test_one_spare(game):
    game.roll(5)
    game.roll(5) #spare
    game.roll(3)
    roll_many(game, 17, 0)
    assert 16 == game.score()

def test_one_strike(game):
    game.roll(10)
    game.roll(3) # strike
    game.roll(4)
    roll_many(game, 16, 0)
    assert 24 == game.score()

def roll_many(game, n, pins):
    for i in range(n):
        game.roll(pins)


