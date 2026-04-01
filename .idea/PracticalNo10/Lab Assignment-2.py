import pandas as pd

# Create data for 5 states
data = {
    "State": ["State1", "State2", "State3", "State4", "State5"],
    "Area": [50000, 70000, 60000, 80000, 55000],  # in sq km
    "Population": [1000000, 1500000, 1200000, 2000000, 1100000]
}

df = pd.DataFrame(data)

# a) Complete information
print("\n--- State Information ---")
print(df)

# b) State with largest Area
largest_area = df.loc[df['Area'].idxmax()]
print("\nState with largest area:", largest_area['State'])

# c) State with largest Population
largest_pop = df.loc[df['Population'].idxmax()]
print("State with largest population:", largest_pop['State'])

# d) Population Density
df['Density'] = df['Population'] / df['Area']

print("\n--- With Population Density ---")
print(df)

# e) State with highest population density
highest_density = df.loc[df['Density'].idxmax()]
print("\nState with highest population density:", highest_density['State'])