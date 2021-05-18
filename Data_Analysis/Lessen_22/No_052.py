# TODO 导入模块
import pandas as pd

# TODO 读取文件，并赋值给变量df
df = pd.read_csv("最近一年单量信息.csv")
# TODO 获得外卖单量列中存在缺失值的行，并赋值给变量df_null
df_null = df[df["外卖单量"].isnull()]
# TODO 计算df外卖单量列的7日移动均值，并赋值给变量rolling_mean
rolling_mean = df["外卖单量"].rolling(window=7,min_periods=1).mean()
# TODO 将rolling_mean取整，赋值给变量round_rolling_mean
round_rolling_mean = rolling_mean.round(0)
# TODO 用round_rolling_mean的值填充缺失值
df["外卖单量"].fillna(round_rolling_mean[df_null.index],inplace=True)
# TODO 计算总单量，并赋值给df["总单量"]
df["总单量"] = df["堂食单量"] + df["打包单量"] + df["外卖单量"]
# TODO 输出df["总单量"]
print(df["总单量"])