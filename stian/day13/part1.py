
import numpy as np

fname = "day13.txt"
tup = lambda a: tuple(map(int, a.split(",")))
def folding(a):
    axis, index = a[11:].split("=")
    return (axis, int(index))

with open(fname) as f:
    lines = f.readlines()
    points = set([tup(line.rstrip()) for line in lines if line[0].isdigit()])
    folds = [folding(line.rstrip()) for line in lines[len(points):] if line.startswith("f")]

def fold(points, axis, fold):
    new = set()
    old = set()

    for p in points:
        if axis == "y" and p[1] > fold:
            new.add((p[0], 2*fold-p[1]))
            old.add(p)
        elif axis == "x" and p[0] > fold:
            new.add((2*fold - p[0], p[1]))
            old.add(p)
    points.difference_update(old)
    points.update(new)
            

for axis, f in folds[0:1]:
    fold(points, axis, f)
print(len(points))
