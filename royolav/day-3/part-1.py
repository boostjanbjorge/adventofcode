#!/usr/bin/env python3
with open("input-3.txt", "r") as f:
    lines = f.readlines()
    gamma = ""
    epsilon = ""
    for i in range(0,12):
        zeros = 0
        ones = 0
        for line in lines:
            if int(line[i]) == 0:
                zeros += 1
            else:
                ones += 1

        if ones > zeros:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print(int(gamma, 2) * int(epsilon, 2))



