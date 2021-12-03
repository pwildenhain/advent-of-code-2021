# pylint: disable=missing-module-docstring,missing-function-docstring,redefined-outer-name

import pytest

from day_03.solution import Diagnostic


@pytest.fixture
def puzzle_input():
    return """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def test_solution_part_1(puzzle_input):
    diagnostic = Diagnostic(puzzle_input)
    power_consumption = diagnostic.calculate_power_consumption()
    assert power_consumption == 198


def test_solution_part_2(puzzle_input):
    diagnostic = Diagnostic(puzzle_input)
    life_support_rating = diagnostic.calculate_life_support_rating()
    assert life_support_rating == 230
