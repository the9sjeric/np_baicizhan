import pandas as pd

df = pd.read_csv("stock_data.csv", usecols=["date", "close"])

df["date"] = pd.to_datetime(df["date"])
df.set_index(["date"], inplace=True)

ma10 = df.rolling(window=10, min_periods=1).mean()
ma10_model = df["close"] > ma10["close"]


def get_buy_date(w):
    return w[0] == False and w[1] == True


def get_sale_date(v):
    return v[0] == True and v[1] == False


se_buy = ma10_model.rolling(window=2).apply(get_buy_date).fillna(0)
se_sale = ma10_model.rolling(window=2).apply(get_sale_date).fillna(0)

# TODO 使用astype()函数对买入时点se_buy转换为布尔型Series，赋值给变量se_buy_bool
se_buy_bool = se_buy.astype(bool)

# TODO 使用astype()函数对卖出时点se_sale转换为布尔型Series，赋值给变量se_sale_bool
se_sale_bool = se_sale.astype(bool)

# TODO 使用布尔索引筛选出df中的买点收盘价，赋值给变量buy_price
buy_price = df[se_buy_bool]

# TODO 使用布尔索引筛选出df中的卖点收盘价，赋值给变量sale_price
sale_price = df[se_sale_bool]

# TODO 如果有100000块为本金，赋值给变量all_money
all_money = 100000
# TODO 定义余额变量remain，交易前余额等于本金
remain = all_money

# TODO 使用len()函数计算交易次数，次数为sale_price的长度，赋值给变量times
times = len(sale_price)

# TODO 通过for循环模拟每次交易，循环次数为times
for i in range(0, times):
    # TODO 计算每次交易前能买入的股数，股数=余额/买点价格，买点价格通过.iloc属性得到，赋值给变量buy_count
    buy_count = remain / buy_price.iloc[i]
    # TODO 计算每次交易后的余额，余额=股数*卖点价格，卖点价格通过.iloc属性得到，赋值给变量remain
    remain = buy_count * sale_price.iloc[i]

# TODO 计算收益率，收益率 =（余额-本金）/本金，赋值给变量profit_rate
profit_rate = (remain - all_money) / all_money

# TODO 格式化输出收益率：50次交易之后，收益率为{profit_rate}
print(f"50次交易之后，收益率为{profit_rate.values[0]}")
