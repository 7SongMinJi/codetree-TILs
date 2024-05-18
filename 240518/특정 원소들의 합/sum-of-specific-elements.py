# arr_2d = [
#     list(map(int, input().split()))
#     for _ in range(4) 
# ]

# sum_val = 0

# for i in range(4):
#     for j in range(4):
#         if i >= j:
#             sum_val += arr_2d[i][j]

# print(sum_val)


# 정답 코드 - 내가 푼 방법과 조금 다름! 정답 코드 방법이 더 나을 듯!

# 2차원 배열을 구현해 각 줄마다 정수를 입력받습니다.
arr_2d = [
	list(map(int, input().split()))
	for _ in range(4)
]
sum_val = 0
	
# 색칠된 칸에 있는 원소들의 합을 구합니다.
for i in range(4):
	for j in range(i + 1):
		sum_val += arr_2d[i][j]

# 출력
print(sum_val)