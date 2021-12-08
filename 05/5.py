import numpy as np


def get_points(coord, part_one=False):
    if (
        part_one
        and abs(coord[0, 0] - coord[1, 0]) > 0
        and abs(coord[0, 1] - coord[1, 1]) > 0
    ):
        return []

    size = max([abs(coord[0, 0] - coord[1, 0]), abs(coord[0, 1] - coord[1, 1])]) + 1

    x_space = np.linspace(coord[0, 0], coord[1, 0], size, dtype=np.int64)
    y_space = np.linspace(coord[0, 1], coord[1, 1], size, dtype=np.int64)

    return np.column_stack((x_space, y_space))


def fill_grid(coords: np.array, max_x: int, max_y: int, part_one=False):
    grid = np.zeros((max_x, max_y), dtype=np.int64)

    for coord in coords:
        points = get_points(coord, part_one=part_one)

        for point in points:
            grid[tuple(point)] += 1

    return len(grid[grid >= 2])


if __name__ == "__main__":
    import sys
    import re

    lines = sys.stdin.readlines()

    coords = []

    coords_re = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
    for line in lines:
        result = coords_re.search(line)
        coords.append(
            [[result.group(1), result.group(2)], [result.group(3), result.group(4)]],
        )

    coords_np = np.array(coords, dtype=np.int64)

    max_x = coords_np[:, :, 0].max() + 1
    max_y = coords_np[:, :, 1].max() + 1

    print(fill_grid(coords_np, max_x, max_y, part_one=True))

    print(fill_grid(coords_np, max_x, max_y, part_one=False))
