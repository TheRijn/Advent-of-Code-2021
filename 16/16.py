import sys
from math import prod

LITERAL = 4
OPERATOR = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda lst: int(lst[0] > lst[1]),
    6: lambda lst: int(lst[0] < lst[1]),
    7: lambda lst: int(lst[0] == lst[1]),
}

total_version = 0


def read_bits(bits, start, n) -> tuple[str, int]:
    end = start + n
    return bits[start:end], end


def read_bits_int(bits, start, n) -> tuple[int, int]:
    number_bits, pos = read_bits(bits, start, n)
    return int(number_bits, base=2), pos


def hex_to_bits(hex: str) -> str:
    return format(int(hex, base=16), "04b")


def hex_string_to_bit_string(hex_string: str) -> str:
    return "".join([hex_to_bits(x) for x in list(hex_string)])


def parse_packet(bits) -> int:
    pos = 0
    packet_version, _ = read_bits_int(bits, pos, 3)

    global total_version
    total_version += packet_version

    type_ID, _ = read_bits_int(bits[3:], pos, 3)

    if type_ID == LITERAL:
        # print("Found: literal")
        value, next_pos = parse_literal(bits[pos:])
        # print("literal:", value)
    else:
        # print("found: operator")
        value, next_pos = parse_operator(bits[pos:])

    pos += next_pos

    return value, pos


def parse_literal(bits) -> tuple[int, int]:
    pos = 0
    packet_version, pos = read_bits_int(bits, pos, 3)

    type_ID, pos = read_bits_int(bits, pos, 3)

    number = ""

    done = False

    while not done:
        part, pos = read_bits(bits, pos, 5)

        if part[0] == "0":
            done = True

        number += part[1:]

    return int(number, base=2), pos


def parse_operator(bits) -> int:
    pos = 0
    packet_version, pos = read_bits_int(bits, pos, 3)
    type_ID, pos = read_bits_int(bits, pos, 3)

    length_type_id = bits[6]

    pos = 7

    parts = []

    if length_type_id == "0":
        total_length, pos = read_bits_int(bits, pos, 15)
        # print("total length:", total_length)
        read = 0

        while read != total_length:
            value, just_read = parse_packet(bits[pos:])
            read += just_read
            # print(f"Length was: {just_read}, total: {read} of {total_length}")
            pos += just_read
            parts.append(value)
    else:
        number_of_subs, pos = read_bits_int(bits, pos, 11)
        # print("number of subs:", number_of_subs)

        for i in range(number_of_subs):
            value, next_pos = parse_packet(bits[pos:])
            parts.append(value)
            pos += next_pos

    calculated = OPERATOR[type_ID](parts)

    return calculated, pos


if __name__ == "__main__":
    hex_string = sys.stdin.readline().strip()
    bits = hex_string_to_bit_string(hex_string)

    value, _ = parse_operator(bits)

    print("part one:", total_version)
    print("part two:", value)
