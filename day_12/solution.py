# pylint: disable=all
# courtesy of jonathon paulson: https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/12.py

from collections import defaultdict, deque

with open("day_12/input.txt") as input_file:
    puzzle_input = input_file.read()
# adjacency list - for each vertex, what vertices does it have edges to?
E = defaultdict(list)
for line in puzzle_input.splitlines():
    a, b = line.strip().split("-")
    E[a].append(b)
    E[b].append(a)


def solve(p1):
    start = ("start", set(["start"]), None)
    ans = 0
    # the various states of our search
    Q = deque([start])
    while Q:
        print(Q)
        # where we are, which small caves we've visited
        pos, small, twice = Q.popleft()
        if pos == "end":
            ans += 1
            continue
        for y in E[pos]:
            if y not in small:
                new_small = set(small)
                if y.lower() == y:
                    new_small.add(y)
                Q.append((y, new_small, twice))
            elif y in small and twice is None and y not in ["start", "end"] and not p1:
                Q.append((y, small, y))
    return ans


print(solve(p1=True))
# print(solve(p1=False))
# my best shot below. Just look up the answer tomorrow
# from collections import defaultdict
# from typing import DefaultDict, Optional
# class Caves:
#     """The Something class"""

#     def __init__(self, paths: str) -> None:
#         """Intialize Something class"""
#         self.cave_dict = self._read_paths(paths)

#     @staticmethod
#     def _read_paths(paths: str) -> DefaultDict[str, set[str]]:
#         """Read paths]"""
#         cave_dict = defaultdict(set)
#         for path in paths.splitlines():
#             path_start, path_end = path.split("-")
#             cave_dict[path_start].add(path_end)
#             cave_dict[path_end].add(path_start)

#         return cave_dict

#     def find_distinct_paths(
#         self,
#         start_cave: str = "start",
#         visited_caves: Optional[list[str]] = None,
#     ) -> tuple[list[str], Optional[list[str]]]:
#         distinct_paths = []
#         next_caves = self.cave_dict[start_cave]
#         print(f"{start_cave=}")
#         if not visited_caves:
#             visited_caves = []
#         if is_tiny_cave and start_cave in visited_caves:
#             # hit a dead end, return an empty result
#             print(f"dead end {start_cave}")
#             return [], []
#         visited_caves += [start_cave]
#         print(f"exploring {next_caves=}")
#         for cave in next_caves:
#             is_tiny_cave = cave == cave.lower()
#             if is_tiny_cave and cave in visited_caves:
#                 # already been to this cave, not going to visit again
#                 print(f"skipping {cave=}")
#                 continue
#             print(f"visiting {cave=}")
#             visited_caves += [cave]
#             print(f"current {visited_caves=}")
#             if cave == "end":
#                 # mark as a distinct visited_caves, now reset the little caves visited
#                 # and move on to the next cave
#                 print(f"made to the end with {visited_caves=}")
#                 distinct_paths += [visited_caves]
#                 visited_caves = []
#                 continue

#             search_result = self.find_distinct_paths(cave, visited_caves)
#             next_distinct_paths, visited_caves = search_result
#             if not next_distinct_paths:
#                 # couldn't get the end, try another route
#                 continue

#             distinct_paths += next_distinct_paths
#         print(f"returning {distinct_paths=} and {visited_caves=}")
#         return distinct_paths, visited_caves

# # I want a recursive function that returns a list of possible paths through a cave, given a starting point
# # start with the starting point
# # find the adjacent caves
# # for each cave:
#     # if it's a little cave, check if we've been there
#     #   if we have, then skip to the next adjacent cave
#     # if it's the 'start' cave, skip to the next adjacent cave
#     # if it's a little cave, mark that we've been there
#     # add this cave to our previously visited caves
#     # if it's the end cave, return all visited caves
#     # else find the adjacent caves


# if __name__ == "__main__":
#     with open("day_12/input.txt") as input_file:
#         puzzle_input = input_file.read()

#     # Part 1 answer
#     caves = Caves(puzzle_input)
#     print(caves.cave_dict)
#     print(caves.find_distinct_paths())
#     # Part 2 answer
#     print()
