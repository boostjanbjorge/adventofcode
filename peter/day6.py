import collections
import tqdm

fish = open("inputs/day6.txt").read().strip().split(",")
fish = [int(f) for f in fish]

fish = collections.Counter(fish)

for day in tqdm.tqdm(range(256)):
    next_fish = collections.Counter()
    for days, count in fish.items():
        if days == 0:
            next_fish[6] += count
            next_fish[8] += count
        else:
            next_fish[days - 1] += count
    fish = next_fish

print(sum(fish.values()))
