from argparse import ArgumentParser
from collections import defaultdict

NEW_FISH = 8
RELOAD_FISH = 6


def simulate_slow(days):
    fishes = [int(x) for x in input().split(",")]

    for _ in range(days):
        new_fish = []
        for i, _ in enumerate(fishes):
            fishes[i] -= 1
            if fishes[i] == -1:
                fishes[i] = RELOAD_FISH
                new_fish.append(NEW_FISH)
        fishes += new_fish

    return len(fishes)


def simulate(days):
    fishes_list = [int(x) for x in input().split(",")]
    fishes: defaultdict[int, int] = defaultdict(int)

    for fish in fishes_list:
        fishes[fish] += 1

    for _ in range(days):
        next = defaultdict(int)

        for timer, n in fishes.items():
            if timer == 0:
                next[NEW_FISH] += n
                next[RELOAD_FISH] += n
            else:
                next[timer - 1] += n

        fishes = next

    return sum(fishes.values())


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("days", nargs="?", default=80, type=int)
    parser.add_argument("--slow", "-s", action="store_true")
    args = parser.parse_args()

    if args.slow:
        if args.days > 80:
            print("Are you sure?")
        print(simulate_slow(args.days))
    else:
        print(simulate(args.days))
