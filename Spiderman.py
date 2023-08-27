import pandas as pd
df = pd.read_csv("SpiderMan.csv")

Stat = [df['Rating']]

d = pd.DataFrame(Stat)
# print(df.describe())
print(df['Rating'].quantile(0.5))