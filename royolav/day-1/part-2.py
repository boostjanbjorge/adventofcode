#!/usr/bin/env python3
with open("input.txt", "r") as f:
    count = 0
    lines = f.readlines()
    num = int(lines[0]) + int(lines[1]) + int(lines[2])
    endpos = len(lines) - 3
    for i, line in enumerate(lines):
        if i == endpos:
            break
        old = num
        num = int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])
        if num > old:
            count += 1
    print(count)
