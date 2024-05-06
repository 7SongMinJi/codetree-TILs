# # 조건을 만족하는 합 구하기

# # sum_val 변수 0으로 초기화한 뒤 이용!

# n = 6
# sum_val = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         sum_val += i
# print(sum_val)

# # 파이썬 - snake case: 변수명을 적을 때 단어와 단어 사이에 _ (underscore)를 넣어 표현하는 것 (가독성)


# 문제
arr = input().split()
a = int(arr[0])
b = int(arr[1])

sum_val = 0

for i in range(a, b + 1):
    sum_val += i

print(sum_val)