arr = list(map(int, input().split()))

for i in range(8):
    arr.append(arr[-2] * 2 + arr[-1])

for elem in arr:
    print(elem, end=" ")