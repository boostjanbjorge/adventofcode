import functools


@functools.cache
def grid() -> tuple[tuple[int, ...], ...]:
    with open("inputs/9.txt") as f:
        rows = f.readlines()
    return tuple(tuple(int(n) for n in row.strip()) for row in rows)


def adjacents(x: int, y: int):
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(grid()[0]) and 0 <= new_y < len(grid()):
            yield grid()[new_y][new_x]


def lows():
    for y in range(len(grid())):
        for x in range(len(grid()[0])):
            if all(adj > grid()[y][x] for adj in adjacents(x, y)):
                yield x, y


def explore_basin(
    x: int, y: int, explored: set[tuple[int, int]]
) -> set[tuple[int, int]]:

    if (x, y) in explored:
        return explored

    len_y = len(grid())  # 5 / 100
    len_x = len(grid()[0])  # 10 / 100

    # Given by the problem description.
    if grid()[y][x] == 9:
        return explored

    explored.add((x, y))
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len_x and 0 <= new_y < len_y:
            explore_basin(new_x, new_y, explored=explored)

    return explored


def basins():
    for low in lows():
        yield explore_basin(*low, set())


def a():
    return sum(grid()[y][x] + 1 for x, y in lows())


def b():
    three_biggest = sorted(tuple(basins()), key=len)[-3:]
    # multiply together the sizes of the three largest basins
    return functools.reduce(lambda a, b: a * b, map(len, three_biggest))


print("a:", a())
print("b:", b())
