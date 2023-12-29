import pandas as pd
import numpy as np


df = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (4).csv", index_col=0)

df1 = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\Aditya_Deliverable (4).csv", index_col=0)
print(df)
print(len(df))
print("Phone")
print(df["Phone"].notnull().sum())
print("Address")
print(df["Address"].notnull().sum())
print("Lat-Long")
print(df["Lat-Long"].notnull().sum())


df.loc[:3320, :] = df1

# df.to_csv(r"C:\Users\Vedant\Desktop\DataZenPrac\Hriday_Deliverable.csv")


df.to_csv(r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (4).csv")
print(len(df))
print("Phone")
print(df["Phone"].notnull().sum())
print("Address")
print(df["Address"].notnull().sum())
print("Lat-Long")
print(df["Lat-Long"].notnull().sum())
