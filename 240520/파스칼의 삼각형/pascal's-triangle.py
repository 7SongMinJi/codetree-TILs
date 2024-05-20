# n = int(input())
# arr_1d, arr_2d = [], []

# # arr_2d = [
# #     ([0] * (n + 1)) for _ in range(n)
# #     for _ in range(n)
# # ]
# # // 이렇게 하면 틀린 거임!! *****

# for i in range(n):
#     arr_2d.append([0] * (i + 1))

# for i in range(n):
#     for j in range(i + 1):
#         if j == 0 or i == j:
#             arr_2d[i][j] = 1
#         else:
#             arr_2d[i][j] = arr_2d[i - 1][j - 1] + arr_2d[i - 1][j]

# for row in arr_2d:
#     for elem in row:
#         print(elem, end=" ")
#     print()


# 정답 코드 - 아래 코드 다시 잘 보기 *****

# 2차원 배열을 구현합니다.
arr = [
    [0 for _ in range(15)]
    for _ in range(15)
]
	
# n을 입력받습니다.
n = int(input())
	
# 배열의 각 행의 첫 열과 마지막 열을 1로 초기화합니다.
for i in range(n):
	arr[i][0] = 1
	arr[i][i] = 1
	
# 배열의 숫자를 채웁니다.
for i in range(n):
	for j in range(1, i):
		arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

# 채워진 배열을 출력합니다.
for i in range(n):
	for j in range(i + 1):
		print(arr[i][j], end=" ")
	print()