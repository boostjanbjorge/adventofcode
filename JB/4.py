
import dataclasses
import uuid


def draw():
    with open("inputs/4.txt") as f:
        d = f.readline().strip()
    yield from map(int, d.split(","))


@dataclasses.dataclass
class Number:
    N: int
    marked: bool = dataclasses.field(default_factory=lambda: False)


@dataclasses.dataclass(frozen=True)
class Board:
    board: tuple[tuple[Number]]
    id: uuid.uuid4 = dataclasses.field(default_factory=uuid.uuid4)

    @property
    def rows(self):
        yield from self.board

    @property
    def columns(self):
        yield from zip(*self.board)

    def mark(self, N):
        for row in self.board:
            for number in row:
                if number.N == N:
                    number.marked = True

    def _row_won(self):
        for row in self.rows:
            if all(n.marked for n in row):
                return True
        return False

    def _column_won(self):
        for column in self.columns:
            if all(n.marked for n in column):
                return True
        return False

    def won(self):
        return self._column_won() or self._row_won()

    def sum(self, draw: int):
        return sum(sum(n.N for n in row if not n.marked) for row in self.rows) * draw



def chunk(arr, size):
    for i in range(0, len(arr), size):
        yield arr[i:i+size]


def borads():

    with open("inputs/4.txt") as f:
        # Skip draws
        f.readline()
        lines = tuple(line.strip() for line in f.readlines() if line)

    lines = tuple(line.split() for line in lines if len(line) > 0)
    lines = tuple(tuple(map(lambda n: Number(int(n)), line)) for line in lines)

    return tuple(Board(board) for board in chunk(lines, 5))


def first_win():
    candidates = borads()
    for d in draw():
        for borad in candidates:
            borad.mark(d)
            if borad.won():
                return borad.sum(d)


def last_win():
    candidates = borads()
    remove = set()

    for d in draw():
        for borad in candidates:
            borad.mark(d)
            if borad.won():
                remove.add(borad.id)

        if len(candidates) == 1 and candidates[0].won():
            assert candidates[0].won()
            return candidates[0].sum(d)

        candidates = tuple(b for b in candidates if b.id not in remove)
        remove.clear()

# 18990, 82440
print("a:", first_win())

# 19845(to low)
print("b:", last_win())
