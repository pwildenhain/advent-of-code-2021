# pylint: disable=missing-module-docstring,missing-function-docstring,redefined-outer-name

import pytest

from day_11.solution import Octopuses


@pytest.fixture
def puzzle_input():
    return """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def test_solution_part_1(puzzle_input):
    octopuses = Octopuses(puzzle_input)
    assert octopuses.calculate_flashes(steps=100) == 1656


def test_solution_part_2(puzzle_input):
    octopuses = Octopuses(puzzle_input)
    assert octopuses.get_simultaneous_step() == 195
