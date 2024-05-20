n, m = tuple(map(int, input().split()))

placed = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

cnt = 1

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    placed[r][c] = cnt
    cnt += 1

for i in range(1, m):
    for j in range(1, m):
        print(placed[i][j], end=" ")
    print()