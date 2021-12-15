import numpy as np
from queue import PriorityQueue
with open("day15.txt") as f:
    caves = np.array([list(map(int, line.rstrip())) for line in f.readlines()])

bigger_caves = np.concatenate([caves + i for i in range(5)], axis=1)
biggest_caves = np.concatenate([bigger_caves + i for i in range(5)], axis=0)
biggest_caves[np.where(biggest_caves > 9)] -= 9

def traverse_caves(caves):
    xdim, ydim = caves.shape
    exit = (xdim-1, ydim-1)
    points = PriorityQueue()
    points.put(((0, 0), (0,0)))
    visited = {(0,0): 0}
    while not points.empty():
        (c, _), p = points.get()
        if p == exit: return c
        x, y = p
        neighs = [
            (max(0, x-1), y),
            (min(xdim-1, x+1), y),
            (x, max(0, y-1)),
            (x, min(ydim-1, y+1))]

        for n in neighs:
            n_cost = c+caves[n]
            if n in visited and n_cost >= visited[n]:
                continue
            visited[n] = n_cost
            dist = (exit[0]-n[0])**2+(exit[1]-n[1])**2
            points.put(((n_cost, dist), n))
print(traverse_caves(biggest_caves))  
