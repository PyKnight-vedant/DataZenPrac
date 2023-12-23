import pandas as pd
import numpy as np


df = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (3).csv", index_col=0)


print(df)
# df.to_csv(r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (3).csv")

df1 = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\Db_1.csv", index_col=0)

print(df1)

total_df = pd.concat([df, df1])

total_df.to_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (3).csv")
