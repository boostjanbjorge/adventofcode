

up = {"{": "}", "(": ")", "[": "]", "<": ">"}
down = {"}": "{", ")": "(", "]": "[", ">": "<"}
value = {"(": 1, "[": 2, "{": 3, "<": 4}

def calc_score(line):
    stack = []
    for c in line.rstrip():
        if c in up:
            stack.append(c)
        else:
            if stack.pop() != down[c]:
                return None
    score = 0
    while len(stack) > 0:
        score = score*5 + value[stack.pop()]
    return score

with open("day10.txt") as f:
    lines_scores = []
    for line in f.readlines():
        score = calc_score(line)
        if score is not None:
            lines_scores.append(score)

    print(sorted(lines_scores)[len(lines_scores)//2])


            
            
