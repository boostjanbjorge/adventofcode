from collections import Counter
from itertools import repeat

tup = lambda a: tuple(map(int, a.split(",")))
is_diag = lambda a, b: a[0] != b[0] and a[1] != b[1]

def auto_range(x0, x1):
    if x0 < x1:
        return range(x0, x1+1)
    elif x0 > x1:
        return range(x0, x1-1, -1)
    return repeat(x0)

fname="day5.txt"
coords= []
with open(fname) as f:
    for line in f.readlines():
        s, e = [tup(i) for i in line.split("->")]
        if not is_diag(s, e): #Remove for part 2
            coords.extend([c for c in zip(
                auto_range(s[0], e[0]),
                auto_range(s[1], e[1]))])
print(len([v for v in Counter(coords).values() if v > 1]))

