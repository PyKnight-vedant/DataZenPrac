import pandas as pd
import numpy as np


df = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (3).csv", index_col=0)
print(df[df["Sector"] == "Gym"])
