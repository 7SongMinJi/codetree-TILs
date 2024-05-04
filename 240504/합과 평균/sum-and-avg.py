# # 합과 평균

# a, b = 9, 4
# print(a + b, (a + b) / 2)

# # 사칙연산 - 우리가 아는 우선순위에 따라 계산됨
# a, b = 9, 4
# print(a + b / 2) # b / 2 먼저 계산 = 2.0 따라서 11.0 출력됨
# # 따라서 괄호 잘 써주기!

# # list - sum() 함수와 len() 함수!! (내장함수)
# # sum(): list에 들어있는 원소 값들의 합
# # len(): list의 원소의 개수
# a, b, c, d = 9, 4, 5, 7

# arr = [a, b, c, d]

# print(sum(arr), sum(arr) / len(arr))


# 문제
arr = input().split()

a = int(arr[0])
b = int(arr[1])
print(f"{a + b} {(a + b) / 2:.1f}")
# 여러 표현 방법 알아두자!
# print("{} {:.1f}".format(a + b, (a + b) / 2))
# print("%d %.1f" % (a + b, (a + b) / 2))