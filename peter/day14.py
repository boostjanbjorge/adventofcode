import collections


with open("inputs/day14.txt") as f:
    lines = f.read().strip().split("\n")

init = lines[0]
pair_counts = collections.Counter()
for c1, c2 in zip(init[:-1], init[1:]):
    pair_counts[c1 + c2] = pair_counts.get(c1 + c2, 0) + 1

maps = [l.split(" -> ") for l in lines[2:]]
maps = {
    m[0]: m[1] for m in maps
}

for _ in range(40):
    new_pairs = collections.Counter()
    char_count = collections.Counter()
    for pair, count in pair_counts.items():
        triplet = pair[0] + maps[pair] + pair[1]

        char_count[pair[0]] += count / 2
        char_count[triplet[1]] += count
        char_count[pair[1]] += count / 2

        new_pairs[triplet[:-1]] += count
        new_pairs[triplet[1:]] += count

    pair_counts = new_pairs

char_count[init[0]] += 0.5
char_count[init[-1]] += 0.5

print(int(char_count.most_common()[0][1] - char_count.most_common()[-1][1]))
