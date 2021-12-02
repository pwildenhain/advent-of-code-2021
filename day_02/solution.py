"""
Part 1:
    Determine the final horizontal position multiplied by the final depth
Part 2:

"""


class Navigation:
    """The Navigation class for the submarine we're using to find the keys to the sleigh"""

    def __init__(self, directions: str) -> None:
        """Intialize Navigation class"""
        self.horizontal_pos = 0
        self.depth = 0
        self.aim = 0
        self.directions = self._read_directions(directions)

    @staticmethod
    def _read_directions(directions: str) -> list[tuple[int, int]]:
        """Take in directions input, and return as a list of tuples
        with horizontal and depth changes
        """
        directions_list: list = []
        for line in directions.splitlines():
            direction, magnitude_str = line.split()
            magnitude = int(magnitude_str)

            horizontal_delta: int = magnitude if direction == "forward" else 0

            if direction == "up":
                depth_direction = -1
            elif direction == "down":
                depth_direction = 1

            depth_delta: int = (
                magnitude * depth_direction if direction in ["up", "down"] else 0
            )

            directions_list += [(horizontal_delta, depth_delta)]

        return directions_list

    def calculate_wrong_position(self) -> tuple[int, int]:
        """Return the wrong horizontal position and depth given
        how we understood the directions in part 1"""
        for direction in self.directions:
            horizontal_delta, depth_delta = direction
            self.horizontal_pos += horizontal_delta
            self.depth += depth_delta

        return (self.horizontal_pos, self.depth)

    def calculate_final_position(self) -> tuple[int, int]:
        """Return the wrong horizontal position and depth given
        how we understood the directions in part 1"""
        for direction in self.directions:
            horizontal_delta, aim_delta = direction
            self.horizontal_pos += horizontal_delta
            self.aim += aim_delta
            self.depth += horizontal_delta * self.aim

        return (self.horizontal_pos, self.depth)


if __name__ == "__main__":
    with open("day_02/input.txt") as input_file:
        puzzle_input = input_file.read()

    nav = Navigation(puzzle_input)
    wrong_horizontal, wrong_depth = nav.calculate_wrong_position()
    # Part 1 answer
    print(
        f"The {wrong_horizontal=} position mulitplied by the {wrong_depth=} position",
        f"is {wrong_horizontal * wrong_depth}",
    )
    # Part 2 answer
    nav = Navigation(puzzle_input)
    final_horizontal, final_depth = nav.calculate_final_position()
    print(
        f"The {final_horizontal=} position mulitplied by the {final_depth=} position",
        f"is {final_horizontal * final_depth}",
    )
