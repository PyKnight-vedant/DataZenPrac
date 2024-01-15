import pandas as pd
import os

df = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (4).csv", index_col=0)

# List of cities to filter
cities_to_filter = ["Kerala", "Mumbai", "Pune",
                    "Bangalore", "Chennai", "Kolkata", "Nagpur", "Thane"]
miscellaneous_df = df[~df['City'].isin(cities_to_filter)]
# Filtering the DataFrame
filtered_df = df[df['City'].isin(cities_to_filter)]
l = []
for i in range(1, len(miscellaneous_df)+1):
    l.append(i)
miscellaneous_df.index = l

# Display the filtered DataFrame
print(filtered_df)
print("True:", len(filtered_df))


print("Miscellaneous:", len(miscellaneous_df))

for city in miscellaneous_df.City.unique():
    if isinstance(city, float):
        for sector in miscellaneous_df.Sector.unique():
            working_df = pd.DataFrame(columns=miscellaneous_df.columns)
            for i in range(1, len(miscellaneous_df)+1):
                if miscellaneous_df.loc[i, "Sector"] == sector and miscellaneous_df.loc[i, "City"] == city:
                    working_df.loc[i, :] = miscellaneous_df.loc[i, :]

            city = "Unfound "
            directory = f"C:\\Users\\Vedant\\Desktop\\DataZenPrac\\DATABASE\\miscellaneous\\{city.strip()}"
            os.makedirs(directory, exist_ok=True)
            working_df.to_csv(os.path.join(
                directory, f"{sector}.csv"), index=False)
