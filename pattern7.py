# 2
# 4 6
# 8 10 12
# 14 16 18 20

num = 2

for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()