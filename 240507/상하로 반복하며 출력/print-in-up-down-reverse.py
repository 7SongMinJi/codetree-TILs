n = int(input())

for i in range(4):
    for j in range(4):
        if j % 2 == 0:
            print(i + 1, end="")
        else:
            print(4 - i, end="")
    print()