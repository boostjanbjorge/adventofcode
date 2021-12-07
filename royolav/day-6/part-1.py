#!/usr/bin/env python3
with open("input.txt", "r") as f:
    num = []
    for elem in f.read().split(","):
        num.append(int(elem))
    for _ in range(0, 80):
        new_num = []
        for elem in num:
            if elem == 0:
                new_num.append(8)
                new_num.append(6)
            else:
                new_num.append(elem - 1)
        num = new_num
    print(len(num))
        
