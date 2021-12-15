class InvalidChar(Exception):
    pass


OPEN = ["(", "[", "{", "<"]
CLOSE = [")", "]", "}", ">"]

CLOSING_FOR_OPEN = dict(zip(CLOSE, OPEN))

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
                if char in OPEN:  # Open backets
                    stack.append(char)
                elif char in CLOSE:  # Close brackets
                    top = stack.pop()

                    if top != CLOSING_FOR_OPEN[char]:
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
            stack: list[str] = []

            for char in list(line):
                if char in CLOSING_FOR_OPEN.values():  # Open backets
                    stack.append(char)
                elif char in CLOSING_FOR_OPEN:  # Close brackets
                    top = stack.pop()

                    if top != CLOSING_FOR_OPEN[char]:
                        # Ignore invalid lines
                        raise InvalidChar

            # Close unclosed pairs
            while stack:
                score = score * 5 + SCORE_TWO[stack.pop()]

            scores.append(score)

        except InvalidChar:
            pass

    scores.sort()

    return scores[len(scores) // 2]


if __name__ == "__main__":
    import sys

    lines = sys.stdin.readlines()

    print("Part one:", part_one(lines))
    print("Part two:", part_two(lines))
