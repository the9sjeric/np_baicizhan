import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("bilibili.csv")

df["date"] = pd.to_datetime(df["date"])

danmu_sum = df["danmu"].groupby(df["author"]).sum()
reply_sum = df["reply"].groupby(df["author"]).sum()
view_sum = df["view"].groupby(df["author"]).sum()
video_sum = df["title"].groupby(df["author"]).count()
jiange = df["date"].groupby(df["author"]).max()  - df["date"].groupby(df["author"]).min()
likes_sum = df["likes"].groupby(df["author"]).sum()
fav_sum = df["favorite"].groupby(df["author"]).sum()
coins_sum = df["coins"].groupby(df["author"]).sum()
df1 = pd.merge(danmu_sum,reply_sum,left_index=True, right_index=True)
df2 = pd.merge(df1,view_sum,left_index=True, right_index=True)
df3 = pd.merge(df2,video_sum,left_index=True, right_index=True)
df4 = pd.merge(df3,jiange,left_index=True, right_index=True)
df5 = pd.merge(df4,likes_sum,left_index=True, right_index=True)
df6 = pd.merge(df5,fav_sum,left_index=True, right_index=True)
df7 = pd.merge(df6,coins_sum,left_index=True, right_index=True)

df8 = df7[df7["title"] >= 5]
df8["I"] = (df8["danmu"] + df8["reply"]) / df8["view"] / df8["title"] * 100
df8["F"] = 1 / (df8["date"].dt.days + 1) / df8["title"] * 100
df8["L"] = (df8["likes"] + df8["coins"] + df8["favorite"]) / df8["view"] * 100
df8["I"] = pd.qcut(df8["I"],q=5,labels=[1,2,3,4,5])
df8["F"] = pd.qcut(df8["F"],q=5,labels=[1,2,3,4,5])
df8["L"] = pd.qcut(df8["L"],q=5,labels=[1,2,3,4,5])
def Trans(x):
    if x > 3:
        return 1
    else:
        return 0
df8["I"] = df8["I"].apply(Trans)
df8["F"] = df8["F"].apply(Trans)
df8["L"] = df8["L"].apply(Trans)
df8["IFL"] = df8["I"].astype(str) + df8["F"].astype(str) + df8["L"].astype(str)
def xT(a):
    if a == "111":
        return "高质量UP主"
    elif a == "101":
        return "高质量拖更UP主"
    elif a == "011":
        return "高质量内容高深UP主"
    elif a == "001":
        return "高质量内容高深拖更UP主"
    elif a == "110":
        return "接地气活跃UP主"
    elif a == "100":
        return "接地气UP主"
    elif a == "010":
        return "活跃UP主"
    elif a  == "000":
        return "还在成长的UP主"

df8["IFL"] = df8["IFL"].apply(xT)
data = df8["IFL"].groupby(df8["IFL"]).count() / df8["IFL"].count()

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.bar(data.index,data.values)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print(data)