import pandas as pd

df = pd.read_csv("index.csv")

print(df["C"])
print(df.iloc[:, -2:])
print(df.iloc[-10:, :2])