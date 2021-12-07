#!/usr/bin/env python3
def compute_cost(distance):
    count = 0
    for elem in range(0, distance + 1):
        count += elem
    return count

with open("input.txt", "r") as f:
    num = []
    for elem in f.read().split(","):
        num.append(int(elem))
    positions = set(num)
    cost = []
    for distance in range(0, (max(positions) - min(positions)) + 1):
        cost.append(compute_cost(distance))
    steps = -1
    for position in positions:
        current = 0
        for elem in num:
            current += cost[abs(elem - position)]
        if steps < 0 or current < steps:
            steps = current
    print(steps)

