import pandas as pd
df = pd.read_csv("day3.txt", names=("n",), converters={"n": lambda x: int(x, 2)})
gamma = 0
for i in range(12):
    gamma |= int(((df["n"] & (1 << i)) > 0).median()) << i
print(gamma * (~gamma & 0xfff))
