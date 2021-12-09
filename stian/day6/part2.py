import numpy as np; from collections import Counter

f = Counter(np.fromfile("day6.txt", sep=","))
fish = [f.get(i, 0) for i in range(9)]
for i in range(256):
    m = fish.pop(0)
    fish[6] += m
    fish.append(m)
print(sum(fish))
