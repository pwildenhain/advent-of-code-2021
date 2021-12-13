"""
Part 1:

Part 2:

"""


from copy import deepcopy


class Octopuses:
    """The Octopuses class"""

    _sentinel: list[tuple[int, int]] = []

    def __init__(self, energy_levels: str) -> None:
        """Intialize Octopuses class"""
        self.energy_levels = self._read_energy_levels(energy_levels)

    def __repr__(self) -> str:
        """Nicely print the octopuses"""
        octopuses_str = ""
        for row in self.energy_levels:
            for level in row:
                octopuses_str += str(level)
            octopuses_str += "\n"
        return octopuses_str

    @staticmethod
    def _read_energy_levels(energy_levels: str) -> list[list[int]]:
        """Read energy_levels"""
        energy_levels_list: list[list[int]] = []
        for row in list(energy_levels.splitlines()):
            energy_levels_list += [[int(level) for level in row]]

        return energy_levels_list

    @staticmethod
    def simulate_step(energy_levels_list: list[list[int]]) -> list[list[int]]:
        """Increment all octopus energy levels by one"""
        # Step every level up by one
        for row_idx, row in enumerate(energy_levels_list):
            for level_idx, _ in enumerate(row):
                energy_levels_list[row_idx][level_idx] += 1

        return energy_levels_list

    @staticmethod
    def find_neighbors(
        energy_levels_list: list[list[int]], coord: tuple[int, int]
    ) -> list[tuple[int, int]]:
        """Find the neighbors of a given octopus"""
        neighboring_levels: list[tuple[int, int]] = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]

        levels_list_max = len(energy_levels_list) - 1
        level_max = len(energy_levels_list[0]) - 1
        row_idx, level_idx = coord
        neighbors: list[tuple[int, int]] = []
        for neighbor in neighboring_levels:
            row_delta, level_delta = neighbor
            neighbor_row_idx = row_idx + row_delta
            neighbor_level_idx = level_idx + level_delta
            off_list = (
                neighbor_row_idx < 0
                or neighbor_row_idx > levels_list_max
                or neighbor_level_idx < 0
                or neighbor_level_idx > level_max
            )
            if off_list:
                # skip to next potential neighbor
                continue

            neighbors += [(neighbor_row_idx, neighbor_level_idx)]

        return neighbors

    # In this case we're allowing a mutable default value to make the function more
    # type safe. If we detect the mutable default value has been passed, then we
    # immediately overwrite it
    # pylint: disable=dangerous-default-value
    def simulate_flashes(
        self,
        energy_levels_list: list[list[int]],
        already_flashed_list: list[tuple[int, int]] = _sentinel,
    ) -> tuple[list[list[int]], list[tuple[int, int]]]:
        """
        Given the state of the octopuses after a step,
        recursively crawl through the group to determine who flashes
        """
        if already_flashed_list is self._sentinel:
            already_flashed_list = []

        for row_idx, row in enumerate(energy_levels_list):
            for level_idx, level in enumerate(row):
                if (row_idx, level_idx) in already_flashed_list:
                    # an octopus can't flash more than once in a step
                    continue
                if level > 9:
                    already_flashed_list += [(row_idx, level_idx)]
                    energy_levels_list[row_idx][level_idx] = 0
                    neighbors = self.find_neighbors(
                        energy_levels_list, (row_idx, level_idx)
                    )
                    for neighbor in neighbors:
                        if neighbor in already_flashed_list:
                            # an octopus can't gain energy after it's flashed
                            continue
                        neighbor_row_idx, neighbor_level_idx = neighbor
                        energy_levels_list[neighbor_row_idx][neighbor_level_idx] += 1

                    energy_levels_list, already_flashed_list = self.simulate_flashes(
                        energy_levels_list, already_flashed_list
                    )

        return energy_levels_list, already_flashed_list

    # pylint: enable=dangerous-default-value

    def calculate_flashes(self, steps: int) -> int:
        """Calculate the number of flashes in the octopus group after a certain number of steps"""
        energy_levels_list = deepcopy(self.energy_levels)
        num_flashes = 0
        for _ in range(steps):
            energy_levels_list = self.simulate_step(energy_levels_list)
            energy_levels_list, flashed_list = self.simulate_flashes(energy_levels_list)

            num_flashes += len(flashed_list)

        return num_flashes

    def get_simultaneous_step(self) -> int:
        """Figure out when all the octopuses flash simultaneously"""
        energy_levels_list = deepcopy(self.energy_levels)
        num_octopuses = len(energy_levels_list) * len(energy_levels_list[0])
        step = 0
        simultaneous_flash = False
        while not simultaneous_flash:
            step += 1
            energy_levels_list = self.simulate_step(energy_levels_list)
            energy_levels_list, flashed_list = self.simulate_flashes(energy_levels_list)
            if len(flashed_list) == num_octopuses:
                simultaneous_flash = True

        return step


if __name__ == "__main__":
    with open("day_11/input.txt") as input_file:
        puzzle_input = input_file.read()

    # Part 1 answer
    octopuses = Octopuses(puzzle_input)
    print(octopuses.calculate_flashes(steps=100))
    # new_levels = octopuses.simulate_step(octopuses.energy_levels)
    # print(octopuses.simulate_step(new_levels))
    # Part 2 answer
    print(octopuses.get_simultaneous_step())
