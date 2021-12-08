import sys
import numpy as np

EASY_LENGTHS = np.array([2, 4, 3, 7])

vec_len = np.vectorize(len)


def part_one(lines):

    total = 0

    for line in lines:
        digits, output_str = line.split("|")
        digits = digits.split()
        output_value: np.ndarray = output_str.split()
        lengths: np.ndarray = vec_len(output_value)
        for length in lengths:
            if length in EASY_LENGTHS:
                total += 1

    return total


def part_two(lines):
    total = 0

    for line in lines:
        digits, output_str = line.split("|")
        digits = np.array([frozenset(list(x)) for x in digits.split()])

        output_value: np.ndarray = np.array(
            [frozenset(list(x)) for x in output_str.split()]
        )

        lengths: np.ndarray = vec_len(digits)

        mapping = {}

        # Get easy mappings
        mapping[1] = digits[lengths == 2][0]
        mapping[4] = digits[lengths == 4][0]
        mapping[7] = digits[lengths == 3][0]
        mapping[8] = digits[lengths == 7][0]

        digits = digits[digits != mapping[1]]
        digits = digits[digits != mapping[4]]
        digits = digits[digits != mapping[7]]
        digits = digits[digits != mapping[8]]
        lengths: np.ndarray = vec_len(digits)

        # 3: length 5, superset of 7
        mapping[3] = digits[(lengths == 5) & (mapping[7] <= digits)][0]
        digits = digits[digits != mapping[3]]
        lengths: np.ndarray = vec_len(digits)

        # 5: length 5, 3 parts of 4
        digits_5 = digits[lengths == 5]
        mapping[5] = digits_5[vec_len(digits_5 & mapping[4]) == 3][0]
        digits = digits[digits != mapping[5]]
        lengths: np.ndarray = vec_len(digits)

        # 2: Remaining length 5
        mapping[2] = digits[lengths == 5][0]
        digits = digits[digits != mapping[2]]
        del lengths  # make sure the invalid list isn't used anymore

        # -- Only length 6 left

        # 9: superset of 4
        mapping[9] = digits[mapping[4] <= digits][0]
        digits = digits[digits != mapping[9]]

        # 0: superset of 7
        mapping[0] = digits[mapping[7] <= digits][0]
        digits = digits[digits != mapping[0]]

        assert len(digits) == 1

        # 6: remaining
        mapping[6] = digits[0]

        decode_mapping = {v: str(k) for k, v in mapping.items()}

        total += int("".join([decode_mapping[x] for x in output_value]))

    return total


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    print("Part one:", part_one(lines))
    print("Part two:", part_two(lines))
