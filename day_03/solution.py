"""
Part 1:
    Determine the power consumption with a list of binary codes
Part 2:
    Determine the life support rating with a list of binary codes
"""

from enum import Enum
from typing import Optional


class Frequency(str, Enum):
    """Frequency of appearance for diagnostic ratings"""

    MOST = "most"
    LEAST = "least"


class Diagnostic:
    """The Diagnostic class"""

    def __init__(self, codes: str) -> None:
        """Intialize Diagnostic class"""
        self.codes = list(codes.splitlines())
        self.codes_transposed = self._tranpose_codes(self.codes)

    @staticmethod
    def _tranpose_codes(codes: list[str]) -> list[str]:
        """Read codes transposed, since that's how we actually calculate values"""
        code_len = len(codes[0])
        codes_transposed: list[str] = ["" for _ in range(code_len)]
        for code in codes:
            for idx in range(code_len):
                codes_transposed[idx] += code[idx]

        return codes_transposed

    def calculate_power_consumption(self) -> int:
        """Calculate the gamma and epsilon values, multiplied together"""
        gamma: bytes = b""
        epsilon: bytes = b""
        code_len = len(self.codes_transposed[0])

        for code in self.codes_transposed:
            zero_count = code.count("0")
            one_count = code_len - zero_count
            if zero_count > one_count:
                gamma += b"0"
                epsilon += b"1"
            else:
                gamma += b"1"
                epsilon += b"0"

        return int(gamma, 2) * int(epsilon, 2)

    def _calculate_rating(self, frequency: Frequency) -> int:
        """Calculate a rating given a codes list"""
        codes_list = self.codes.copy()
        codes_list_transposed = self._tranpose_codes(codes_list)
        rating: Optional[bytes] = None
        idx: int = 0

        while not rating:
            code = codes_list_transposed[idx]
            code_len = len(code)
            zero_count = code.count("0")
            one_count = code_len - zero_count

            if frequency == "least":
                num = "0" if zero_count <= one_count else "1"
            elif frequency == "most":
                num = "1" if one_count >= zero_count else "0"

            if len(codes_list) > 1:
                codes_list = [code for code in codes_list if code[idx] == num]

                codes_list_transposed = self._tranpose_codes(codes_list)

                idx += 1

            if len(codes_list) == 1:
                rating = codes_list[0].encode("utf-8")

        return int(rating, 2)

    def calculate_life_support_rating(self) -> int:
        """Calculate the oxygen generator rating and CO2 scrubber rating multiplied together"""
        o2_generator_rating = self._calculate_rating(Frequency("most"))
        co2_scrubber_rating = self._calculate_rating(Frequency("least"))
        return o2_generator_rating * co2_scrubber_rating


if __name__ == "__main__":
    with open("day_03/input.txt") as input_file:
        puzzle_input = input_file.read()

    # Part 1 answer
    diagnostic = Diagnostic(puzzle_input)
    print(f"The power consumption is: {diagnostic.calculate_power_consumption()}")
    # Part 2 answer
    print(f"The life support rating is: {diagnostic.calculate_life_support_rating()}")
