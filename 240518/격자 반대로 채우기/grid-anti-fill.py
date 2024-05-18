n = int(input())

arr_2d = [
    [0] * n
    for _ in range(n)
]

num = 1

for j in range(n-1, -1, -1):
    if j % 2 == 1:
        for i in range(n-1, -1, -1):
            arr_2d[i][j] = num
            num += 1
    else:
        for i in range(n):
            arr_2d[i][j] = num
            num += 1

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()