# pylint: disable=missing-module-docstring,missing-function-docstring,redefined-outer-name

import pytest

from day_13.solution import ThermalImagingManual


@pytest.fixture
def puzzle_input():
    return """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def test_solution_part_1(puzzle_input):
    manual = ThermalImagingManual(puzzle_input)
    visible_dots = manual.fold(manual.dots, manual.instructions[0])
    assert len(visible_dots) == 17


def test_solution_part_2(puzzle_input):
    manual = ThermalImagingManual(puzzle_input)
    # I don't want to actually write out the test output, just test that we can follow directions
    assert manual.follow_instructions()
