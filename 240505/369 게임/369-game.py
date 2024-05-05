# n = int(input())

# for i in range(1, n + 1):
#     if i % 3 == 0 or (i // 10 == 3 or i // 10 == 6 or i // 10 == 9 or (i % 10) // 1 == 3 or (i % 10) // 1 == 6 or (i % 10) // 1 == 9):
#         print(0, end=" ")
#     else:
#         print(i, end=" ")


# 정답 코드
# 변수 선언, 입력
n = int(input())

# 출력
for i in range(1, n+1):
	if i % 3 == 0:
		print("0", end=" ")
	elif i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
		print("0", end=" ")
	elif i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
		print("0", end=" ")
	else:
		print(i, end=" ")


# 아 그냥 i % 10 하면 일의 자리 수 나오는 거지!...
# i가 3, 6, 9 중 하나를 포함하는 수는 i를 10으로 나누었을 때 나머지 또는 몫이 3, 6, 9일 때.