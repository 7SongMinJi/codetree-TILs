n = int(input())

arr = list()
arr.append(1)
arr.append(n)
i = 1

while True:
    arr.append(arr[i - 1] + arr[i])
    i += 1
    if arr[i] >= 100:
        break

for elem in arr:
    print(elem, end=" ")