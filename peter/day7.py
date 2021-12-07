import numpy as np
import math
import functools


positions = open("inputs/day7.txt").read().strip().split(",")
# positions = [16,1,2,0,4,2,7,1,2,14]
positions = [int(p) for p in positions]
median = np.median(positions)

moves = []
new_positions = []

for pos in positions:
    moves.append(median - pos)
    new_positions.append(pos + moves[-1])


print(sum([abs(m) for m in moves]))


@functools.lru_cache(maxsize=100000)
def calculate_fuel(position, target):
    return abs(target - position) * (abs(target - position) + 1) / 2


def find_least_fuel(positions):
    best_target = 0
    best_fuel = math.inf
    for target in range(min(positions), max(positions) + 1):
        total_fuel = sum(calculate_fuel(pos, target) for pos in positions)
        if total_fuel < best_fuel:
            best_target = target
            best_fuel = total_fuel
    return best_target, best_fuel

print(find_least_fuel(positions))
