n = int(input())

for i in range(1, n + 1):
    x = int(input())
    if x % 2 == 1 and x % 3 == 0:
        print(x)