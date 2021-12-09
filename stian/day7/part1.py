import numpy as np; from collections import Counter
crab_dist = Counter(np.fromfile("day7.txt", dtype=int, sep=","))
upper = max(crab_dist.keys())
base = np.zeros((upper+1,), dtype=int)
for k, v in crab_dist.items(): base[k] = v
fw = np.cumsum(np.cumsum(np.roll(base, 1)))
bw = np.cumsum(np.cumsum(np.roll(base[::-1], -1)))
cost = fw+bw[::-1]
print(np.argmin(cost), np.min(cost))


