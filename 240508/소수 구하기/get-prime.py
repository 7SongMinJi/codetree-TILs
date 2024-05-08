n = int(input())
arr = []

for i in range(2, n + 1):
    cnt = 0
    for j in range(1, i):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        arr.append(i)

arr.sort()

for i in range(len(arr)):
    print(arr[i], end=" ")