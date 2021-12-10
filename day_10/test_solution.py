# pylint: disable=missing-module-docstring,missing-function-docstring,redefined-outer-name

import pytest

from day_10.solution import SyntaxChecker


@pytest.fixture
def puzzle_input():
    return """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


def test_solution_part_1(puzzle_input):
    sytanx_checker = SyntaxChecker(puzzle_input)
    assert sytanx_checker.calculate_syntax_error_score() == 26397


def test_solution_part_2(puzzle_input):
    sytanx_checker = SyntaxChecker(puzzle_input)
    assert sytanx_checker.calculate_autocomplete_score() == 288957
