
with open("inputs/3.txt") as f:
    bits = [bit.strip() for bit in f.readlines()]


def cols(rows: list[str], idx: int) -> str:
    for row in rows:
        yield row[idx]


def invert(bits: str) -> str:
    return ''.join('1' if bit == '0' else '0' for bit in bits)


def from_bits(bits: str) -> int:
    return int(bits, 2)


def most_common(bits: str) -> str:
    return "0" if bits.count("0") > bits.count("1") else "1"


gamma = "".join(most_common("".join(cols(bits, col))) for col in range(len(bits[0])))
epsilon = invert(gamma)

print("gamma:", from_bits(gamma))
print("epsilon:",from_bits(epsilon))
print("power: ", from_bits(gamma) * from_bits(epsilon))


def oxygen_criterion(bits):
    return "0" if bits.count("0") > bits.count("1") else "1"


def co2_criterion(bits):
    return "1" if bits.count("0") > bits.count("1") else "0"


def reduce(criterion):

    candiates = bits.copy()
    column = 0

    while len(candiates) != 1:

        remove = set()
        c = criterion(list(cols(candiates, column)))

        remove = set(idx for idx, candiate in enumerate(candiates) if c != candiate[column])
        candiates = [bits for idx, bits in enumerate(candiates) if idx not in remove]
        column += 1

    return candiates[0]


# First 4989288, 3910368
print("")
print("oxygen:", from_bits(reduce(oxygen_criterion)))
print("co2:", from_bits(reduce(co2_criterion)))

print("life support rating:", from_bits(reduce(oxygen_criterion)) * from_bits(reduce(co2_criterion)))
