def load():
    with open("inputs/17.txt") as f:
        xr, yr = f.read().split(", ")
    xl, xu = xr.split("=")[-1].split("..")
    yl, yu = yr.split("=")[-1].split("..")
    return (
        (int(xl), int(xu)),
        (int(yl), int(yu)),
    )


def inside(
    me: tuple[int, int],
    target: tuple[tuple[int, int], tuple[int, int]],
):
    mx, my = me
    (txl, txu), (tyl, tyu) = target
    return txl <= mx <= txu and tyl <= my <= tyu


def valid_velocity(
    velocity: tuple[int, int],
    start: tuple[int, int],
    target: tuple[tuple[int, int], tuple[int, int]],
):
    vx, vy = velocity
    sx, sy = start

    maxxt = target[0][1]
    minyt = target[1][0]

    peak = start

    while True:
        sx += vx
        sy += vy

        if sy > peak[1]:
            peak = (sx, sy)

        vx -= 1
        if vx < 0:
            vx = 0
        vy -= 1

        if inside((sx, sy), target):
            return ((vx, vy), peak)

        # Right of target, exit as we can
        # never reach its target.
        if sx > maxxt:
            return None

        # Below of target, exit as we can
        # never reach its target.
        if sy < minyt:
            return None


def trajectory_sweep(
    target: tuple[tuple[int, int], tuple[int, int]],
    xrange: tuple[int, int] = (0, 500),  # Yolo range, seem to work for my input
    yrange: tuple[int, int] = (-500, 500),  # Yolo range, seem to work for my input
):
    for x in range(*xrange):
        for y in range(*yrange):
            valid = valid_velocity((x, y), (0, 0), target)
            if valid is not None:
                yield (x, y), *valid


if __name__ == "__main__":
    print("a:", max(maxy for *_, (_, maxy) in trajectory_sweep(load())))
    print("b:", len(set(v for v, *_ in trajectory_sweep(load()))))
