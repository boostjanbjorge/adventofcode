#!/usr/bin/env python3
def precompute(num):
    age = [num]
    for count in range(0, 128):
        new_age = []
        for elem in age:
            if elem == 0:
                new_age.append(8)
                new_age.append(6)
            else:
                new_age.append(elem - 1)
        age = new_age
    return len(age)

with open("input.txt", "r") as f:
    age = []
    multiplier = []
    for elem in range(0, 9):
        multiplier.append(precompute(elem))
    for elem in f.read().split(","):
        age.append(int(elem))
    for _ in range(0, 128):
        new_age = []
        for elem in age:
            if elem == 0:
                new_age.append(8)
                new_age.append(6)
            else:
                new_age.append(elem - 1)
        age = new_age
    count = 0
    for elem in age:
        count += multiplier[elem]
    print(count)
    


    
