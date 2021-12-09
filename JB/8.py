import itertools


def load():
    with open("inputs/8.txt") as f:
        ios = f.readlines()

    for io in ios:
        i, o = io.strip().split("|")
        yield (
            tuple("".join(sorted(x)) for x in i.strip().split()),
            tuple("".join(sorted(x)) for x in o.strip().split()),
        )


# First 195
def a():
    return sum(sum(1 for x in o if len(x) in (2, 3, 4, 7)) for _, o in load())


SEVENS = "abcdefg"
DIGITS = {
    "cf": 1,
    "acf": 7,
    "bcdf": 4,
    "abdfg": 5,
    "acdeg": 2,
    "acdfg": 3,
    "abcefg": 0,
    "abdefg": 6,
    "abcdfg": 9,
    "abcdefg": 8,
}


def brute(lhs):
    def valid(m):
        for key in map(lambda x: "".join(sorted(m[n] for n in x)), lhs):
            try:
                DIGITS[key]
            except KeyError:
                return False
        return True

    for perm in itertools.permutations(SEVENS, 7):
        m = dict(zip(perm, SEVENS))
        if valid(m):
            return m

    raise RuntimeError("No found")


def b():
    def _decoder():
        for lhs, rhs in load():
            maps = brute(lhs)
            decoded = ["".join(sorted(maps[x] for x in r)) for r in rhs]
            yield int("".join(str(DIGITS[n]) for n in decoded))

    return sum(_decoder())


print("a:", a())
print("b:", b())
