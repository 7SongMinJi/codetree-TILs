n, m = map(int, input().split())

arr_2d = [
    [0] * m
    for _ in range(n)
]

i, j, cnt = 0, 0, 1

while i <= n-1 and j <= m-1:
    arr_2d[i][j] = cnt
    cnt += 1
    if i < j:
        i += 1
        j -= 1
    elif i >= j and j != 0:
        i -= 1
        j += 1
    else:
        j = i + 1
        i = 0

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()

# [i][j]
# [0][0]

# [0][1]
# [1][0]

# [0][2]
# [1][1]
# [2][0]

# [0][3]
# [1][2]
# [2][1]
# [3][0]