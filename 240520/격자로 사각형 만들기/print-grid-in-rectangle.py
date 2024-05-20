n = int(input())

arr_2d = [
    [0] * n
    for _ in range(n)
]

for i in range(n):
    arr_2d[0][i] = 1
    arr_2d[i][0] = 1

for i in range(1, n):
    for j in range(1, n):
        arr_2d[i][j] = arr_2d[i - 1][j - 1] + arr_2d[i - 1][j] + arr_2d[i][j - 1]

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()

# // 처음에는 틀림 왜냐하면 규칙에 따라 값 업데이트할 때 0행 0열은 제외시키고 해야 하니까!


# 정답 코드