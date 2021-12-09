import numpy as np

f = np.fromfile("day6.txt", dtype=int, sep=",")
for i in range(80):
    f -= 1
    z = np.where(f < 0)[0]
    f[z] = 6
    f = np.append(f, [8]*len(z))
print(len(f))
