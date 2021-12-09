from pprint import pprint
import numpy as np
import sys

np.set_printoptions(
    threshold=sys.maxsize,
    # linewidth=1000,
)


def is_low_point(grid: np.ndarray, y: int, x: int) -> bool:
    current = grid[y, x]

    indexies = [
        (y - 1, x),  # N
        (y, x + 1),  # E
        (y + 1, x),  # S
        (y, x - 1),  # W
    ]

    for index in indexies:
        try:
            if grid[index] <= current:
                return False
        except IndexError:
            pass

    return True


def part_one(grid: np.ndarray):
    low_points = np.empty_like(grid, dtype=bool)

    for point in np.ndindex(grid.shape):
        low_points[point] = is_low_point(grid, *point)

    # print(str(grid).replace(" ", ""))
    # print(str(low_points).replace(" True", "o").replace("False", ".").replace(" ", ""))
    # print(grid[low_points] + 1)

    return sum(grid[low_points] + 1)


if __name__ == "__main__":
    import sys

    grid_lists = []

    for line in sys.stdin.readlines():
        grid_lists.append([int(x) for x in list(line.strip())])

    print("Part One:", part_one(grid))
