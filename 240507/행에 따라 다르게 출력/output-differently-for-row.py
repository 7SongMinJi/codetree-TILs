# n = int(input())

# cnt = 1

# for i in range(n):
#     if i % 2 == 0:
#         for j in range(n):
#             print(cnt, end=" ")
#             cnt += 1
#     else:
#         for j in range(n):
#             cnt += 1
#             print(cnt, end=" ")
#             cnt += 1
#     print()


# # 정답 코드

# # 변수 선언 및 입력
n = int(input())
cnt = 0
	
# 값을 조건대로 증가시켜 출력합니다.
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            cnt += 1
        else:
            cnt += 2
        print(cnt, end=" ")
    print()