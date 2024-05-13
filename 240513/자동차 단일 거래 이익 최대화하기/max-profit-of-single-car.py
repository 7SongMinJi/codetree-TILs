n = int(input())
arr = list(map(int, input().split()))

max_val = 0

for i in range(1, n):
    for j in range(1, i):
        if max_val < arr[i] - arr[j]:
            max_val = arr[i] - arr[j]

print(max_val)