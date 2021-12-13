

up = {"{": "}", "(": ")", "[": "]", "<": ">"}
down = {"}": "{", ")": "(", "]": "[", ">": "<"}
value = {")": 3, "]": 57, "}": 1197, ">": 25137}

with open("day10.txt") as f:
    error_codes = 0
    for line in f.readlines():
        stack = []
        for c in line.rstrip():
            if c in up:
                stack.append(c)
            else:
                if stack.pop() != down[c]: 
                    error_codes += value[c]
                    break
    print(error_codes)


            
            
