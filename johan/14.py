from collections import Counter, defaultdict
import get

problem_input = get.input(14)

initial = problem_input[0]
rule = dict([line.split(" -> ") for line in problem_input[2:]])

"""
def update_polymer(polymer):
    pairs = ["".join(pair) for pair in zip(polymer, polymer[1:])]
    out = [] 
    for i, c in enumerate(polymer):
        out.append(c)
        try:
            out.append(rule.get(pairs[i], ""))
        except IndexError:
            pass
    return "".join(out)


polymer = initial

for _ in range(10):
    polymer = update_polymer(polymer)

counter = Counter(polymer)
print(max(counter.values()) - min(counter.values()))
"""

polymer = initial
pair_counter = Counter("".join(pair) for pair in zip(polymer, polymer[1:]))


def update_pair_counter(pair_counter):
    for pair, count in list(pair_counter.items()):
        a, b = pair
        pair_counter[pair] -= count
        c = rule[pair]
        pair_counter[a + c] += count
        pair_counter[c + b] += count

    return pair_counter


def reconstruct_counts(pair_counter, first, last):
    counts = defaultdict(int)
    for pair, count in pair_counter.items():
        a, b = pair
        counts[a] += count
        counts[b] += count

    counts[first] += 1
    counts[last] += 1

    for c in counts:
        counts[c] = counts[c] // 2

    return counts


for n in (10, 30):
    for _ in range(n):
        pair_counter = update_pair_counter(pair_counter)

    counts = reconstruct_counts(pair_counter, initial[0], initial[-1])
    print(max(counts.values()) - min(counts.values()))
