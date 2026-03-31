# p
# y y
# t t t
# h h h h
# o o o o o
# n n n n n n

word = "python"

for i in range(len(word)):
    for j in range(i + 1):
        print(word[j], end=" ")
    print()