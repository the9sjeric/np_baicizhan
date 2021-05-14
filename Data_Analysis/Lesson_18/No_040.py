import os
import pandas as pd

path = "azhen"
dfList = []
allItems = os.listdir(path)
for item in allItems:
    file = os.path.join(path,item)
    df = pd.read_csv(file)
    dfList.append(df)
dfAll = pd.concat(dfList)
print(dfAll)