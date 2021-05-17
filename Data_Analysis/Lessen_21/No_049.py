import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/huanhuan/bilibili.csv")
data = df["coins"].groupby(df["author"]).count()

df = df[df["author"] == data.index]
print(data)
