"""
Part 1:
    Determine where all the non-diagonal vents overlap
Part 2:

"""

from collections import Counter


class Vent:
    """The Vent class"""

    def __init__(self, endpoints: str, exclude_diagonals: bool) -> None:
        self.points = self._read_endpoints(endpoints, exclude_diagonals)
        self.start = self.points[0]
        self.end = self.points[-1]

    def __repr__(self) -> str:
        return f"{ self.start } -> { self.end }: { self.points }"

    @staticmethod
    def _read_endpoints(
        endpoints: str, exclude_diagonals: bool
    ) -> list[tuple[int, int]]:
        start_str, end_str = endpoints.split(" -> ")
        start = tuple(int(point) for point in start_str.split(","))
        end = tuple(int(point) for point in end_str.split(","))
        start_x, start_y = start
        end_x, end_y = end

        if exclude_diagonals and start_x != end_x and start_y != end_y:
            raise ValueError(f"No diagonals allowed { endpoints }")

        if end_x > start_x:
            x_range: list[int] = list(range(start_x + 1, end_x))
        elif start_x > end_x:
            x_range = list(reversed(range(end_x + 1, start_x)))
        else:
            x_range = [start_x] * abs(start_y - end_y)

        if end_y > start_y:
            y_range: list[int] = list(range(start_y + 1, end_y))
        elif start_y > end_y:
            y_range = list(reversed(range(end_y + 1, start_y)))
        else:
            y_range = [start_y] * abs(start_x - end_x)

        points = list(zip(x_range, y_range))

        return [start] + points + [end]  # type: ignore


class VentMap:
    """The VentMap class"""

    def __init__(self, map_input: str, exclude_diagonals: bool) -> None:
        """Intialize VentMap class"""
        self.vent_list = self._read_vent_list(map_input, exclude_diagonals)

    @staticmethod
    def _read_vent_list(map_input: str, exclude_diagonals: bool) -> list[Vent]:
        """Read vent_map"""
        vent_list = []
        for endpoints in map_input.splitlines():
            try:
                vent = Vent(endpoints, exclude_diagonals)
                vent_list += [vent]
            except ValueError:
                pass
        return vent_list

    def calculate_number_of_overlaps(self) -> int:
        """Calculate the number of overlaps on the vent map"""
        point_list = []
        for vent in self.vent_list:
            point_list += vent.points
        point_count_dict = Counter(point_list)

        return len([point for point in point_count_dict if point_count_dict[point] > 1])


if __name__ == "__main__":
    with open("day_05/input.txt") as input_file:
        puzzle_input = input_file.read()

    # Part 1 answer
    vent_map = VentMap(puzzle_input, exclude_diagonals=True)
    print(vent_map.calculate_number_of_overlaps())
    # Part 2 answer
    vent_map = VentMap(puzzle_input, exclude_diagonals=False)
    print(vent_map.calculate_number_of_overlaps())
