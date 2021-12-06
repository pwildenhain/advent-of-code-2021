"""
Part 1:
    Simulate a round of bingo with the giant squid to determine who wins first
Part 2:
    Simulate many rounds of bingo with the giant squid to determine who wins last
"""

from typing import Optional


class Board:
    """The bingo board class"""

    def __init__(self, board_input: str) -> None:
        """Intialize board class"""
        self.board_dict = self._read_board(board_input)
        self.last_num: Optional[int] = None

    def __repr__(self) -> str:
        "Print a readable representation of the board"
        board_str = ""
        idx = 0
        for num, mark in self.board_dict.items():
            board_str += f"{ num } {mark}"
            if idx % 4 == 0 and idx != 0:
                board_str += "\n"
            else:
                board_str += " "
            idx += 1
        return board_str

    @staticmethod
    def _read_board(board_input: str) -> dict[int, str]:
        """Read board input"""
        board_nums = [
            int(num) for row in board_input.splitlines() for num in row.split()
        ]
        return {num: "_" for num in board_nums}

    def mark_number(self, number: int) -> None:
        "Mark a number on the board"
        try:
            self.board_dict[number] = "x"
        except KeyError:
            pass

    def calculate_score(self):
        "Calculate a board's final score"
        unmarked_nums = [num for num in self.board_dict if self.board_dict[num] != "x"]
        return sum(unmarked_nums) * self.last_num


class Bingo:
    """Bingo system on the submarine"""

    def __init__(self, game_input: str) -> None:
        """Initialize Bingo System"""
        self.numbers = self._read_numbers(game_input)
        self.boards = self._read_boards(game_input)
        self.win_conditions = [
            # rows
            range(0, 5),
            range(5, 10),
            range(10, 15),
            range(15, 20),
            range(20, 25),
            # columns
            range(0, 25, 5),
            range(1, 25, 5),
            range(2, 25, 5),
            range(3, 25, 5),
            range(4, 25, 5),
        ]

    @staticmethod
    def _read_numbers(game_input: str) -> list[int]:
        """Read numbers for Bingo System"""
        separated_input = game_input.split("\n\n")
        numbers = separated_input[0]
        return [int(num) for num in numbers.split(",")]

    @staticmethod
    def _read_boards(game_input: str) -> list[Board]:
        """Read boards for Bingo System"""
        separated_input = game_input.split("\n\n")
        return [Board(board_input) for board_input in separated_input[1:]]

    def is_winner(self, board: Board) -> bool:
        "Determine if a board has won a round of bingo"
        num_positions = list(board.board_dict)

        for cond in self.win_conditions:
            for idx in cond:
                num = num_positions[idx]
                if board.board_dict[num] != "x":
                    break
            else:
                return True
        return False

    def play(self) -> Board:
        "Determine the winning board of a Bingo game"
        there_is_a_winner = False
        for num in self.numbers:
            for board in self.boards:
                board.mark_number(num)
                if self.is_winner(board):
                    board.last_num = num
                    there_is_a_winner = True
                    winning_board = board
                    break
            if there_is_a_winner:
                break
        return winning_board

    def get_last_winning_board(self) -> Board:
        """Determine the last board to win in the Bingo System"""
        while len(self.boards) > 1:
            winning_board = self.play()
            self.boards.remove(winning_board)
        last_winning_board = self.play()
        return last_winning_board


if __name__ == "__main__":
    with open("day_04/input.txt") as input_file:
        puzzle_input = input_file.read()

    bingo_system = Bingo(puzzle_input)
    # Part 1 answer
    winner = bingo_system.play()
    print(f"The first board to wins score is { winner.calculate_score() }")
    # Part 2 answer
    bingo_system = Bingo(puzzle_input)
    last_winner = bingo_system.get_last_winning_board()
    print(f"The last board to wins score is { last_winner.calculate_score() }")
