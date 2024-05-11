arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 999 or arr[i] == -999:
        break

arr = arr[:i]

min_val, max_val = arr[0], arr[0]

for elem in arr:
    if min_val > elem:
        min_val = elem
    if max_val < elem:
        max_val = elem

print(max_val, min_val)