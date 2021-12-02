"""
Part 1:

Part 2:

"""


class Something:
    """The Something class"""

    def __init__(self, instructions: str) -> None:
        """Intialize Something class"""
        self.instructions = self._read_instructions(instructions)

    @staticmethod
    def _read_instructions(instructions: str):
        """Read instructions"""
        return instructions


if __name__ == "__main__":
    with open("day_XX/input.txt") as input_file:
        puzzle_input = input_file.read()

    # Part 1 answer
    print()
    # Part 2 answer
    print()
