# Input prices
n = int(input("Enter number of items sold: "))
prices = []

for i in range(n):
    price = int(input(f"Enter price of item {i+1}: "))
    prices.append(price)

t = tuple(prices)

# a) Total number of items
print("Total items sold:", len(t))

# b) Cheapest item
print("Cheapest item:", min(t))

# c) Costliest item
print("Costliest item:", max(t))

# d) Prices in ascending order
print("Ascending order:", tuple(sorted(t)))

# e) Number of costliest items sold
max_price = max(t)
count = t.count(max_price)

print("Number of costliest items sold:", count)