import pandas as pd
df = pd.read_csv("SpiderMan.csv")

Stat = [df['Rating']]

d = pd.DataFrame(Stat)
# print(df.describe())
print(df['Rating'].quantile(0.5))
a = (df['Rating'].quantile(0.25))
b = (df['Rating'].quantile(0.75))
c = b - a
print("The IQR is", c)
# print(df['Rating'].quantile(0.5))