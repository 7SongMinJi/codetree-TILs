n, m = map(int, input().split())

arr_2d_1 = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr_2d_2 = [
    list(map(int, input().split()))
    for _ in range(n)
]

# arr_2d_3 = [
#     0 if a == b else 1 for a in 
# ]

arr_2d_3 = [
    [0] * m for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if arr_2d_1[i][j] == arr_2d_2[i][j]:
            arr_2d_3[i][j] = 0
        else:
            arr_2d_3[i][j] = 1

for row in arr_2d_3:
    for elem in row:
        print(elem, end=" ")
    print()