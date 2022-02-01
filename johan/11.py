from collections import deque
from itertools import product
import get

problem_input = get.input(11)

matrix = [[int(x) for x in line] for line in problem_input]
coordinates = {(x, y) for x, line in enumerate(matrix) for y in range(len(line))}


def neighbors(current):
    x, y = current
    for z in product((x - 1, x, x + 1), (y - 1, y, y + 1)):
        if z != current and z in coordinates:
            yield z


def step():
    flashes = 0
    queue = deque(coordinates)

    while queue:
        x, y = queue.popleft()
        matrix[x][y] += 1
        if matrix[x][y] == 10:
            flashes += 1
            for adjacent in neighbors((x, y)):
                queue.append(adjacent)

    for x, y in coordinates:
        if matrix[x][y] > 9:
            matrix[x][y] = 0

    return flashes


print(sum(step() for _ in range(100)))

matrix = [[int(x) for x in line] for line in problem_input]


def distinct_entries(matrix):
    return set.union(*(set(line) for line in matrix))


i = 0
while distinct_entries(matrix) != {0}:
    step()
    i += 1
print(i)
