import numpy as np

fname = "day4.txt"
numbers = np.loadtxt(fname, dtype=int, max_rows=1, delimiter=",")
n = np.loadtxt(fname, dtype=int, skiprows=1)
n = n.reshape(-1, n.shape[1], n.shape[1])
board_ids = set(range(n.shape[0]))

def update_board(number, boards, board_ids):
    matches = np.where(boards==number)
    boards[matches] *= -1
    for b,r,c in zip(*matches):
        if b not in board_ids:
            continue
        board = boards[b,:,:]
        if all(board[r,:] <= 0) or all(board[:,c] <= 0):
            board_ids.discard(b)
            if len(board_ids) == 0:
                return np.where(board > 0, board, 0).sum() * number
    return None

for b in numbers:
    res = update_board(b, n, board_ids)
    if res is not None:
        print(b, res)

        
