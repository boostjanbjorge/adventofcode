import pandas as pd
df = pd.read_csv("day2.txt", names=("dir", "val"), delim_whitespace=True)
def aim(row):
    if row.dir=="down":
        return row.val
    elif row.dir == "up":
        return -row.val
    return 0
df["aim"] = df.apply(aim, axis=1).cumsum()
depth = df.apply(lambda row: row.val*row.aim if row.dir == "forward" else 0, axis=1).cumsum().iloc[-1]
position = df.apply(lambda row: row.val if row.dir == "forward" else 0, axis=1).cumsum().iloc[-1]
print(depth*position)
