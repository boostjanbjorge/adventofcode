import numpy as np

with open("day9.txt") as f:
    m = np.array([list(map(int, line.rstrip())) for line in f.readlines()])

f = np.pad(m, 1, constant_values=10)
a = (f[1:] < f[:-1])[:-1,1:-1]
b = (f[:-1] < f[1:])[1:,1:-1]
c = (f[:,1:] < f[:,:-1])[1:-1,:-1]
d = (f[:,:-1] < f[:,1:])[1:-1,1:]

hm = a & b & c & d

def count_neigh(p, mask):
    visited = set()
    stack = [p]
    xdim, ydim = mask.shape
    while len(stack) > 0:
        x, y = z = stack.pop()
        visited.add(z)
        neighs = [(max(0, x-1), y), (min(xdim-1, x+1), y), (x, max(0, y-1)), (x, min(ydim-1, y+1))]
        for n in neighs:
            if n not in visited and mask[n] < 9:
                stack.append(n)
    return len(visited)

basins = [count_neigh(p, m) for p in zip(*np.where(hm==True))]
import math
print(math.prod(sorted(basins)[-3:]))
