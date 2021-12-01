import sys

depths = []

for line in sys.stdin:
    depths.append(int(line))

total = 0
for i in range(1, len(depths)):
    if depths[i - 1] < depths[i]:
        total += 1

print("a:", total)


prev = 1000000
total = 0
for i in range(len(depths) - 2):
    new = sum(depths[i : i + 3])

    if new > prev:
        total += 1
    prev = new

print("b:", total)
