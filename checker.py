import pandas as pd
import numpy as np


df = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (4).csv", index_col=0)

for i in df.columns:
    print(i, "-", df.loc[:, i].value_counts().sum())
