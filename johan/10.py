from functools import reduce

import get

problem_input = get.input(10)

brackets = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
error_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
completion_points = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def autocomplete_score(stack):
    return reduce(
        lambda x, y: 5 * x + y, map(lambda k: completion_points[k], reversed(stack))
    )


def scores(line):
    stack = []
    for c in line:
        if c in brackets:
            stack.append(c)
        else:
            b = stack.pop()
            if brackets[b] != c:
                return error_points[c], 0
    return 0, autocomplete_score(stack)


error_scores = []
autocomplete_scores = []

for line in problem_input:
    e_score, ac_score = scores(line)
    if e_score:
        error_scores.append(e_score)
    if ac_score:
        autocomplete_scores.append(ac_score)

print(sum(error_scores))


def odd_median(array):
    return sorted(array)[len(array) // 2]


print(odd_median(autocomplete_scores))
