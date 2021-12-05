import sys

import collections


text = open("inputs/day4.txt").read().strip()

draw_numbers = text.split("\n")[0].strip().split(",")
draw_numbers = [int(draw) for draw in draw_numbers]

boards = text.split("\n\n")
boards = boards[1:]  # skip draw line


class Board:
    def __init__(self, matrix_text):
        lines = matrix_text.split("\n")
        self.numbers = []
        self.bingo_markers = []
        for line in lines:
            self.numbers.append([int(n) for n in line.split()])
            self.bingo_markers.append([False for _ in line.split()])

    def add_number(self, new_number):
        for row, bingo_row in zip(self.numbers, self.bingo_markers):
            for i, number in enumerate(row):
                if new_number == number:
                    bingo_row[i] = True

    def is_bingo(self):
        for row in self.bingo_markers:
            if all(row):
                return True
        for column in zip(*self.bingo_markers):
            if all(column):
                return True
        return False

    def unmarked_numbers(self):
        for i, row in enumerate(self.bingo_markers):
            for j, is_matched in enumerate(row):
                if not is_matched:
                    yield self.numbers[i][j]

    def __str__(self):
        board_strings = []
        for bingo_row, number_row in zip(self.bingo_markers, self.numbers):
            row_string = ""
            for is_matched, number in zip(bingo_row, number_row):
                if is_matched:
                    row_string += f"*{number}*"
                else:
                    row_string += f" {number} "
            board_strings.append(row_string)
        return "\n".join(board_strings)

    def __hash__(self):
        s = "\n".join(" ".join([str(n) for n in self.numbers]))
        return hash(s)


boards = [Board(board) for board in boards]

winner_sequence = []

for draw in draw_numbers:
    for board in boards:
        board.add_number(draw)
        if board.is_bingo():
            score = sum(board.unmarked_numbers()) * draw
            winner_sequence.append(board)
            if set(winner_sequence) == set(boards):
                print("Last winner: {}".format(str(board)))
                print("score", score)
                sys.exit(0)
