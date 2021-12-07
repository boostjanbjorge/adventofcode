import pandas as pd; import math; import operator

df = pd.read_csv("day3.txt", names=("n",), converters={"n": lambda x: int(x, 2)})
def calc(df, op=operator.eq, bits=12):
    for i in reversed(range(bits)):
        if len(df) == 1:
            break
        common = ((df.n & (1 << i)) > 0).astype(int)
        df = df[op(common, math.ceil(common.median()))]
    return int(df.iloc[-1])

val = calc(df.copy()) * calc(df, op=operator.ne)
print(val)
