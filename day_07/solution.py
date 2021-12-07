"""
Part 1:
    What's the least amount of fuel the crabs need to align their horizontal positions
Part 2:
    What's the least amount of fuel the crabs need to align their horizontal positions,
    with non-linear cost
"""

from statistics import median


class Crabs:
    """The Crabs class"""

    def __init__(self, positions: str) -> None:
        """Intialize Crabs class"""
        self.positions = self._read_positions(positions)

    @staticmethod
    def _read_positions(positions: str) -> list[int]:
        """Read positions"""
        return [int(pos) for pos in positions.split(",")]

    def calculate_wrong_cost_to_align(self) -> int:
        """Calculate cost to align based on part 1"""
        optimal_position = median(self.positions)
        diffs = [int(abs(pos - optimal_position)) for pos in self.positions]
        return sum(diffs)

    def calculate_min_cost_to_align(self) -> int:
        """Calculate cost to align crab subs"""
        optimal_ranges = range(min(self.positions), max(self.positions) + 1)
        min_fuel_cost = float("inf")
        for possible in optimal_ranges:
            fuel_cost = 0
            for position in self.positions:
                diff = abs(position - possible)
                fuel_cost += sum(range(diff + 1))

            if fuel_cost < min_fuel_cost:
                min_fuel_cost = fuel_cost

        return int(min_fuel_cost)


if __name__ == "__main__":
    with open("day_07/input.txt") as input_file:
        puzzle_input = input_file.read()

    # Part 1 answer
    crabs = Crabs(puzzle_input)
    print(crabs.calculate_wrong_cost_to_align())
    # Part 2 answer
    crabs = Crabs(puzzle_input)
    print(crabs.calculate_min_cost_to_align())
