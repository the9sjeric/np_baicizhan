# 导入模块
import pandas as pd
import matplotlib.pyplot as plt

# 读取路径为/Users/express/近一年快递信息.csv的文件，赋值给变量df
df = pd.read_csv("近一年快递信息.csv")

# TODO 将日期列数据转化为时间格式
df["日期"] = pd.to_datetime(df["日期"])

# TODO 将日期列设为行索引，并对原DataFrame df立即生效
df = df.set_index("日期")

# TODO 使用rolling()和mean()函数，将min_periods参数设置为1
# 计算揽收量的7日移动均值，并赋值给变量collect_mean
collect_mean = df["揽收量"].rolling(window=7, min_periods=1).mean()

# TODO 使用rolling()和mean()函数，将min_periods参数设置为1
# 计算发出量的7日移动均值，并赋值给变量deliver_mean
deliver_mean = df["发出量"].rolling(window=7, min_periods=1).mean()

# 数据可视化
# 显示中文标签
plt.rcParams['font.sans-serif'] = ["SimHei"]
# 绘制原始数据和揽收量7日移动均线图
plt.subplot(2,1,1)
plt.plot(collect_mean.index,collect_mean.values,color="red")
plt.plot(df.index,df["揽收量"],color="gray")
plt.xlabel("日期")
plt.ylabel("揽收量")

# 绘制原始数据和发出量7日移动均线图
plt.subplot(2,1,2)
plt.plot(deliver_mean.index,deliver_mean.values,color="orange")
plt.plot(df.index,df["发出量"],color="skyblue")
plt.xlabel("日期")
plt.ylabel("发出量")
plt.show()