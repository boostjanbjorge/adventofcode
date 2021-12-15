import queue


def load():
    gph: dict[tuple[int, int], int] = {}
    with open("inputs/15.txt") as f:
        for y, row in enumerate(f.readlines()):
            for x, risk in enumerate(row):
                if r := risk.strip():
                    gph[(x, y)] = int(r)
    return gph


def top_left_to_bottom_left(gph: dict[tuple[int, int], int]):
    minx, maxx = min(x for x, _ in gph), max(x for x, _ in gph)
    miny, maxy = min(y for _, y in gph), max(y for _, y in gph)

    start = (minx, miny)
    stop = (maxx, maxy)

    pq: queue.PriorityQueue[tuple[int, tuple[int, int]]] = queue.PriorityQueue()
    pq.put((0, start))
    visited = set((start,))

    while not pq.empty():
        acc_risk, (x, y) = pq.get()

        if (x, y) == stop:
            return acc_risk

        # Neighbors
        for x, y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if minx <= x <= maxx and miny <= y <= maxy and (x, y) not in visited:
                pq.put((acc_risk + gph[(x, y)], (x, y)))
                visited.add((x, y))

    raise ValueError("No path")


def extended(rx=5, ry=5):
    gph = load()
    maxx = max(x for x, _ in gph) + 1
    maxy = max(y for _, y in gph) + 1

    for x, y in tuple(gph.keys()):
        for sx in range(rx):
            for sy in range(ry):
                gph[(x + sx * maxx, y + sy * maxy)] = gph[(x, y)] + sx + sy

    for key, risk in tuple(gph.items()):
        while risk > 9:
            risk -= 9
        gph[key] = risk

    return gph


if __name__ == "__main__":
    print("a:", top_left_to_bottom_left(load()))
    print("b:", top_left_to_bottom_left(extended()))
