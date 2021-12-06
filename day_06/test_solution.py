# pylint: disable=missing-module-docstring,missing-function-docstring,redefined-outer-name

import pytest

from day_06.solution import LaternFishSchool


@pytest.fixture
def puzzle_input():
    return """3,4,3,1,2"""


def test_solution_part_1(puzzle_input):
    latern_school = LaternFishSchool(puzzle_input)
    assert latern_school.predict_size(80) == 5934


def test_solution_part_2(puzzle_input):
    latern_school = LaternFishSchool(puzzle_input)
    assert latern_school.predict_size(256) == 26984457539
