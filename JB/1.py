
with open("inputs/1.txt") as f:
    _input = [int(i) for i in f.readlines() if i]


# 1a
print("1a:", sum(1 for a, b in zip(_input[1:], _input) if a > b))

# 1b
def combo_sum(_input):
    def _inner():
        for combo in zip(_input[2:], _input[1:], _input):
            yield sum(combo)
    return tuple(_inner())

print("1b:", sum(1 for a, b in zip(combo_sum(_input)[1:], combo_sum(_input)) if a > b))