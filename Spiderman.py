import pandas as pd
df = pd.read_csv("Sumit AIML-2\SpiderMan.csv")

Stat = [df['Rating']]

d = pd.DataFrame(Stat)

print(df.describe())
print("Median is",df['Rating'].quantile(0.5))
print("The Mean is",df['Rating'].mean())
a = (df['Rating'].quantile(0.25))
b = (df['Rating'].quantile(0.75))
c = b - a
print("The IQR is", c)
