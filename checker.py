import pandas as pd
import numpy as np

df1 = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\restraurants_Aditya.csv", index_col=0)

df = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (4).csv", index_col=0)

print(df)
print(df1)

df = pd.concat([df, df1])

df.to_csv(r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (4).csv")
