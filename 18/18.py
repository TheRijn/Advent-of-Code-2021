import sys


class SnailfishNumber:
    def __init__(self, pair) -> None:
        self._pair = pair
        self.reduce()

    def reduce(self):
        while self.explode():
            pass

        while self.explode():
            pass

    def explode(self) -> bool:
        pass

    def split(self) -> bool:
        pass

    def __repr__(self) -> str:
        return f"SnailfishNumber({self._pair})"

    def __str__(self) -> str:
        return self._pair

    def __add__(self, p2: "SnailfishNumber") -> "SnailfishNumber":
        return SnailfishNumber([self._pair, p2._pair])


if __name__ == "__main__":
    numbers = []

    for line in sys.stdin.readlines():
        numbers.append(SnailfishNumber(eval(line.strip())))

    print(numbers)
