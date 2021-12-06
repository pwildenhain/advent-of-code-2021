"""
Part 1:
    Simulate the spawing pattern of a school of latern fish
Part 2:

"""

from collections import Counter, defaultdict


class LaternFishSchool:
    """The LaternFishSchool class"""

    def __init__(self, school_input: str) -> None:
        """Intialize LaternFishSchool class"""
        self.school_map = self._read_school(school_input)

    @staticmethod
    def _read_school(school_input: str) -> Counter:
        """Read school"""
        fish = [int(num) for num in school_input.split(",")]
        return Counter(fish)

    def predict_size(self, days: int) -> int:
        """Predict how large the school will grow"""
        for _ in range(days):
            next_day_fish: defaultdict = defaultdict(int)
            for fish_type, count in self.school_map.items():
                if fish_type == 0:
                    next_day_fish[8] += count
                    next_day_fish[6] += count
                else:
                    next_day_fish[fish_type - 1] += count

            self.school_map = Counter(next_day_fish)

        return sum(self.school_map.values())


if __name__ == "__main__":
    with open("day_06/input.txt") as input_file:
        puzzle_input = input_file.read()

    # Part 1 answer
    latern_school = LaternFishSchool(puzzle_input)
    size = latern_school.predict_size(80)
    print(size)
    # Part 2 answer
    latern_school = LaternFishSchool(puzzle_input)
    size = latern_school.predict_size(256)
    print(size)
