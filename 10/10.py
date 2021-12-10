import sys


class InvalidChar(Exception):
    pass


PAIRS = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

SCORE_ONE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

SCORE_TWO = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def part_one(lines: list[str]) -> int:
    score = 0
    for line in lines:
        try:
            stack = []
            for char in list(line):
                # Open backets
                if char in PAIRS.values():
                    stack.append(char)

                # Close brackets
                elif char in PAIRS:
                    top = stack.pop()
                    if top != PAIRS[char]:
                        score += SCORE_ONE[char]
                        raise InvalidChar
        except InvalidChar:
            pass
    return score


def part_two(lines: list[str]) -> int:
    scores = []
    for line in lines:
        score = 0
        try:
            stack = [None]
            for char in list(line):
                # Open backets
                if char in PAIRS.values():
                    stack.append(char)

                # Close brackets
                elif char in PAIRS:
                    top = stack.pop()
                    if top != PAIRS[char]:
                        raise InvalidChar

            # Check not closed brackets
            while top := stack.pop():
                score = score * 5 + SCORE_TWO[top]

            scores.append(score)
        except InvalidChar:
            pass

    scores.sort()

    return scores[len(scores) // 2]


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    print("Part one:", part_one(lines))
    print("Part two:", part_two(lines))
