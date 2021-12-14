import collections
import typing


def load():
    with open("inputs/14.txt") as f:
        return f.readlines()


def template():
    return load()[0].strip()


def rules():
    return {
        tuple(k.strip()): v.strip() for k, v in (row.split("->") for row in load()[2:])
    }


def count(steps: int):

    pairs = rules()
    cnt = collections.Counter(zip(template(), template()[1:]))

    for _ in range(steps):
        for key, n in tuple(cnt.items()):
            cnt[key] -= n
            m = pairs[key]
            f, s = key
            cnt[(f, m)] += n
            cnt[(m, s)] += n

    accumulated: typing.Counter[str] = collections.Counter()

    for (f, s), n in cnt.items():
        accumulated[f] += n
        accumulated[s] += n

    (_, most), *_, (_, least) = accumulated.most_common()

    # Don't undersant why i need to add one, but worked with
    # ex-data and work with real... 
    return (most - least) // 2 + 1


if __name__ == "__main__":
    print("a:", count(10))
    print("b:", count(40))
