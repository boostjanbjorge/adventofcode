import numpy as np

fname = "day4.txt"
numbers = np.loadtxt(fname, dtype=int, max_rows=1, delimiter=",")
n = np.loadtxt(fname, dtype=int, skiprows=1)
n = n.reshape(-1, n.shape[1], n.shape[1])

def update_board(number, boards):
    matches = np.where(boards==number)
    boards[matches] *= -1
    for b,r,c in zip(*matches):
        board = boards[b,:,:]
        if all(board[r,:] < 0) or all(board[:,c] < 0):
            return np.where(board > 0, board, 0).sum() * number
    return None

for b in numbers:
    res = update_board(b, n)
    if res is not None:
        print(res)
        exit(0)

        
