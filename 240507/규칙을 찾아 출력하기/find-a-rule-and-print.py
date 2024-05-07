n = int(input())

for i in range(n):
    for j in range(n):
        if i != 0 and i != (n-1) and j != 0 and j != (n-1) and i <= j:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()