# # 조건을 만족하는 곱 구하기

# # prod라는 변수를 활용하기! 초기화는 1로 해줄 것

# a, b = 3, 8
# prod = 1

# for i in range(a, b + 1):
#     if i % 2 == 0:
#         prod *= i

# print(prod)


# 문제
arr = input().split()

a, b = int(arr[0]), int(arr[1])
prod = 1

for i in range(a, b + 1):
    prod *= i

print(prod)