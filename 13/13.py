import sys
import numpy as np
import re

np.set_printoptions(threshold=sys.maxsize, linewidth=1000)


def print_sheet(grid):
    print(
        str(grid)
        .replace("[", "")
        .replace("]", "")
        .replace(" ", "")
        .replace("True", "▓")
        .replace("False", "░")
    )


def part_one(points: np.ndarray, folds: list[tuple[str, int]], part_one=True):
    x_max = folds[0][1] * 2 if folds[0][0] == "x" else folds[1][1] * 2
    y_max = folds[0][1] * 2 if folds[0][0] == "y" else folds[1][1] * 2

    grid = np.full((y_max + 1, x_max + 1), False)

    grid[tuple(points.T)] = True

    if part_one:
        grid = do_fold(grid, folds[0])
        return np.count_nonzero(grid)

    for fold in folds:
        grid = do_fold(grid, fold)

    print_sheet(grid)


def do_fold(grid: np.ndarray, fold: tuple[str, int]) -> np.ndarray:
    if fold[0] == "x":
        grid = grid.T

    top_part = grid[: fold[1]]

    bottom_part = grid[fold[1] + 1 :][::-1]

    grid = top_part | bottom_part

    if fold[0] == "x":
        grid = grid.T

    return grid


if __name__ == "__main__":
    points_lst = []

    while (line := sys.stdin.readline()) != "\n":
        points_lst.append(tuple([int(x) for x in line.split(",")][::-1]))

    points = np.array(points_lst)

    folds = []

    fold_line = re.compile(r"fold along ([xy])=(\d*)")

    for line in sys.stdin.readlines():
        match = fold_line.match(line)
        folds.append((match.groups()[0], int(match.groups()[1])))

    print("Part one:", part_one(points, folds))

    print("Part two:")
    part_one(points, folds, part_one=False)
