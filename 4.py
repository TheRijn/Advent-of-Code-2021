import numpy as np


def has_bingo(board: np.ndarray) -> bool:
    for row in board:
        if np.all(row == -1):
            return True

    for col in board.T:
        if np.all(col == -1):
            return True

    return False


def part_one(boards, number):
    for number in numbers:
        boards[boards == number] = -1

        for board in boards:
            if has_bingo(board):
                return board[board != -1].sum() * number


def part_two(boards: np.ndarray, number):
    for number in numbers:
        boards[boards == number] = -1

        done_boards = []

        for b, board in enumerate(boards):
            if has_bingo(board):
                done_boards.append(b)

        if len(boards) == 1 and len(done_boards) == 1:
            board = boards[0]
            return board[board != -1].sum() * number

        boards = np.delete(boards, done_boards, 0)


if __name__ == "__main__":
    numbers = [int(x) for x in input().split(",")]

    input()  # Skip blank line

    boards = []

    try:
        while True:
            current_board = []
            while (line := input().strip()) != "":
                current_board.append([int(x) for x in line.split()])
            boards.append(current_board)
    except EOFError:
        boards.append(current_board)

    boards = np.array(boards)

    print("Winning board:", part_one(boards.copy(), numbers))

    print("Losing board :", part_two(boards.copy(), numbers))
