import collections
import dataclasses
import itertools
import typing


@dataclasses.dataclass
class Octopus:
    level: int
    flashes: int = 0
    flashed: bool = False


def load():
    with open("inputs/11.txt") as f:
        return tuple(tuple(Octopus(int(n)) for n in c.strip()) for c in f.readlines())


def adjacents(x: int, y: int, grid: tuple[tuple[Octopus, ...], ...]):
    leny = len(grid)
    lenx = len(grid[0])
    for dx, dy in itertools.product((1, 0, -1), repeat=2):
        if (dx, dy) == (0, 0):
            continue
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < lenx and 0 <= new_y < leny:
            yield (
                new_x,
                new_y,
                grid[new_y][new_x],
            )


def flash(x: int, y: int, grid: tuple[tuple[Octopus, ...], ...]):

    me = grid[y][x]

    if me.flashed:
        return

    if me.level >= 10:
        me.flashed = True
        for nx, ny, neighbor in adjacents(x, y, grid):
            neighbor.level += 1
            flash(nx, ny, grid)


def step(grid: tuple[tuple[Octopus, ...], ...]):

    # Everyone gains energy
    for y, row in enumerate(grid):
        for x, octopus in enumerate(row):
            octopus.level += 1

    # Flash to neighbours
    for y, row in enumerate(grid):
        for x, octopus in enumerate(row):
            flash(x, y, grid)

    # # Reset
    for row in grid:
        for octopus in row:
            if octopus.flashed:
                octopus.flashes += 1
            octopus.flashed = False
            if octopus.level >= 10:
                octopus.level = 0


def simulate(N=100):
    grid = load()

    for _ in range(N):
        step(grid)

    return sum(sum(oct.flashes for oct in row) for row in grid)


def cnt(grid: tuple[tuple[Octopus, ...], ...]):
    return collections.Counter(octopus.level for row in grid for octopus in row)


def synchronized():

    grid = load()
    len_y = len(grid)
    len_x = len(grid[0])

    t = 0
    while cnt(grid)[0] != len_y * len_x:
        t += 1
        step(grid)
    return t


if __name__ == "__main__":
    print("a:", simulate())
    print("b:", synchronized())
