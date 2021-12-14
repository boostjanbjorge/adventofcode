import collections
import tqdm

with open("inputs/day14.txt") as f:
    lines = f.read().strip().split("\n")

init = list(lines[0])
maps = [l.split(" -> ") for l in lines[2:]]
maps = {
    m[0]: m[1] for m in maps
}

# part 1
for _ in tqdm.tqdm(range(10)):
    seq = []
    for i, (c1, c2) in enumerate(zip(init[:-1], init[1:])):
        seq.append(c1)
        seq.append(maps[c1 + c2])
        if i == len(init) - 2:
            seq.append(c2)
    init = seq

counts = collections.Counter(seq)
print(counts.most_common()[0][1] - counts.most_common()[-1][1])
