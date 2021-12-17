import sys
from collections import defaultdict


def part_x(template: str, pairs: list[tuple[str, str, str]], iterations=10) -> int:
    duos = defaultdict(int)

    for i in range(len(template) - 1):
        duos[template[i : i + 2]] += 1

    for i in range(iterations):
        next_duos = defaultdict(int)

        for duo, n in duos.items():
            inserted = pairs[duo]
            next_duos[duo[0] + inserted] += n
            next_duos[inserted + duo[1]] += n

        duos = next_duos

    letter_counts = count_occurrences(duos, template)

    return max(letter_counts.values()) - min(letter_counts.values())


def count_occurrences(duos: dict[str, int], template: str):
    letter_counts = defaultdict(int)

    letter_counts[template[0]] = 1
    letter_counts[template[-1]] = 1

    for duo, count in duos.items():
        letter_counts[duo[0]] += count
        letter_counts[duo[1]] += count

    letter_counts = dict(map(lambda kv: (kv[0], kv[1] // 2), letter_counts.items()))

    return letter_counts


if __name__ == "__main__":
    template = sys.stdin.readline().strip()
    sys.stdin.readline()

    pairs = {}

    for line in sys.stdin.readlines():
        A = line[0:2]
        C = line[6]
        pairs[A] = C

    print("Part One:", part_x(template, pairs))
    print("Part Two:", part_x(template, pairs, 40))
