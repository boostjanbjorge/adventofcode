import math
import get

problem_input = get.input(9)

matrix = [[int(x) for x in line] for line in problem_input]


def one_dim_low_points(matrix):
    low_points = []
    for x in range(len(matrix)):
        for y in range(n := len(matrix[x])):
            is_low = False
            try:
                is_low = matrix[x][y] < min(matrix[x][y - 1], matrix[x][y + 1])
            except IndexError:
                if y < n - 1:
                    is_low = matrix[x][y] < matrix[x][y + 1]
                if y > 0:
                    is_low = matrix[x][y] < matrix[x][y - 1]

            if is_low:
                low_points.append((x, y))
    return low_points


horizontal_low_points = one_dim_low_points(matrix)
vertical_low_points = one_dim_low_points(list(zip(*matrix)))
low_points = [(x, y) for x, y in horizontal_low_points if (y, x) in vertical_low_points]

print(sum(matrix[x][y] + 1 for x, y in low_points))

coordinates = {(x, y) for x, line in enumerate(matrix) for y in range(len(line))}
visited = {(x, y) for x, y in coordinates if matrix[x][y] == 9}
unvisited = coordinates.difference(visited)


def neighbors(current, unvisited):
    x, y = current
    for z in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if z in unvisited:
            yield z


basins = []

while unvisited:
    init_basin = next(iter(unvisited))
    queue = {init_basin}
    basin = set()

    while queue:
        current = queue.pop()
        basin.add(current)
        unvisited.remove(current)
        for z in neighbors(current, unvisited):
            queue.add(z)

    basins.append(basin)

print(math.prod(len(basin) for basin in sorted(basins, key=len)[-3:]))
