import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api

df = pd.read_csv("jetrail.csv")

df["Datetime"] = pd.to_datetime(df['Datetime'])
df = df.set_index('Datetime')
print(df)