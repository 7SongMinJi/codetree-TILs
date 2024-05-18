# # 2차원 배열과 for문

# # n * n 크기의 격자에 규칙에 맞춰 숫자를 출력하는 문제
# # 홀수 번째 행에 대해서는 우측으로 이동하며 숫자를 적고, 짝수 번째 행에 대해서는 좌측으로 이동하며 숫자를 적는 식으로 코드를 작성
# # 0번째 행 = 첫 번째 행 = 홀수 번째 행!!!!! 주의 *****
# n = 4
# arr_2d = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]
# num = 1
# for i in range(n):
#     if i % 2 == 0:
#         for j in range(n):
#             arr_2d[i][j] = num
#             num += 1
#     else:
#         for j in range(n - 1, -1, -1):
#             arr_2d[i][j] = num
#             num += 1
# # 출력
# for row in arr_2d:
#     for elem in row:
#         print(elem, end=" ")
#     print()


# 문제

n = int(input())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1
for j in range(n):
    for i in range(n):
        arr_2d[i][j] = num
        num += 1

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()