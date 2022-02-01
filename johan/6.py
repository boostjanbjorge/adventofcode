from collections import defaultdict
import get

problem_input = get.input(6)
initial_state = list(map(int, problem_input[0].split(",")))

fish = defaultdict(int)
for x in initial_state:
    fish[x] += 1


def dictsim(d):
    out = defaultdict(int)
    out[8] = d[0]
    for k in d:
        out[k - 1 if k else 6] += d[k]
    return out


for _ in range(80):
    fish = dictsim(fish)

print(sum(fish[k] for k in fish))

for _ in range(256 - 80):
    fish = dictsim(fish)

print(sum(fish[k] for k in fish))
