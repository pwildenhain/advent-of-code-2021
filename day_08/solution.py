"""
Part 1:

Part 2:

"""
from copy import deepcopy

# actual answer
# source: https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/8.py
# pylint: disable=all
# 0: abcefg (6)
# 6: abdefg (6)
# 9: abcdfg (6)

# 2: acdeg (5)
# 3: acdfg (5)
# 5: abdfg (5)

# 1: cf (2)
# 4: bcdf (4)
# 7: acf (3)
# 8: abcdefg (7)
# use this as a template for how the numbers are arranged
digits = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}


def find_perm(before) -> dict:
    """use process of elimination to determine which letters belong to which numbers"""
    A = {}
    for w in before:
        if len(w) == 2:  # 1
            cf = w
    assert len(cf) == 2, cf
    for w in before:
        if len(w) == 6 and (cf[0] in w) != (cf[1] in w):  # 6
            if cf[0] in w:
                A[cf[0]] = "f"
                A[cf[1]] = "c"
            else:
                A[cf[1]] = "f"
                A[cf[0]] = "c"
    assert len(A) == 2, f"A={A} cf={cf} {before}"
    for w in before:
        if len(w) == 3:  # 7
            for c in w:
                if c not in cf:
                    A[c] = "a"
    assert len(A) == 3, A
    for w in before:
        if len(w) == 4:  # 4
            bd = ""
            for c in w:
                if c not in cf:
                    bd += c
    assert len(bd) == 2, bd
    # 0 is length-6 and missing one of b/d. B is present; D is missing.
    # 9 is length-6 missing one of e/g. G is present; E is missing.
    for w in before:
        if len(w) == 6 and (bd[0] in w) != (bd[1] in w):  # 0
            if bd[0] in w:
                A[bd[0]] = "b"
                A[bd[1]] = "d"
            else:
                A[bd[1]] = "b"
                A[bd[0]] = "d"
    assert len(A) == 5, A
    eg = ""
    for c in ["a", "b", "c", "d", "e", "f", "g"]:
        if c not in A:
            eg += c
    assert len(eg) == 2, eg
    for w in before:
        if len(w) == 6 and (eg[0] in w) != (eg[1] in w):  # 9
            if eg[0] in w:
                A[eg[0]] = "g"
                A[eg[1]] = "e"
            else:
                A[eg[1]] = "g"
                A[eg[0]] = "e"
    assert len(A) == 7, A
    return A


if __name__ == "__main__":
    with open("day_08/input.txt") as input_file:
        puzzle_input = input_file.read()

    p1 = 0
    ans = 0

    for line in puzzle_input.splitlines():
        before, after = line.split("|")
        before = before.split()  # type: ignore
        after = after.split()  # type: ignore

        D = find_perm(before)
        ret = ""
        for w in after:
            w_perm = ""
            for c in w:
                w_perm += D[c]
            w_perm = "".join(sorted(w_perm))
            d = [k for k, v in digits.items() if v == w_perm]
            assert len(d) == 1
            if d[0] in [1, 4, 7, 8]:
                p1 += 1
            ret += str(d[0])
        ans += int(ret)
    print(p1)
    print(ans)
# pylint: enable=all
# this was my original unsuccessful attempt, where I just got part 1
# class SevenSegementDisplays:
#     """The SevenSegementDisplays class"""

#     def __init__(self, signals: str) -> None:
#         """Intialize SevenSegementDisplays class"""
#         self.signal_patterns = self._read_signals(signals)
#         self.digit_len_map = {
#             2: ["1"],
#             3: ["7"],
#             4: ["4"],
#             5: ["2", "3", "5"],
#             6: ["0", "6", "9"],
#             7: ["8"],
#         }
#         self.unique_lens = [2, 3, 4, 7]
#         self.possible_letter_positions_map = {
#             "top": ["a", "b", "c", "d", "e", "f", "g"],
#             "top left": ["a", "b", "c", "d", "e", "f", "g"],
#             "top right": ["a", "b", "c", "d", "e", "f", "g"],
#             "middle": ["a", "b", "c", "d", "e", "f", "g"],
#             "bottom left": ["a", "b", "c", "d", "e", "f", "g"],
#             "bottom right": ["a", "b", "c", "d", "e", "f", "g"],
#             "bottom": ["a", "b", "c", "d", "e", "f", "g"],
#         }
#         self.digit_positions_map = {
#             "0": [
#                 "top",
#                 "top left",
#                 "top right",
#                 "bottom left",
#                 "bottom right",
#                 "bottom",
#             ],
#             "1": ["top right", "bottom right"],
#             "2": ["top", "top right", "middle", "bottom left", "bottom"],
#             "3": ["top", "top right", "middle", "bottom right", "bottom"],
#             "4": ["top left", "top right", "middle", "bottom right"],
#             "5": ["top", "top left", "middle", "bottom right", "bottom"],
#             "6": ["top", "top left", "middle", "bottom left", "bottom right", "bottom"],
#             "7": ["top", "top right", "bottom right"],
#             "8": [
#                 "top",
#                 "top left",
#                 "top right",
#                 "middle",
#                 "bottom left",
#                 "bottom right",
#                 "bottom",
#             ],
#             "8": ["top", "top left", "top right", "middle", "bottom right", "bottom"],
#         }

