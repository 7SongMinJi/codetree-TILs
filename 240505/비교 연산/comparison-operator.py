# # 비교 연산자와 조건

# # 비교 연산자는 식이 옳은지 틀린지에 따라 True(참) 또는 False(거짓)을 반환함
# print(1 > 2)
# print(1 < 2)

# if 1 > 2:
#     코드1
# if 1 < 2:
#     코드2


# 문제

arr = input().split()

a = int(arr[0])
b = int(arr[1])

print(int(a >= b))
print(int(a > b))

print(int(a <= b))
print(int(a < b))

print(int(a == b))
print(int(a != b))