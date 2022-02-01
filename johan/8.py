from collections import defaultdict
import get

problem_input = get.input(8)

problem_input = [line.split() for line in problem_input]
inputs = [line[:10] for line in problem_input]
outputs = [line[-4:] for line in problem_input]

print(sum(sum(map(lambda x: len(x) in {2, 3, 4, 7}, out)) for out in outputs))

# sort
inputs = [["".join(sorted(x)) for x in line] for line in inputs]
outputs = [["".join(sorted(x)) for x in line] for line in outputs]


def str_diff(string, it):
    return "".join(x for x in string if x not in it)


def decode(digits):
    mapping = defaultdict(list)
    for x in digits:
        mapping[len(x)].append("".join(sorted(x)))

    #  0000
    # 1    2
    # 1    2
    #  3333
    # 4    5
    # 4    5
    #  6666

    tr = {}
    tr[0] = str_diff(mapping[3][0], one := mapping[2][0])
    # 2, 3, 4
    diag = str_diff("abcdefg", set.intersection(*(set(x) for x in mapping[6])))
    tr[5] = str_diff(one, diag)
    tr[2] = str_diff(one, tr[5])
    # 3, 4
    three_four = str_diff(diag, tr[2])
    tr[4] = str_diff(three_four, mapping[4][0])
    tr[3] = str_diff(three_four, tr[4])
    # 1, 3
    one_three = str_diff(mapping[4][0], one)
    tr[1] = str_diff(one_three, tr[3])
    tr[6] = str_diff("abcdefg", [tr[i] for i in range(6)])

    return mapping, tr


total = 0
for digits, out in zip(inputs, outputs):
    mapping, tr = decode(digits)

    recipe = {
        0: (0, 1, 2, 4, 5, 6),
        1: (2, 5),
        2: (0, 2, 3, 4, 6),
        3: (0, 2, 3, 5, 6),
        4: (1, 2, 3, 5),
        5: (0, 1, 3, 5, 6),
        6: (0, 1, 3, 4, 5, 6),
        7: (0, 2, 5),
        8: (0, 1, 2, 3, 4, 5, 6),
        9: (0, 1, 2, 3, 5, 6),
    }
    d = {"".join(sorted([tr[i] for i in v])): str(k) for k, v in recipe.items()}

    total += int("".join(d[signal] for signal in out))

print(total)
