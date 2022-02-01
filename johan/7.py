import get

problem_input = get.input(7)

positions = list(map(int, problem_input[0].split(",")))
min_pos = sorted(positions)[len(positions) // 2]


def fuel(array, pos):
    return sum(abs(x - pos) for x in array)


print(fuel(positions, min_pos))


def triangular_fuel(array, pos):
    def abs_triang(k):
        return abs(k) * (abs(k) + 1) // 2

    return sum(abs_triang(x - pos) for x in array)


min_cost = float("inf")
for pos in range(min(positions), max(positions) + 1):
    cost = triangular_fuel(positions, pos)
    if cost < min_cost:
        min_cost = cost

print(min_cost)
