with open("input.3") as f:
    bitstrings = [bitstring.strip() for bitstring in f.readlines()]

transpose = ["".join(tr) for tr in zip(*bitstrings)]
gamma = []
epsilon = []


def from_binary(l) -> int:
    return int("".join(l), 2)


def oxygen_criterion(bitstring):
    if bitstring.count("0") > bitstring.count("1"):
        return "0"
    else:
        return "1"


def co2_criterion(bitstring):
    if bitstring.count("0") > bitstring.count("1"):
        return "1"
    else:
        return "0"


for tr in transpose:
    gamma.append(oxygen_criterion(tr))
    epsilon.append(co2_criterion(tr))

print(from_binary(gamma) * from_binary(epsilon))


def reduce(bitstrings, criterion, i = 0):
    if len(bitstrings) == 1:
        return bitstrings[0]

    transpose = ["".join(tr) for tr in zip(*bitstrings)]
    crit = criterion(transpose[i])
    bitstrings = [bitstring for bitstring in bitstrings if bitstring[i] == crit]
    return reduce(bitstrings, criterion, i + 1)


print(
    from_binary(reduce(bitstrings, oxygen_criterion))
    * from_binary(reduce(bitstrings, co2_criterion))
)
