with open("day14_test.txt") as f:
    lines = f.readlines()
    template = lines[0].rstrip()
    xform = dict(tuple(line.rstrip().split(" -> ")) for line in lines[2:])

for i in range(10):
    new = []
    for s, e in zip(template, template[1:]):
        new.extend([s, xform[s+e]])
    new.append(e)
    template = new

from collections import Counter
counts = sorted(Counter(template).items(), key=lambda p: p[1])
print(counts[-1][1] - counts[0][1])
