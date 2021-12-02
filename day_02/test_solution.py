# pylint: disable=missing-module-docstring,missing-function-docstring,redefined-outer-name

import pytest

from day_02.solution import Navigation


@pytest.fixture
def puzzle_input():
    return """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def test_solution_part_1(puzzle_input):
    nav = Navigation(puzzle_input)
    final_horizontal, final_depth = nav.calculate_wrong_position()
    assert final_horizontal * final_depth == 150


def test_solution_part_2(puzzle_input):
    nav = Navigation(puzzle_input)
    final_horizontal, final_depth = nav.calculate_final_position()
    assert final_horizontal * final_depth == 900
