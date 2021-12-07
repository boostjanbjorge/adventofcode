#!/usr/bin/env python3
with open("input.txt", "r") as f:
    num = []
    for elem in f.read().split(","):
        num.append(int(elem))
    positions = set(num)
    steps = -1
    for position in positions:
        current = 0
        for elem in num:
            current += abs(elem - position)
        if steps < 0 or current < steps:
            steps = current
    print(steps)

