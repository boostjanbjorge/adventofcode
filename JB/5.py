import collections
import dataclasses
import itertools


@dataclasses.dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclasses.dataclass(frozen=True)
class Segment:
    start: Point
    stop: Point

    @property
    def slope(self):
        dy = self.stop.y - self.start.y
        dx = self.stop.x - self.start.x
        return dy / dx

    @property
    def y_intercept(self):
        # y = slope * x + b
        # b = y - slope * x, x->start.x
        return self.start.y - self.slope * self.start.x

    def points(self):

        min_y = min(self.start.y, self.stop.y)
        max_y = max(self.start.y, self.stop.y)

        min_x = min(self.start.x, self.stop.x)
        max_x = max(self.start.x, self.stop.x)

        if self.start.x == self.stop.x:
            for y in range(min_y, max_y + 1):
                yield Point(self.start.x, y)
        else:
            for x in range(min_x, max_x + 1):
                yield Point(x, round(self.slope * x + self.y_intercept))


def segments():
    with open("inputs/5.txt") as f:
        points = f.readlines()

    points = (p.strip() for p in points)
    points = (p.split("->") for p in points)
    points = ((p1.split(","), p2.split(",")) for p1, p2 in points)

    for (p1x, p1y), (p2x, p2y) in points:
        yield Segment(
            Point(int(p1x), int(p1y)),
            Point(int(p2x), int(p2y)),
        )


def count_interception(S: Segment):
    cnt = collections.Counter(itertools.chain.from_iterable(s.points() for s in S))
    return sum(1 for v in cnt.values() if v > 1)


# 13319, to high
print(
    count_interception(
        s for s in segments() if s.start.x == s.stop.x or s.start.y == s.stop.y
    )
)

# 19172
print(count_interception(segments()))
