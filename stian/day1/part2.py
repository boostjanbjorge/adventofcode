import numpy as n
print(sum((n.diff(n.convolve(n.genfromtxt("day1.txt"), n.ones((3)))) > 0)))

