"""
Part 1:
    Given the height map, what is the sum of all the risk factor of each low point
Part 2:
    Given the height map, identify the three largest basins
"""


from collections import defaultdict
from functools import reduce
from typing import DefaultDict

# this is the best I got pylint!
# pylint: disable=too-many-branches,too-many-locals


class HeightMap:
    """The HeightMap class"""

    def __init__(self, map_str: str) -> None:
        """Intialize HeightMap class"""
        self.height_map = self._read_map(map_str)

    @staticmethod
    def _read_map(map_str: str) -> list[str]:
        """Read map"""
        return list(map_str.splitlines())

    def map_crawl(
        self,
    ) -> tuple[
        dict[tuple[int, int], int], dict[tuple[int, int], list[tuple[int, int]]]
    ]:
        """Crawl through the height map and spit out data around low points and basins"""
        coords_category: DefaultDict[
            tuple[int, int], DefaultDict[str, str]
        ] = defaultdict(lambda: defaultdict(str))
        basin_dict: dict[tuple[int, int], list[tuple[int, int]]] = {}
        # search up, down, left, and right
        search_path = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for level_idx, level in enumerate(self.height_map):
            for point_idx, point in enumerate(level):
                for direction in search_path:
                    level_delta, point_delta = direction
                    neighbor_level_idx = level_idx + level_delta
                    neighbor_point_idx = point_idx + point_delta
                    if neighbor_level_idx < 0 or neighbor_point_idx < 0:
                        # off the map
                        continue
                    try:
                        neighboring_point = self.height_map[neighbor_level_idx][
                            neighbor_point_idx
                        ]
                    except IndexError:
                        # off the map
                        continue
                    neighboring_point_coord = (neighbor_level_idx, neighbor_point_idx)
                    neighboring_point_category = coords_category[
                        neighboring_point_coord
                    ][neighboring_point]

                    if neighboring_point_category == "high":
                        # we already know it's higher than at least one of it's adjacent points
                        # move along, nothing to see here
                        continue

                    if neighboring_point_category == "low":
                        new_category = "high" if neighboring_point >= point else "low"
                    elif neighboring_point_category == "":
                        # we've never categorized this point before, let's do that now
                        new_category = "high" if neighboring_point >= point else "low"

                    if new_category == "high" and neighboring_point != "9":
                        try:
                            basin_dict[(level_idx, point_idx)] += [
                                neighboring_point_coord
                            ]
                        except KeyError:
                            # new basin
                            basin_dict[(level_idx, point_idx)] = [
                                neighboring_point_coord
                            ]

                    coords_category[neighboring_point_coord][
                        neighboring_point
                    ] = new_category

        low_points_dict: dict[tuple[int, int], int] = {}
        for coord, category_dict in coords_category.items():
            for point, category in category_dict.items():
                if category == "low":
                    low_points_dict[coord] = int(point)

        return low_points_dict, basin_dict

    def calculate_risk_score(self) -> int:
        """Add up the value of all the low points"""
        low_points_dict, _ = self.map_crawl()
        risk_scores = [point + 1 for point in low_points_dict.values()]
        return sum(risk_scores)

    def get_all_points_in_basin(
        self,
        basin_start: tuple[int, int],
        basin_dict: dict[tuple[int, int], list[tuple[int, int]]],
    ) -> list[tuple[int, int]]:
        """
        Recursively sift through all the connected points in the basin
        and return a flattened list of those points, with potential duplicates
        """
        higher_points = basin_dict[basin_start]
        new_points = []
        for point in higher_points:
            try:
                new_points += self.get_all_points_in_basin(point, basin_dict)
            except KeyError:
                # no more higher points to find
                new_points += [point]

        return higher_points + new_points + [basin_start]

    def calculate_largest_basin_scores(self):
        """Calculate the size of all the basins, and multiply the three largest together"""
        low_points_dict, basin_dict = self.map_crawl()
        low_point_basin_size_dict = {}
        for point in low_points_dict:
            points_in_basin = self.get_all_points_in_basin(point, basin_dict)
            low_point_basin_size_dict[point] = len(set(points_in_basin))

        basin_sizes = list(low_point_basin_size_dict.values())
        basin_sizes.sort()

        return reduce(lambda x, y: x * y, basin_sizes[-3:])


if __name__ == "__main__":
    with open("day_09/input.txt") as input_file:
        puzzle_input = input_file.read()

    # Part 1 answer
    height_map = HeightMap(puzzle_input)
    print(height_map.calculate_risk_score())
    # Part 2 answer
    print(height_map.calculate_largest_basin_scores())
