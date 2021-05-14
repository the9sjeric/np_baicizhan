# 导入模块
import pandas as pd
# 定义一个字典raw_data_1
raw_data_1 = {
        "project_id": ["1", "2", "3", "4", "5"],
        "first_name": ["Alex", "Amy", "Allen", "Alice", "Ayoung"],
        "last_name": ["Anderson", "Ackerman", "Ali", "Aoni", "Atiches"]}
# 定义一个字典raw_data_2
raw_data_2 = {
        "project_id": ["6", "7", "8", "9", "10"],
        "first_name": ["Billy", "Brian", "Bran", "Bryce", "Betty"],
        "last_name": ["Bonder", "Black", "Balwner", "Brice", "Btisan"]}

# TODO 使用pd.DataFrame()函数，根据raw_data_1构造一个DataFrame
# 将结果赋值给data1
data1 = pd.DataFrame(raw_data_1)

# TODO 使用pd.DataFrame()函数，根据raw_data_2构造一个DataFrame
# 将结果赋值给data2
data2 = pd.DataFrame(raw_data_2)

# TODO 使用pd.concat()函数
# 按照垂直方向将data1、data2合并，并赋值给变量all_data
all_data = pd.concat([data1,data2])

# TODO 输出all_data
print(all_data)

# TODO 使用pd.concat()函数
# 按照水平方向将data1、data2合并，并赋值给变量all_data_col
all_data_col = pd.concat([data1,data2],axis=1)

# TODO 输出all_data_col
print(all_data_col)