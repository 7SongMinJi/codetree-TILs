# # 사칙연산

# # 덧셈 + 뺄셈 - 곱셈 *

# # 나눗셈: 몫 // 나머지 % 정확한 나누기 실수 값 /

# # 지수승: **

# a, b = 9, 4
# print(a + b, a * b, a - b, a // b, a % b, a / b, a ** b) # 13 36 5 2 1 2.25 9^4

# # 나눗셈 / 의 경우 나눈 결과가 정수 값으로 딱 떨어져도 결과는 실수 형태로 나옴!
# # 만약 정수 결과를 얻고 싶다면 int()를 이용하기

# a = 3 / 3 # 실제 값은 1이지만 1.0으로 출력됨
# print(a)
# print(int(a))

# # 사칙연산 계산시 type은 더 큰 범위를 따라가게 되어있음
# # => 정수와 실수가 만나면 type은 실수가 됨

# a = 1 + 3.0
# print(a)
# a = 3 / 3
# b = 4
# print(a + b) # a = 1.0, b = 4니까 5.0 출력됨!


# 문제
arr = input().split()
a = int(arr[0])
b = int(arr[1])

print(a + b)
print(a - b)
print(a // b)
print(a % b)