import numpy as n
print(sum((n.diff(n.genfromtxt("day1.txt")) > 0).astype(n.int64)))

