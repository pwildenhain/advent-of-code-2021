"""
Part 1:

Part 2:

"""

from statistics import median
from typing import Optional


class SyntaxChecker:
    """The SyntaxChecker class"""

    def __init__(self, codes: str) -> None:
        """Intialize SyntaxChecker class"""
        self.codes = self._read_codes(codes)
        self.syntax_dict = {"(": ")", "[": "]", "{": "}", "<": ">"}

    @staticmethod
    def _read_codes(codes: str) -> list[str]:
        """Read codes"""
        return list(codes.splitlines())

    def _check_for_error(self, code: str) -> Optional[str]:
        """Check if there is an error in the code and return it, else return the remaining chars"""
        expected_chars = []
        error: Optional[str] = None
        for char in code:
            # starting char
            if char in self.syntax_dict:
                expected_chars += [self.syntax_dict[char]]
            # ending char
            else:
                expected_char = expected_chars.pop()
                if char != expected_char:
                    error = char
                    break

        return error

    def _get_auto_complete(self, code: str) -> str:
        """Return the chars needed to complete the code"""
        expected_chars = []
        for char in code:
            # starting char
            if char in self.syntax_dict:
                expected_chars += [self.syntax_dict[char]]
            # ending char
            else:
                expected_chars.pop()
        # Need to work backward to autocomplete
        expected_chars.reverse()
        return "".join(expected_chars)

    def calculate_syntax_error_score(self) -> int:
        """Calculate the total sum of the error scores"""
        error_score = 0
        score_dict = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137,
        }

        for code in self.codes:
            error = self._check_for_error(code)
            if error:
                error_score += score_dict[error]

        return error_score

    def calculate_autocomplete_score(self) -> int:
        """Calculate the autocomplete score of the remaining characters"""
        autocomplete_scores = []
        score_dict = {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4,
        }
        for code in self.codes:
            if self._check_for_error(code):
                # error found, no autocomplete is possible
                continue

            autocomplete = self._get_auto_complete(code)
            score = 0
            for char in autocomplete:
                score *= 5
                score += score_dict[char]

            autocomplete_scores += [score]

        return int(median(autocomplete_scores))


if __name__ == "__main__":
    with open("day_10/input.txt") as input_file:
        puzzle_input = input_file.read()

    # Part 1 answer
    syntax_checker = SyntaxChecker(puzzle_input)
    print(syntax_checker.calculate_syntax_error_score())
    # Part 2 answer
    print(syntax_checker.calculate_autocomplete_score())
