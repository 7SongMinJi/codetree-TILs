# cnt = 0

# while True:
#     n = int(input())
#     if n % 2 == 0:
#         if cnt == 3:
#             break
#         print(n // 2)
#         cnt += 1

# # 위와 같이 코드를 작성하면 출력 결과는 잘 나오지만 EOFError 런타임 에러가 뜸
# # 그 이유는 EOFError - 더 이상 받을 입력이 없음에도 input을 시도할 때 발생


# cnt = 0

# while True:
#     try:
#         n = int(input())
#         if n % 2 == 0:
#             if cnt == 3:
#                 break
#             print(n // 2)
#             cnt += 1
#     except EOFError:
#         break



# # 정답 코드
# # 변수 선언 및 입력
cnt = 0
	
while True:
	# 변수 선언 및 입력
	n = int(input())
	
	# n이 홀수라면 아무 작업도 하지 않고, n이 짝수라면 n/2를 출력하는 작업을 3번 한 뒤 종료합니다.
    # 
	if n % 2 == 1:
		continue
		
	print(n // 2)
	cnt += 1
		
	if cnt >= 3:
		break