
import collections

with open("inputs/2.txt") as f:
    instructions = [instruction.split() for instruction in f.readlines()]
    instructions = [(cmd, int(step)) for cmd, step in instructions]


cnt = collections.defaultdict(int)


for cmd, step in instructions:
    cnt[cmd] += step

    if cmd == "down":
        cnt["aim"] += step
    elif cmd == "up":
        cnt["aim"] -= step
    elif cmd == "forward":
        cnt["depth"] += cnt["aim"] * step

print(cnt)

print("a: ", cnt["forward"] * (cnt["down"]-cnt["up"]))
print("b: ", cnt["forward"] * cnt["depth"])
