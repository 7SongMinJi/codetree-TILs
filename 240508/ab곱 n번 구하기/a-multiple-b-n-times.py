# # n번 반복하는 경우

# # 한 쌍을 입력 받고, 그 사이의 합을 구하기
# arr = input().split()
# a, b = int(arr[0]), int(arr[1])
# sum_val = 0
# for i in range(a, b + 1):
#     sum_val += i
# print(sum_val)

# # 여러 쌍
# n = int(input())
# for _ in range(n):
#     arr = input().split()
#     a, b = int(arr[0]), int(arr[1])
#     sum_val = 0
#     for i in range(a, b + 1):
#         sum_val += i
#     print(sum_val)

# # 이렇게 서로 다른 케이스에 대해 계산이 필요한 경우에는 꼭 적절한 위치에서 sum_val 값을 0으로 초기화 해줘야 함!

# # 코드 어떻게 짜야 할 지 모르겠다면 위에서처럼 한 번에 대한 코드 먼저 짜고 for문 안에 넣기!! ***


# 문제
n = int(input())

for _ in range(n):
    arr = input().split()
    a, b = int(arr[0]), int(arr[1])

    prod = 1
    for i in range(a, b + 1):
        prod *= i
    print(prod)