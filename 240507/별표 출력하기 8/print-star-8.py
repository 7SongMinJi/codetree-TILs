# 행에 따라 모양이 다른 경우

# for i in range(6):
#     if i % 2 == 0:
#         for _ in range(i + 1):
#             print("*", end="")
#         print()
#     else:
#         print("$")

# 위와 같이 i가 짝수인지 홀수인지에 따라 출력하는 모양을 바꿔주면 해결 가능!


# 문제
n = int(input())

for i in range(n):
    if i % 2 == 0:
        print("*")
    else:
        for _ in range(i + 1):
            print("*", end=" ")
        print()


# # 정답 코드

# # 변수 선언 및 입력
# n = int(input())

# #i가 짝수인 경우 별을 1개, 홀수인 경우 i+1개를 출력합니다
# for i in range(n):
# 	if i % 2 == 0:
# 		print("*", end="")
# 	else:
# 		for _ in range(i + 1):
# 			print("*", end=" ")
# 	print()