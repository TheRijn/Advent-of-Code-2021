from __future__ import annotations
import sys

bitstrings: list[str] = []

for x in sys.stdin:
    bitstrings.append(x.rstrip())

transposed_bits = zip(*bitstrings)

gamma_bit = ""
epsilon_bit = ""

for bit in transposed_bits:
    if bit.count("0") > len(bit) // 2:
        gamma_bit += "0"
        epsilon_bit += "1"
    else:
        gamma_bit += "1"
        epsilon_bit += "0"

gamma = int(gamma_bit, base=2)
epsilon = int(epsilon_bit, base=2)

print("a:", gamma * epsilon)

remaining = bitstrings

current_bit = 0
while len(remaining) > 1:
    zipped = list(zip(*remaining))
    common_value = (
        "1" if zipped[current_bit].count("1") >= zipped[current_bit].count("0") else "0"
    )
    new_bits = []

    for bits in remaining:
        if bits[current_bit] == common_value:
            new_bits.append(bits)

    remaining = new_bits

    current_bit += 1


ox_rating = int(remaining[0], base=2)

remaining = bitstrings

current_bit = 0
while len(remaining) > 1:
    zipped = list(zip(*remaining))
    least_common_value = (
        "0" if zipped[current_bit].count("1") >= zipped[current_bit].count("0") else "1"
    )
    new_bits = []

    for bits in remaining:
        if bits[current_bit] == least_common_value:
            new_bits.append(bits)

    remaining = new_bits

    current_bit += 1

co2_rating = int(remaining[0], base=2)
print("b:", ox_rating * co2_rating)
