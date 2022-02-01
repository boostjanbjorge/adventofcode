from collections import defaultdict

import get

problem_input = get.input(5)
string_coords = [x.split(" -> ") for x in problem_input]
start, stop = zip(*string_coords)


def convert_coord(string):
    # "x,y" --> (int(x), int(y))
    return tuple(map(int, string.split(",")))


start = list(map(convert_coord, start))
stop = list(map(convert_coord, stop))


def param_line(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    steps = max(abs(x1 - x2), abs(y1 - y2))

    def line(t):
        return (
            round(x1 * (1 - t / steps) + x2 * t / steps),
            round(y1 * (1 - t / steps) + y2 * t / steps),
        )

    for step in range(steps + 1):
        yield line(step)


count = defaultdict(int)
count_diagonal = defaultdict(int)

for source, sink in zip(start, stop):
    diagonal = source[0] != sink[0] and source[1] != sink[1]
    for i, j in param_line(source, sink):
        if diagonal:
            count_diagonal[(i, j)] += 1
        else:
            count[(i, j)] += 1

print(sum(count[x] > 1 for x in count.keys()))

count_combined = count.copy()
for x in count_diagonal:
    count_combined[x] += count_diagonal[x]

print(sum(count_combined[x] > 1 for x in count_combined.keys()))
