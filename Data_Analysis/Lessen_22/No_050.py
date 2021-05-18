# 导入模块
import pandas as pd
import matplotlib.pyplot as plt

# TODO 读取路径为/Users/stock/gongshang.csv的文件，赋值给变量df_B


# TODO 读取路径为/Users/stock/minsheng.csv的文件，赋值给变量df_C


# TODO 使用to_datetime函数将df_B中date列数据转化为时间格式，赋值给df_B["date"]


# TODO 使用set_index函数将date列设为行索引，并对原DataFrame df_B生效


# TODO 使用to_datetime函数将df_C中date列数据转化为时间格式，赋值给df_C["date"]


# TODO 使用set_index函数将date列设为行索引，并对原DataFrame df_C生效


# TODO 使用rolling()和mean()函数，将min_periods参数设置为1
# 计算df_B收盘价(close列)的5日移动均值，并赋值给变量ma5_B


# TODO 使用rolling()和mean()函数，将min_periods参数设置为1
# 计算df_C收盘价(close列)的5日移动均值，并赋值给变量ma5_C


# 数据可视化
# 显示中文标签
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# 绘制B、C三支股票的5日移动均线图
plt.plot(ma5_B.index,ma5_B.values,color="blue")
plt.plot(ma5_C.index,ma5_C.values,color="orange")
plt.xlabel("日期")
plt.ylabel("收盘价")
plt.show()