# pylint: disable=missing-module-docstring,missing-function-docstring,redefined-outer-name

import pytest

from day_01.solution import Sonar


@pytest.fixture
def puzzle_input():
    return """199
200
208
210
200
207
240
269
260
263"""


@pytest.mark.parametrize("window,answer", [(1, 7), (3, 5)])
def test_solution(puzzle_input, window, answer):
    sonar = Sonar(puzzle_input)
    changes = sonar.calculate_depth_changes(window=window)
    num_increases = sum([change > 0 for change in changes])
    assert num_increases == answer
