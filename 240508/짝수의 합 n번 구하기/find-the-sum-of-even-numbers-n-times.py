n = int(input())

for i in range(n):
    sum_val = 0
    arr = input().split()
    a, b = int(arr[0]), int(arr[1])

    for j in range(a, b + 1):
        if j % 2 == 0:
            sum_val += j
    print(sum_val)