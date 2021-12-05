

# part 1

with open("inputs/day1.txt", "r") as f:
    lines = f.read().strip().split("\n")

n_increases = 0
for left, right in zip(lines[:-1], lines[1:]):
    if int(right) > int(left):
        n_increases += 1

print("Part 1:", n_increases)


# part 2
n_increases = 0
prevval = None
for left, middle, right in zip(lines[:-2], lines[1:-1], lines[2:]):
    curval = int(left) + int(middle) + int(right)
    if prevval is not None and curval > prevval:
        n_increases += 1
    prevval = curval
print("Part 2:", n_increases)