#     @staticmethod
#     def _read_signals(signals: str) -> dict[tuple[str, ...], tuple[str, ...]]:
#         """Read signals"""
#         signals_list = [signal.split(" | ") for signal in signals.splitlines()]

#         return {
#             tuple(signal_pattern.split()): tuple(output_value.split())
#             for signal_pattern, output_value in signals_list
#         }

#     def count_unique_digits(self) -> int:
#         unique_digit_count = 0

#         for output_values in self.signal_patterns.values():
#             output_lens = [len(output_value) for output_value in output_values]
#             for output_len in output_lens:
#                 if output_len in self.unique_lens:
#                     unique_digit_count += 1

#         return unique_digit_count

#     def build_unique_digit_letter_map(
#         self, signal_pattern: tuple[str, ...]
#     ) -> dict[str, list[str]]:
#         unique_digit_letter_map = {}
#         for pattern in signal_pattern:
#             pattern_len = len(pattern)
#             if pattern_len in self.unique_lens:
#                 digit = self.digit_len_map[pattern_len][0]
#                 unique_digit_letter_map[digit] = [letter for letter in pattern]

#         return unique_digit_letter_map

#     # this is not going to work...
#     # need to just use regular deduction logic
#     @staticmethod
#     def reduce_letter_positions_map(letter_positions_map: dict[str, list[str]]) -> dict[str, list[str]]:
#         all_letters_solved = False
#         breakpoint()
#         while not all_letters_solved:
#             for letters in letter_positions_map.values():
#                 if len(letters) == 1:
#                     unique_letter = letters[0]
#                     continue
#                 try:
#                     letters.remove(unique_letter)
#                 except NameError:
#                     # we haven't found a unique letter yet
#                     pass
#                 except ValueError:
#                     # letter doesn't exist in the list
#                     pass
#             all_letters_solved = all([len(letters) == 1 for letters in letter_positions_map.values()])

#         return letter_positions_map


#     def build_digit_letter_map(
#         self, signal_pattern: tuple[str, ...]
#     ) -> dict[str, list[str]]:
#         possible_letter_positions_map = deepcopy(self.possible_letter_positions_map)
#         digit_letter_map = self.build_unique_digit_letter_map(signal_pattern)
#         for digit, digit_letters in digit_letter_map.items():
#             digit_positions = self.digit_positions_map[digit]
#             # remove everything from the digit positions that isn't that letter
#             for position in digit_positions:
#                 possible_letters = possible_letter_positions_map[position]
#                 for possible_letter in possible_letters:
#                     if possible_letter not in digit_letters:
#                         try:
#                             possible_letters.remove(possible_letter)
#                         except ValueError:
#                             # letter has already been removed as a possibility
#                             pass
#             # for all remaining positions, remove the digit letters as a possibility
#             remaining_positions = list(
#                 set(possible_letter_positions_map.keys()).symmetric_difference(
#                     set(digit_positions)
#                 )
#             )
#             for position in remaining_positions:
#                 possible_letters = possible_letter_positions_map[position]
#                 for possible_letter in possible_letters:
#                     if possible_letter in digit_letters:
#                         try:
#                             possible_letters.remove(possible_letter)
#                         except ValueError:
#                             # letter has already been removed as a possibility
#                             pass

#         return self.reduce_letter_positions_map(possible_letter_positions_map)

#     @staticmethod
#     def decode_output_value(
#         digit_letter_map: dict[str, set[str]], output_value: tuple[str, ...]
#     ) -> int:
#         output_str = ""
#         for value in output_value:
#             letter_set = {letter for letter in value}
#             for digit, digit_letter_set in digit_letter_map.items():
#                 if letter_set == digit_letter_set:
#                     output_str += digit

#         return int(output_str)


# if __name__ == "__main__":
#     with open("day_08/input.txt") as input_file:
#         puzzle_input = input_file.read()

#     # Part 1 answer
#     seven_segment_displays = SevenSegementDisplays(puzzle_input)
#     print(seven_segment_displays.count_unique_digits())
#     # Part 2 answer
#     print(
#         seven_segment_displays.build_unique_digit_letter_map(
#             [
#                 "be",
#                 "cfbegad",
#                 "cbdgef",
#                 "fgaecd",
#                 "cgeb",
#                 "fdcge",
#                 "agebfd",
#                 "fecdb",
#                 "fabcd",
#                 "edb",
#             ]
#         )
#     )
#     print(
#         seven_segment_displays.build_digit_letter_map(
#             [
#                 "be",
#                 "cfbegad",
#                 "cbdgef",
#                 "fgaecd",
#                 "cgeb",
#                 "fdcge",
#                 "agebfd",
#                 "fecdb",
#                 "fabcd",
#                 "edb",
#             ]
#         )
#     )
