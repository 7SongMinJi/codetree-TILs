n = int(input())
arr_1d, arr_2d = [], []

# arr_2d = [
#     ([0] * (n + 1)) for _ in range(n)
#     for _ in range(n)
# ]
# // 이렇게 하면 틀린 거임!! *****

for i in range(n):
    arr_2d.append([0] * (i + 1))

for i in range(n):
    for j in range(i + 1):
        if j == 0 or i == j:
            arr_2d[i][j] = 1
        else:
            arr_2d[i][j] = arr_2d[i - 1][j - 1] + arr_2d[i - 1][j]

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()