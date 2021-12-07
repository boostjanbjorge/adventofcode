def load():
    with open("inputs/7.txt") as f:
        yield from map(int, f.readline().split(","))


def solve(cost):
    positions = tuple(load())
    min_position, max_position = min(positions), max(positions)
    return min(
        sum(cost(suggestion, crab) for crab in positions)
        for suggestion in range(min_position, max_position + 1)
    )


print("a:", solve(lambda a, b: abs(a - b)))
print("b:", solve(lambda a, b: (abs(a - b) + abs(a - b) ** 2) // 2))
