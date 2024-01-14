import pandas as pd

df = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (4).csv", index_col=0)


# List of cities to filter
cities_to_filter = ["Kerala", "Mumbai", "Pune",
                    "Bangalore", "Chennai", "Kolkata", "Nagpur", "Thane"]

# Filtering the DataFrame
filtered_df = df[df['City'].isin(cities_to_filter)]

# Display the filtered DataFrame
print(filtered_df)
print("True:", len(filtered_df))

miscellanious_df = df[~df['City'].isin(cities_to_filter)]

print("Miscellaneous:", len(miscellanious_df))
print(miscellanious_df.City.unique())
