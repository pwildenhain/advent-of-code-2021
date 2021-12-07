# pylint: disable=missing-module-docstring,missing-function-docstring,redefined-outer-name

import pytest

from day_07.solution import Crabs


@pytest.fixture
def puzzle_input():
    return """16,1,2,0,4,2,7,1,2,14"""


def test_solution_part_1(puzzle_input):
    crabs = Crabs(puzzle_input)
    assert crabs.calculate_wrong_cost_to_align() == 37


def test_solution_part_2(puzzle_input):
    crabs = Crabs(puzzle_input)
    assert crabs.calculate_min_cost_to_align() == 168
