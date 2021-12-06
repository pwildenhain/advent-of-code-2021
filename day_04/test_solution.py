# pylint: disable=missing-module-docstring,missing-function-docstring,redefined-outer-name

import pytest

from day_04.solution import Bingo


@pytest.fixture
def puzzle_input():
    return """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


def test_solution_part_1(puzzle_input):
    bingo_system = Bingo(puzzle_input)
    winning_board = bingo_system.play()
    assert winning_board.calculate_score() == 4512


def test_solution_part_2(puzzle_input):
    bingo_system = Bingo(puzzle_input)
    last_winning_board = bingo_system.get_last_winning_board()
    assert last_winning_board.calculate_score() == 1924
