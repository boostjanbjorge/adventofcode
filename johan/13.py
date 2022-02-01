import get
import lib

problem_input = get.input(13)
coords, folds = lib.partition_at_value(problem_input, "")

coords = {(int(x), int(y)) for x, y in (line.split(",") for line in coords)}
folds = [(axis, int(line)) for axis, line in (f.split()[-1].split("=") for f in folds)]


def perform_fold(coords, fold, xmax=None, ymax=None):
    if xmax is None:
        xmax = max(c[0] for c in coords)
    if ymax is None:
        ymax = max(c[1] for c in coords)

    folded_coords = set()
    axis, line = fold

    if axis == "x":
        for c in coords:
            if c[0] < line:
                folded_coords.add(c)
            elif c[0] > line:
                folded_coords.add((2 * line - c[0], c[1]))
            else:
                print("Xikes")
    else:
        for c in coords:
            if c[1] < ymax // 2:
                folded_coords.add(c)
            elif c[1] > ymax // 2:
                folded_coords.add((c[0], 2 * line - c[1]))
            else:
                print("Yikes")

    return folded_coords


print(len(perform_fold(coords, folds[0])))

xmax = max(c[0] for c in coords)
ymax = max(c[1] for c in coords)

for fold in folds:
    coords = perform_fold(coords, fold, xmax, ymax)
    axis, line = fold
    if axis == "x":
        xmax = line - 1
    else:
        ymax = line - 1

for y in range(ymax + 1):
    line = ["#" if (x, y) in coords else "." for x in range(xmax + 1)]
    print("".join(line))
