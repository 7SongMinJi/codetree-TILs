# # 직각삼각형

# # 바깥 for문 = 행에 연관, 안쪽 for문 = 열에 연관 (각각의 행에 출력되는 것에 대해)

# for i in range(4):
#     for j in range(i + 1):
#         print("*", end="")
#     print()

# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()

# # //for문을 사용할 때는 0, 1 중 원하는 값에서부터 시작하면 됨! 더 익숙한 방식 택하면 됨


# 문제
n = int(input())

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# # 정답 코드

# # 변수 선언 및 입력
# n = int(input())

# # 길이가 n인 직각삼각형을 출력합니다.
# for i in range(n):
# 	for _ in range(n-i):
# 		print("*", end=" ")
# 	print()