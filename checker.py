import pandas as pd

df = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\D2Build.csv", index_col=0)

df1 = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (3).csv", index_col=0)

df2 = pd.concat([df1, df])

print(df2)

df2.to_csv(r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (3).csv")
