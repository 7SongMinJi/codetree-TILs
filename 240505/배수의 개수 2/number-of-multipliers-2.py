# # 조건을 만족하는 개수 세기

# # cnt 변수 활용! 초기값 cnt = 0으로 설정하고 진행 ***
# cnt = 0
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         cnt += 1
# print(cnt)

# a, b = 3, 8
# cnt = 0
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         cnt += 1
# print(cnt)

# # 처음 cnt 변수 초기화는 for문 바깥에! print는 for문 끝나고 한 번!
# for i in range(10):
#     n = int(input())
#     print(n, end=" ")


# 문제
cnt = 0
for i in range(10):
    n = int(input())
    if n % 2 == 1:
        cnt += 1
print(cnt)