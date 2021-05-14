import pandas as pd
import matplotlib.pyplot as plt

dataA = pd.read_excel("202001.xlsx", sheet_name=0)
dataB = pd.read_excel("202001.xlsx", sheet_name=1)
dataC = pd.read_excel("202001.xlsx", sheet_name=2)

data = pd.concat([dataA, dataB, dataC])
wares_count = data["商品名称"].value_counts()

plt.rcParams["font.sans-serif"] = ["SimHei"]
wares_count.plot.bar()
plt.tight_layout()
plt.show()
