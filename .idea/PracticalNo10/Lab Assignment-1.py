import pandas as pd

# Load CSV
df = pd.read_csv("books.csv")

# a) Complete report in tabular form
print("\n--- Complete Book Report ---")
print(df)

# b) List of books of a given author
author_name = input("\nEnter author name: ")
print(f"\nBooks by {author_name}:")
print(df[df['author'] == author_name])

# c) Books of a given publishing house
publisher_name = input("\nEnter publisher name: ")
print(f"\nBooks by {publisher_name}:")
print(df[df['publisher'] == publisher_name])

# d) Cheapest and costliest book
cheapest = df.loc[df['price'].idxmin()]
costliest = df.loc[df['price'].idxmax()]

print("\nCheapest Book:")
print(cheapest)

print("\nCostliest Book:")
print(costliest)

# e) Sort by year of publication
print("\nBooks sorted by publication year:")
print(df.sort_values(by='publication_year'))