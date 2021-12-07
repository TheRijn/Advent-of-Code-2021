import numpy as np


def part_one(crabs: np.ndarray):

    smallest_diff = np.inf

    for i in range(1, crabs.max()):
        cost = abs(crabs - i).sum()
        smallest_diff = min(smallest_diff, cost)

    return smallest_diff


def part_two(crabs):
    smallest_diff = np.inf

    for i in range(1, crabs.max()):
        diffs = abs(crabs - i) + 1

        cost = sum([np.arange(diff, dtype=np.int64).sum() for diff in diffs])

        smallest_diff = min(smallest_diff, cost)

    return smallest_diff


if __name__ == "__main__":
    crabs = np.array([int(x) for x in input().split(",")])
    print("Part One:", part_one(crabs))
    print("Part Two:", part_two(crabs))
