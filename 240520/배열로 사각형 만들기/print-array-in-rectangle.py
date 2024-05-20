# # 순서대로 채우기

# # n * n 크기의 격자에서
# # 첫 번째 행은 전부 숫자 1로 이루어져 있고,
# # 두 번째 행부터는 바로 위의 칸에 적혀있는 숫자에 2를 더해서 적어주는 코드

# # 첫 번째 행에 전부 숫자 1을 채우기 -> 두 번째 행부터 마지막 행까지 전부 숫자 채우기 -> 결과 출력
# n = 3
# arr_2d = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]
# # 1. 첫 번째 행에 전부 숫자 1을 채우기
# for j in range(n):
#     arr_2d[0][j] = 1
# # 2. 두 번째 행부터 마지막 행까지 전부 숫자를 채우기
# for i in range(1, n):
#     for j in range(n):
#         arr_2d[i][j] = arr_2d[i - 1][j] + 2
# # 3. 출력
# for row in arr_2d:
#     for elem in row:
#         print(elem, end=" ")
#     print()


# 문제
arr_2d = [
    [0] * 5
    for _ in range(5)
]
for i in range(5):
    for j in range(5):
        if i == 0 or j == 0:
            arr_2d[i][j] = 1
        else:
            arr_2d[i][j] = arr_2d[i - 1][j] + arr_2d[i][j - 1]

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()