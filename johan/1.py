with open("input.1") as f:
    depths = f.readlines()
    depths = [int(depth.strip()) for depth in depths]


def number_of_increases(depths):
    prev = None
    increases = 0

    for depth in depths:
        if prev is not None and depth > prev:
            increases += 1
        prev = depth
    
    return increases


window_sum = []
for i in range(len(depths)):
    window = depths[i:i + 3]
    if len(window) == 3:
        window_sum.append(sum(window))


print(number_of_increases(depths))
print(number_of_increases(window_sum))
