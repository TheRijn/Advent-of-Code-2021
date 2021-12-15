import numpy as np
from heapq import heappush, heappop
import sys


def neighbors(pos: tuple[int, int], shape):
    n = []
    if pos[0] > 0:
        n.append((pos[0] - 1, pos[1]))
    if pos[1] > 0:
        n.append((pos[0], pos[1] - 1))
    if pos[0] != shape[0] - 1:
        n.append((pos[0] + 1, pos[1]))
    if pos[1] != shape[1] - 1:
        n.append((pos[0], pos[1] + 1))

    return n


def dijkstra(grid):
    dist = np.full_like(grid, np.iinfo(np.int64).max)

    q = []

    heappush(q, (0, (0, 0)))
    dist[0, 0] = 0

    while q:
        dist_u, u = heappop(q)

        if dist[u] < dist_u:
            continue

        for neighbour in neighbors(u, grid.shape):
            if dist[neighbour] > dist[u] + grid[neighbour]:
                dist[neighbour] = dist[u] + grid[neighbour]
                heappush(q, (dist[neighbour], neighbour))

    return dist[(grid.shape[0] - 1, grid.shape[1] - 1)]


def multiply_grid(grid: np.ndarray, n=5) -> np.ndarray:

    for axis in range(2):
        to_copy = grid.copy()

        for i in range(1, n):
            new = to_copy + i
            grid = np.concatenate([grid, new], axis=axis)

    grid[grid > 9] -= 9

    return grid


if __name__ == "__main__":
    import sys

    grid = np.array(
        [[int(x) for x in list(line.strip())] for line in sys.stdin.readlines()]
    )
    print("Part one:", dijkstra(grid))
    print("Part two:", dijkstra(multiply_grid(grid)))
