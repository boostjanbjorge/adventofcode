lines = open("inputs/day2.txt").read().strip().split("\n")

position = {"depth": 0, "horizontal": 0}

for line in lines:
    command, value = line.split()
    value = int(value)

    if command == "forward":
        position["horizontal"] += value
    if command == "up":
        position["depth"] -= value
    if command == "down":
        position["depth"] += value

print(position, position["depth"] * position["horizontal"])


"part 2"
position = {"depth": 0, "horizontal": 0, "aim": 0}

for line in lines:
    command, value = line.split()
    value = int(value)

    if command == "forward":
        position["horizontal"] += value
        position["depth"] += value * position["aim"]
    if command == "up":
        position["aim"] -= value
    if command == "down":
        position["aim"] += value

print(position, position["depth"] * position["horizontal"])