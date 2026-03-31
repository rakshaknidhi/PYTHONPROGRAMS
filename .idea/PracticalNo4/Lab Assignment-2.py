import numpy as np

print("Enter elements for 5x3 matrix:")
A = []
for i in range(5):
    row = list(map(int, input(f"Enter row {i+1} (3 values): ").split()))
    A.append(row)

print("\nEnter elements for 3x2 matrix:")
B = []
for i in range(3):
    row = list(map(int, input(f"Enter row {i+1} (2 values): ").split()))
    B.append(row)

# Convert to NumPy arrays
A = np.array(A)
B = np.array(B)

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Multiplication
product = np.dot(A, B)

print("\nProduct Matrix (A x B):")
print(product)