import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("avocado.csv")
plt.rcParams["font.sans-serif"] = ["SimHei"]

df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

USA_M_MeanPrice = df.resample("M").mean()
Region_M_MeanPrice = df.groupby("region").resample("M").mean()
print(Region_M_MeanPrice)
NewYork_M = Region_M_MeanPrice.loc["NewYork"]
Chicago_M = Region_M_MeanPrice.loc["Chicago"]


plt.plot(NewYork_M.index,NewYork_M["AveragePrice"],color="skyblue",marker="o",label="纽约价格水平")
plt.legend()

plt.plot(Chicago_M.index,Chicago_M["AveragePrice"],color="blue",marker="o",label="芝加哥价格水平")
plt.legend()

plt.plot(USA_M_MeanPrice.index,USA_M_MeanPrice["AveragePrice"],color="green",marker="o",label="全美价格水平")
plt.xlabel("时间")
plt.ylabel("价格水平")
plt.legend(loc="upper left")

plt.show()