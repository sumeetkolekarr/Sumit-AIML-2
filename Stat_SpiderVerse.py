import pandas as pd
df = pd.read_csv("SpiderVerse.csv")


A = (df['Rating'] == 1.0).sum()
B = (df['Rating'] == 2.0).sum()
C = (df['Rating'] == 3.0).sum()
D = (df['Rating'] == 4.0).sum()
E = (df['Rating'] == 5.0).sum()
F = (df['Rating'] == 6.0).sum()
G = (df['Rating'] == 7.0).sum()
H = (df['Rating'] == 8.0).sum()
I = (df['Rating'] == 9.0).sum()
J = (df['Rating'] == 10.0).sum()

print("The Frequency Distribution is\n")
print(f"The No. of 1.0 Rating is {A}")
print(f"The No. of 2.0 Rating is {B}")
print(f"The No. of 3.0 Rating is {C}")
print(f"The No. of 4.0 Rating is {D}")
print(f"The No. of 5.0 Rating is {E}")
print(f"The No. of 6.0 Rating is {F}")
print(f"The No. of 7.0 Rating is {G}")
print(f"The No. of 8.0 Rating is {H}")
print(f"The No. of 9.0 Rating is {I}")
print(f"The No. of 10.0 Rating is {J}")