import queue


def load():
    gph = {}
    with open("inputs/15.txt") as f:
        for y, row in enumerate(f.readlines()):
            for x, risk in enumerate(row):
                if r := risk.strip():
                    gph[(x, y)] = int(r)
    return gph


def walk(
    start: tuple[int, int],
    stop: tuple[int, int],
    gph: dict[tuple[int, int], int],
):
    minx, maxx = min(x for x, _ in gph), max(x for x, _ in gph)
    miny, maxy = min(y for _, y in gph), max(y for _, y in gph)

    pq: queue.PriorityQueue[tuple[int, tuple[int, int]]] = queue.PriorityQueue()
    pq.put((0, start))
    visited = set((start,))

    while not pq.empty():
        acc_risk, (x, y) = pq.get()

        if (x, y) == stop:
            return acc_risk

        # Neighbors
        for x, y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            p = (x, y)
            if minx <= x <= maxx and miny <= y <= maxy and p not in visited:
                pq.put((acc_risk + gph[p], p))
                visited.add(p)

    raise ValueError("No path")


print(walk((0, 0), (99, 99), load()))
