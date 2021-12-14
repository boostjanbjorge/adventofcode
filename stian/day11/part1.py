import numpy as np
with open("day11.txt") as f:
    c = np.array([list(map(int, line.rstrip())) for line in f.readlines()])


x,y = c.shape
total_number_of_flashing_octopuses = 0

for step in range(1000):
    c += 1
    while True:
        excited_octopodes = np.where(c>9)
        if len(excited_octopodes[0]) == 0:
            break
        for i, j in zip(*excited_octopodes):
            c[max(0, i-1):min(x, i+2), max(0, j-1):min(y, j+2)] += 1
        c[excited_octopodes] = -99
    flashing_octopi = np.where(c<0)
    c[flashing_octopi] = 0
    total_number_of_flashing_octopuses += len(flashing_octopi[0])
    if np.all(c == 0):
        print("First flash dance at step", step+1)
        break

print(c)
print(total_number_of_flashing_octopuses)
