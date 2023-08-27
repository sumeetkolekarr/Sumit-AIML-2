import pandas as pd
df = pd.read_csv("SpiderVerse.csv")

Stat = [df['Rating']]

# print(df.describe())
print(df['Rating'].quantile(0.5))