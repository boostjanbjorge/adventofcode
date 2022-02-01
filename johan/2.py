import get

instructions = get.input(2)
instructions = [instruction.split() for instruction in instructions]
instructions = [(d, int(v)) for d, v in instructions]

depth = 0
horizontal = 0

for d, v in instructions:
    if d == "down":
        depth += v
    if d == "up":
        depth -= v
    if d == "forward":
        horizontal += v

print(depth * horizontal)


depth = 0
horizontal = 0
aim = 0

for d, v in instructions:
    if d == "down":
        aim += v
    if d == "up":
        aim -= v
    if d == "forward":
        horizontal += v
        depth += aim * v

print(horizontal * depth)
