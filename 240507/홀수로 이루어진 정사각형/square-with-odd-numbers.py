n = int(input())

for i in range(n):
    for j in range(n):
        print(2 * (j + 5) + (2 * i + 1), end=" ")
    print()