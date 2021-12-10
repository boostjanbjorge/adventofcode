import collections
import statistics as st


def load():
    with open("inputs/10.txt") as f:
        return tuple(tuple(c.strip()) for c in f.readlines())


def points_a(c):
    return {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }[c]


def points_b(c):
    return {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }[c]


def opening():
    return ("(", "[", "{", "<")


def closing():
    return (")", "]", "}", ">")


def chunks():
    return dict(zip(opening(), closing()))


def balanced(row):
    stack = collections.deque()
    illegal = []
    for op in row:
        if op in opening():
            stack.append(op)
        else:
            if stack and op != chunks()[stack[-1]]:
                illegal.append(op)
            if stack:
                stack.pop()
    return illegal


def close(row):
    row = list(row)
    while True:
        n = None
        for idx in range(len(row) - 1):
            if row[idx] in opening() and chunks()[row[idx]] == row[idx + 1]:
                n = idx
                break
        if n is not None:
            del row[idx + 1]
            del row[idx]
        if n is None:
            return "".join(chunks()[r] for r in reversed(row))


def b():
    for row in load():
        if not balanced(row):
            acc = 0
            for char in close(row):
                acc *= 5
                acc += points_b(char)
            yield acc


print("a:", sum(sum(points_a(i) for i in balanced(row)) for row in load()))
print("b:", st.median(b()))
