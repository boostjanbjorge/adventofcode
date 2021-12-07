import pandas as pd
sums = pd.read_csv("day2.txt", index_col="dir", names=("dir", "val"), delim_whitespace=True).groupby("dir").sum().transpose()
print((sums["down"] - sums["up"])*sums["forward"])
