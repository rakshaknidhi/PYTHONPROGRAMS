# A
# A B
# A B C
# A B C D
# A B C D E

for i in range(1, 6):
    ch = ord('A')
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()