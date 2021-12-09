import numpy as np; from collections import Counter
crab_dist = Counter(np.fromfile("day7.txt", dtype=int, sep=","))
upper = max(crab_dist.keys())
cost = np.zeros((upper,), dtype=int)
for k,n in crab_dist.items():
    for o, i in enumerate(range(k-1, upper)):
        cost[i] += n*(o*(o+1)/2)
    for o, i in enumerate(range(k-1, -1, -1)):
        cost[i] += n*(o*(o+1)/2)
print(np.argmin(cost)+1, np.min(cost))


