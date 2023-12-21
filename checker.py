import pandas as pd
import numpy as np


df = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (3).csv", index_col=0)

df1 = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\Final_Gym.csv")

df1.index = df1.index+5280
df = pd.concat([df, df1])
print(df)

df.to_csv(r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (3).csv")
