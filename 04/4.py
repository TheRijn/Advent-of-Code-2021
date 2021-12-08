import numpy as np


def bingo_in_lines(lines: np.ndarray) -> bool:
    for line in lines:
        if np.all(line == -1):
            return True
    return False


def bingo_in_board(board: np.ndarray) -> bool:
    return bingo_in_lines(board) or bingo_in_lines(board.T)


def board_score(board: np.ndarray, number: int) -> int:
    return board[board != -1].sum() * number


def part_one(boards: np.ndarray, numbers: list[int]):
    for number in numbers:
        boards[boards == number] = -1

        for board in boards:
            if bingo_in_board(board):
                return board_score(board, number)


def part_two(boards: np.ndarray, numbers: list[int]):
    for number in numbers:
        boards[boards == number] = -1

        done_boards = []

        for b, board in enumerate(boards):
            if bingo_in_board(board):
                done_boards.append(b)

        if len(boards) == 1 and len(done_boards) == 1:
            board = boards[0]
            return board_score(board, number)

        boards = np.delete(boards, done_boards, axis=0)


if __name__ == "__main__":
    import sys

    numbers = [int(x) for x in input().split(",")]

    input()  # Skip blank line

    boards = []

    current_board = []

    for line in sys.stdin:
        if line != "\n":
            current_board.append([int(x) for x in line.split()])
        else:
            boards.append(current_board)
            current_board = []

    np_boards = np.array(boards)

    print("Winning board:", part_one(np_boards.copy(), numbers))

    print("Losing board :", part_two(np_boards.copy(), numbers))
