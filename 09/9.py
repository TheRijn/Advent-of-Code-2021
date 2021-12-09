import sys
import matplotlib.pyplot as plt
import numpy as np

from collections import defaultdict
from typing import Optional


def indeces(y, x):
    return [
        (y - 1, x),  # N
        (y, x + 1),  # E
        (y + 1, x),  # S
        (y, x - 1),  # W
    ]


def is_low_point(grid: np.ndarray, y: int, x: int) -> bool:
    current = grid[y, x]

    for index in indeces(y, x):
        try:
            if index[0] < 0 or index[1] < 0:
                raise IndexError
            if grid[index] <= current:
                return False
        except IndexError:
            pass

    return True


def lowest_neighbour(grid: np.ndarray, y: int, x: int) -> Optional[tuple[int, int]]:
    lowest = grid[y, x]
    point = None

    for index in indeces(y, x):
        try:
            if index[0] < 0 or index[1] < 0:
                raise IndexError

            if (new := grid[index]) < lowest:
                lowest = new
                point = index
        except IndexError:
            pass

    return point


def heatmap(grid):
    plt.imshow(grid, cmap="Greys", interpolation="nearest")
    # plt.savefig("heat.png")
    plt.show()


def part_one(grid: np.ndarray):
    low_points = np.empty_like(grid, dtype=bool)

    for point in np.ndindex(grid.shape):
        low_points[point] = is_low_point(grid, *point)

    return sum(grid[low_points] + 1)


def part_two(grid: np.ndarray):
    smoke_direction = np.empty_like(grid, dtype=tuple)

    for point in np.ndindex(grid.shape):
        smoke_direction[point] = lowest_neighbour(grid, *point)

    basins = defaultdict(int)

    for starting_point, height in np.ndenumerate(grid):
        if height == 9:
            continue

        point = starting_point
        while (next := smoke_direction[point]) is not None:
            point = next

        basins[point] += 1

    return np.prod(sorted(basins.values(), reverse=True)[:3])


if __name__ == "__main__":
    import sys

    grid_lists = []

    for line in sys.stdin.readlines():
        grid_lists.append([int(x) for x in list(line.strip())])

    grid = np.array(grid_lists)

    print("Part One:", part_one(grid))
    print("Part Two:", part_two(grid))
