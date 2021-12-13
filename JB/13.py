import dataclasses


@dataclasses.dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclasses.dataclass(frozen=True)
class Instruction:
    axis: str
    line: int


def load():
    with open("inputs/13.txt") as f:
        return f.readlines()


def points():
    return set(
        Point(int(x), int(y))
        for x, y in (line.strip().split(",") for line in load() if "," in line)
    )


def instructions():
    return tuple(
        Instruction(i[-1], int(l))
        for i, l in (line.strip().split("=") for line in load() if "=" in line)
    )


def yfold(_points: set[Point], line: int):
    return set(p if p.y < line else Point(p.x, 2 * line - p.y) for p in _points)


def xfold(_points: set[Point], line: int):
    return set(p if p.x < line else Point(2 * line - p.x, p.y) for p in _points)


def pprint(_points: set[Point]):
    minx, maxx, miny, maxy = (
        min(p.x for p in _points),
        max(p.x for p in _points),
        min(p.y for p in _points),
        max(p.y for p in _points),
    )

    for y in range(miny, maxy + 1):
        print(
            "".join(
                "#" if Point(x, y) in _points else " " for x in range(minx, maxx + 1)
            )
        )


def fold(_points: set[Point], _instructions: list[Instruction]):
    for i in _instructions:
        if i.axis == "y":
            _points = yfold(_points, i.line)
        else:
            _points = xfold(_points, i.line)
    return _points


if __name__ == "__main__":
    print("a:", len(fold(points(), instructions()[:1])))
    print("b:")
    pprint(fold(points(), instructions()))
