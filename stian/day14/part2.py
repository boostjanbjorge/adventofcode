from collections import defaultdict

with open("day14.txt") as f:
    lines = f.readlines()
    template = lines[0].rstrip()
    xform = dict(tuple(line.rstrip().split(" -> ")) for line in lines[2:])

pairs = defaultdict(int)
for s,e in zip(template, template[1:]):
    pairs[(s,e)] += 1

for i in range(40):
    new_pairs = defaultdict(int)
    for p, v in pairs.items():
        n = xform["".join(p)]
        new_pairs[(p[0],n)] += v
        new_pairs[(n,p[1])] += v
    pairs = new_pairs

single = defaultdict(int)
for p, v in pairs.items():
    single[p[0]] += v
single[template[-1]] += 1

s = sorted(single.items(), key=lambda p: p[1])
print(s[-1][1] - s[0][1])
