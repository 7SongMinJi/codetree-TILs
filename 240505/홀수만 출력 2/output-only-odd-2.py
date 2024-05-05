arr = input().split()

a = int(arr[1])
b = int(arr[0])

for i in range(b, a - 1, -2):
    print(i, end=" ")