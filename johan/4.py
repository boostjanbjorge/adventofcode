import get
import lib

problem_input = get.input(4)


def map_list_deep(func, it):
    out = []
    for x in it:
        if isinstance(x, list):
            out.append(map_list_deep(func, x))
        else:
            out.append(func(x))
    return out


gen = lib.partition_at_value(problem_input, "")
draws = map_list_deep(int, next(gen)[0].split(","))
boards = map_list_deep(int, [[line.split() for line in board] for board in gen])

board_lines = []
for board in boards:
    lines = [set(line) for line in board]
    for line in zip(*board):
        lines.append(set(line))
    board_lines.append(lines)


def is_bingo(lines, draws):
    return any(line <= set(draws) for line in lines)


bingos = {}  # board_index: (draw_index, sum)

for draw_idx in range(len(draws)):
    current_draws = draws[: draw_idx + 1]
    for i, lines in enumerate(board_lines):
        if i not in bingos and is_bingo(lines, current_draws):
            board = boards[i]
            new_board = [
                [0 if x in current_draws else x for x in line] for line in board
            ]
            board_sum = sum(sum(line) for line in new_board)
            bingos[i] = (draw_idx, board_sum)

# use insertion order
bingo_order = list(bingos.keys())
first = bingo_order[0]
last = bingo_order[-1]

for i in (first, last):
    draw_idx, board_sum = bingos[i]
    print(board_sum * draws[draw_idx])
