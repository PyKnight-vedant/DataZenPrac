import pandas as pd
import numpy as np

df = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\Final_Gyms.csv", index_col=0)
print(df)
df.City = ""
for i in df.index:
    l = df.loc[i, "Name"].split("-")
    df.loc[i, "City"] = l[-1].strip()

df.to_csv(r"C:\Users\Vedant\Desktop\DataZenPrac\Final_Gyms.csv")
