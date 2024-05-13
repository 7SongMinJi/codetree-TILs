n = int(input())
arr = list(map(int, input().split()))

temp = -1
max_val = arr[0]
overlap = list()

for i in range(1, n):
    if max_val < arr[i] and arr[i] not in overlap:
        temp, max_val = max_val, arr[i]
    elif max_val == arr[i]:
        max_val = temp
        overlap.append(arr[i])

if max_val > 0:
    print(max_val)
else:
    print(-1)