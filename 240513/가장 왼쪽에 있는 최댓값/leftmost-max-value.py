n = int(input())
arr = list(map(int, input().split()))

i = n

while True:
    max_idx, max_val = 0, arr[0]

    for j in range(i):
        if max_val < arr[j]:
            max_idx = j
            max_val = arr[j]
    
    print(max_idx + 1, end=" ")

    if max_idx == 0:
        break

    i = max_idx