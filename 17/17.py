from typing import Optional

target_t = tuple[tuple[int, int], tuple[int, int]]

START = (0, 0)


class Nope(Exception):
    pass


def step_y(y: int) -> int:
    return y - 1


def step_x(x: int) -> int:
    if x == 0:
        return 0
    elif x > 0:
        return x - 1
    else:
        return x + 1


def pos_in_target(x: int, y: int, target: target_t) -> bool:
    if x > target[0][1] or y < target[1][0]:
        raise Nope

    if x < target[0][0] or y > target[1][1]:
        return False

    return True


def brute_force(target: target_t):
    best_y = 0

    values_found = 0

    for x0 in range(1, 200):
        for y0 in range(-100, 100):
            new_y = run_velocity(x0, y0, target)

            if new_y is not None:
                values_found += 1

                if new_y > best_y:
                    best_y = new_y

    return best_y, values_found


def run_velocity(dx: int, dy: int, target: target_t) -> Optional[int]:
    x, y = START

    max_y = 0

    try:
        while True:
            x += dx
            y += dy

            max_y = max(y, max_y)

            if pos_in_target(x, y, target):
                return max_y

            dx = step_x(dx)
            dy = step_y(dy)

    except Nope:
        return None


if __name__ == "__main__":
    import re, sys

    expression = r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)"
    match = re.match(expression, sys.stdin.readline())

    if not match:
        exit(1)

    numbers = [int(x) for x in match.groups()]
    target: target_t = ((numbers[0], numbers[1]), (numbers[2], numbers[3]))

    best, n = brute_force(target)

    print("Part one:", best)
    print("Part two:", n)
