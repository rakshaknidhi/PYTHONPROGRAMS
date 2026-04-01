# Take input and store in tuple
n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

t = tuple(numbers)

# a) Print total number of items
print("Total items:", len(t))

# b) Print the last item
print("Last item:", t[-1])

# c) Print tuple elements in reverse order
print("Reverse order:", t[::-1])

# d) Print 'S' if number is even, else 'N'
print("Even/Odd check:")
for i in t:
    if i % 2 == 0:
        print(i, "-> S")
    else:
        print(i, "-> N")

# e) Remove first and last items, sort remaining
new_tuple = t[1:-1]
sorted_tuple = tuple(sorted(new_tuple))

print("After removing first and last & sorting:", sorted_tuple)