# pylint: disable=missing-module-docstring,missing-function-docstring,redefined-outer-name

import pytest

from day_05.solution import VentMap


@pytest.fixture
def puzzle_input():
    return """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def test_solution_part_1(puzzle_input):
    vent_map = VentMap(puzzle_input, exclude_diagonals=True)
    assert vent_map.calculate_number_of_overlaps() == 5


def test_solution_part_2(puzzle_input):
    vent_map = VentMap(puzzle_input, exclude_diagonals=False)
    assert vent_map.calculate_number_of_overlaps() == 12
