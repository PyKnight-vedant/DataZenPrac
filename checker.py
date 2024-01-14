import pandas as pd
import numpy as np


df = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (4).csv", index_col=0)

print(len(df))
print()
print("Phone")
print(df["Phone"].notnull().sum())
print("Address")
print(df["Address"].notnull().sum())
print("Lat-Long")
print(df["Lat-Long"].notnull().sum())
print("Email")
print(df["Email"].notnull().sum())

for i in range(1, len(df)+1):
    if isinstance(df.loc[i, "Email"], float) and isinstance(df.loc[i, "Phone"], float):
        df.drop(i, inplace=True)
print()
print(len(df))

l = []
for i in range(1, len(df)+1):
    l.append(i)

df.index = l

df.to_csv(r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (4).csv")
