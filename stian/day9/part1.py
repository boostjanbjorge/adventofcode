import numpy as np

with open("day9.txt") as f:
    m = np.array([list(map(int, line.rstrip())) for line in f.readlines()])

f = np.pad(m, 1, constant_values=10)
a = (f[1:] < f[:-1])[:-1,1:-1]
b = (f[:-1] < f[1:])[1:,1:-1]
c = (f[:,1:] < f[:,:-1])[1:-1,:-1]
d = (f[:,:-1] < f[:,1:])[1:-1,1:]
hm = a & b & c & d
print(np.sum(m[np.where(hm == True)] + 1))
