# # <두 변수 값을 교환>

# # 1. temp 이용
# a, b = 5, 3

# temp = a
# a = b
# b = temp

# print(f"A is {a} B is {b}")

# # 2. , 를 이용하여 바로 교환하기
# a, b = 5, 3

# a, b = b, a

# print(f"A is {a} B is {b}")


# 문제
a, b = 3, 5
a, b = b, a

print(f"{a}\n{b}")