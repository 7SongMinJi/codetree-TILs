# # 2차 격자점으로서의 배열

# # 2차 평면 상에 n개의 점이 주어졌을 때, (a, b)가 해당 점들 중 하나인지 판단하는 방법
# a, b = 1, 3
# exists = False
# for _ in range(n):
#     r, c = tuple(map(int, input().split()))
#     if r == a and c == b:
#         exists = True
# print(exists)
# # BUT 일일이 모든 점에 대해 확인하는 것은 굉장히 비효율적인 방법

# # 만약 점들의 위치 (r, c)의 범위가 1에서 10 사이라면 다음과 같이 0으로 초기화된 2차원 배열을 만든 뒤,
# # 각 점들이 주어질 때마다 해당 위치에 1로 표시해주는 방식으로 해결 가능
# # 단, 이때 for문을 11까지 돌아야 함에 유의! ***
# a, b = 1, 3
# placed = [
#     [0 for _ in range(11)]
#     for _ in range(11)
# ]
# for _ in range(n):
#     r, c = tuple(map(int, input().split()))
#     placed[r][c] = 1
# exists = True if placed[a][b] == 1 else False
# # 윗줄 문법 알아두기!!
# print(exists)

# # 만약 0번지부터 값을 채우는 식으로 진행하려면, placed 배열의 (r, c)가 아닌 (r - 1, c - 1)에 표기하는 식으로 하기!
# # 이번에는 11이 아닌 10까지만 배열을 만들어도 됨!
# a, b = 1, 3
# placed = [
#     [0 for _ in range(10)]
#     for _ in range(10)
# ]
# for _ in range(n):
#     r, c = tuple(map(int, input().split()))
#     placed[r - 1][c - 1] = 1
# exists = True if placed[a - 1][b - 1] == 1 else False
# print(exists)


# 문제

n, m = map(int, input().split())

placed = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    placed[r - 1][c - 1] = 1

for row in placed:
    for elem in row:
        print(elem, end=" ")
    print()