import collections




class Vector2:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return self.__class__.__name__ + f"({self.x}, {self.y})"


class Line:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def get_points(self, skip_diagonal=False):
        if self.v1.x < self.v2.x:
            x_coords = list(range(self.v1.x, self.v2.x + 1))
        else:
            x_coords = list(reversed(range(self.v2.x, self.v1.x + 1)))

        if self.v1.y < self.v2.y:
            y_coords = list(range(self.v1.y, self.v2.y + 1))
        else:
            y_coords = list(reversed(range(self.v2.y, self.v1.y + 1)))

        if len(x_coords) == 1:
            x_coords *= len(y_coords)
        elif len(y_coords) == 1:
            y_coords *= len(x_coords)
        elif skip_diagonal:
            return

        yield from zip(x_coords, y_coords)

    def __repr__(self):
        return self.__class__.__name__ + f"({self.v1}, {self.v2})"


file_lines = open("inputs/day5.txt").read().strip().split("\n")

lines = []
for line in file_lines:
    v1, v2 = line.split(" -> ")
    lines.append(
        Line(
            Vector2(*v1.split(",")),
            Vector2(*v2.split(","))
        )
    )


position_counts = collections.Counter()
for line in lines:
    for point in line.get_points(skip_diagonal=True):
        position_counts[point] += 1


n = 0
for point, count in position_counts.most_common():
    if count < 2:
        break
    n += 1

print("Part 1:", n)


position_counts = collections.Counter()
for line in lines:
    for point in line.get_points(skip_diagonal=False):
        position_counts[point] += 1

n = 0

for point, count in position_counts.most_common():
    if count < 2:
        break
    n += 1

print("Part 2:", n)
