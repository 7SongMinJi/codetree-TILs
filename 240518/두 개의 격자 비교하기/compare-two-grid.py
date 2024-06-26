# n, m = map(int, input().split())

# arr_2d_1 = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]

# arr_2d_2 = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]

# # arr_2d_3 = [
# #     0 if a == b else 1 for a in 
# # ]

# arr_2d_3 = [
#     [0] * m for _ in range(n)
# ]

# for i in range(n):
#     for j in range(m):
#         if arr_2d_1[i][j] == arr_2d_2[i][j]:
#             arr_2d_3[i][j] = 0
#         else:
#             arr_2d_3[i][j] = 1

# for row in arr_2d_3:
#     for elem in row:
#         print(elem, end=" ")
#     print()


# 정답 코드 - arr_2 부분 표현 잘 보기!! *****

# n, m을 입력받습니다.
n, m = tuple(map(int, input().split()))

# 첫 번째 2차원 배열을 구현해 정수를 입력받습니다.
arr_1 = [
	list(map(int, input().split()))
	for _ in range(n)
]

# 두 번째 2차원 배열을 구현해 정수를 입력받습니다.
arr_2 = [
	list(map(int, input().split()))
	for _ in range(n)
]
	
# 두 배열의 같음 여부를 새로운 배열에 담습니다. *****
arr_3 = [
	[1 if arr_1[i][j] != arr_2[i][j] else 0 for j in range(m)]
	for i in range(n)
]

# 새로운 배열을 출력합니다.
for row in arr_3:
	for elem in row:
		print(elem, end=" ")
	print()