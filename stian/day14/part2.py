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
    single = defaultdict(int)
    for s, e in pairs.keys():
        n = xform[s+e]
        v_old = pairs[(s,e)]
        new_pairs[(s,n)] += v_old
        new_pairs[(n,e)] += v_old
        single[s] += v_old
        single[n] += v_old
    single[template[-1]] += 1
    pairs = new_pairs

s = sorted(single.items(), key=lambda p: p[1])
print(s[-1][1] - s[0][1])
