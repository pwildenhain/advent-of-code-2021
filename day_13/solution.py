"""
Part 1:
    Follow the firsts folding instruction in the manual to see how many dots remain visible
Part 2:
    Follow all the instructions in the manual to see what our activation code is
"""

from copy import deepcopy


class ThermalImagingManual:
    """The ThermalImagingManual class"""

    def __init__(self, manual_input: str) -> None:
        """Intialize Manual class"""
        self.dots = self._read_dots(manual_input)
        self.instructions = self._read_instructions(manual_input)

    def __repr__(self) -> str:
        max_x = max([dot[0] for dot in self.dots]) + 1
        max_y = max([dot[1] for dot in self.dots]) + 1

        empty_grid = []
        for _ in range(max_y + 1):
            points = []
            for _ in range(max_x + 1):
                points += ["."]

            empty_grid += [points]

        for dot in self.dots:
            dot_x, dot_y = dot
            empty_grid[dot_y][dot_x] = "#"

        empty_grid_str = ""
        for line in empty_grid:
            for point in line:
                empty_grid_str += point
            empty_grid_str += "\n"

        return empty_grid_str

    @staticmethod
    def _read_dots(manual_input: str) -> list[tuple[int, int]]:
        """Read instructions"""
        dots_str = manual_input.split("\n\n")[0]
        dots = []
        for pos in dots_str.splitlines():
            dot_x_str, dot_y_str = pos.split(",")
            dot_x = int(dot_x_str)
            dot_y = int(dot_y_str)
            dots += [(dot_x, dot_y)]
        return dots

    @staticmethod
    def _read_instructions(manual_input: str) -> list[tuple[str, int]]:
        """Read instructions"""
        instructions_str = manual_input.split("\n\n")[1]
        instructions: list[tuple[str, int]] = []
        for instruction in instructions_str.splitlines():
            axis, idx_str = instruction.removeprefix("fold along ").split("=")
            idx = int(idx_str)
            instructions += [(axis, idx)]
        return instructions

    @staticmethod
    def fold(
        dots: list[tuple[int, int]], instruction: tuple[str, int]
    ) -> list[tuple[int, int]]:
        """
        with instruction=("y", 7)
        (1, 6) -> (1, 6)
        (1, 10) -> (1, 4)
        (0, 14) -> (0, 0)
        """
        axis, idx = instruction
        new_dots: list[tuple[int, int]] = []
        for dot in dots:
            dot_x, dot_y = dot
            if axis == "x" and dot_x > idx:
                new_dot = (idx * 2 - dot_x, dot_y)
            elif axis == "y" and dot_y > idx:
                new_dot = (dot_x, idx * 2 - dot_y)
            else:
                new_dot = dot

            if new_dot not in new_dots:
                new_dots += [new_dot]

        return new_dots

    def follow_instructions(self) -> list[tuple[int, int]]:
        """Follow all the instructions in the manual to get the activation code"""
        dots = deepcopy(self.dots)
        for instruction in self.instructions:
            dots = self.fold(dots, instruction)

        return dots


if __name__ == "__main__":
    with open("day_13/input.txt") as input_file:
        puzzle_input = input_file.read()

    # Part 1 answer
    manual = ThermalImagingManual(puzzle_input)
    visible_dots = manual.fold(manual.dots, manual.instructions[0])
    print(len(visible_dots))
    # Part 2 answer
    manual.dots = manual.follow_instructions()
    print(manual)
