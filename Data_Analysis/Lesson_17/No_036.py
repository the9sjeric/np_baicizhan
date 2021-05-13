import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("train.csv")

#plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]
plt.rcParams["font.sans-serif"] = ["SimHei"]

plt.subplot(1,2,1)
SP = data.groupby("Pclass")["Survived"].sum()
SPall = data.groupby("Pclass")["Survived"].count()
SPrate = SP / SPall

SPrate.plot.bar("Pclass","Survived")
plt.xlabel("Pclass")
plt.ylabel("存活率")
plt.title("各船舱存活情况")
plt.xticks(rotation=0)

plt.subplot(1,2,2)
SS = data.groupby("Sex")["Survived"].sum()
SSall = data.groupby("Sex")["Survived"].count()
SSrate = SS / SSall
SSrate.plot.bar("Sex","Survived")
plt.xlabel("Sex")
plt.ylabel("存活率")
plt.title("各性别存活情况")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
