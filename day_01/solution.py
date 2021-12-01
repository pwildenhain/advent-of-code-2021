"""
Part 1:
    Determine how many times the depth measurement increased
Part 2:
    Determine how many times the depth measurement increased
    using a three measurement sliding window
"""


class Sonar:
    """The Sonar class for the submarine we're using to find the keys to the sleigh"""

    def __init__(self, measurements: str) -> None:
        """Intialize Sonar class"""
        self.measurements = self._read_measurements(measurements)

    @staticmethod
    def _read_measurements(measurements: str) -> list[int]:
        """Take in measurements input, and return as a numeric list"""
        return [int(measure) for measure in measurements.splitlines()]

    def calculate_depth_changes(self, window: int) -> list[int]:
        """Returns a list of the changes in depth from the previous measurement"""
        measurement_windows: list[list[int]] = []
        for idx, _ in enumerate(self.measurements):
            measurement_window = self.measurements[idx : idx + window]
            measurement_windows += [measurement_window]

        depth_changes: list = []
        for idx, measures in enumerate(measurement_windows[1:]):
            previous_measures: list[int] = measurement_windows[idx]
            depth_changes += [sum(measures) - sum(previous_measures)]

        return depth_changes


if __name__ == "__main__":
    with open("day_01/input.txt") as input_file:
        puzzle_input = input_file.read()

    sonar = Sonar(measurements=puzzle_input)

    changes = sonar.calculate_depth_changes(window=1)
    num_increases = sum([change > 0 for change in changes])
    # Part 1 answer
    print(f"There were {num_increases} consecutively increasing depth measurements")

    changes = sonar.calculate_depth_changes(window=3)
    num_increases = sum([change > 0 for change in changes])
    # Part 2 answer
    print(
        f"There were {num_increases} increasing depth measurements with a three measurement window"
    )
