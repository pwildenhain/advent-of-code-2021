# pylint: disable=missing-module-docstring,missing-function-docstring,redefined-outer-name

import pytest

from day_09.solution import HeightMap


@pytest.fixture
def puzzle_input():
    return """2199943210
3987894921
9856789892
8767896789
9899965678"""


def test_solution_part_1(puzzle_input):
    height_map = HeightMap(puzzle_input)
    assert height_map.calculate_risk_score() == 15


def test_solution_part_2(puzzle_input):
    height_map = HeightMap(puzzle_input)
    assert height_map.calculate_largest_basin_scores() == 1134
