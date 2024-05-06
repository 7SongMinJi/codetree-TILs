# # 무한 루프: 특정 조건을 만족하기 전까지는 절대 빠져나올 수 없는 loop

# # while True라는 조건, 특정 조건 만족시 탈출 가능하도록 하는 break 이용
# # 입력을 몇 번 받아야 하는지 알 수 없을 때!!! *** -> while문을 이용한 무한 루프를 만들자!

# while True:
#     n = int(input())
#     if n >= 10:
#         코드1
#         break
#     코드2
# 코드3
# # n이 10보다 작은 경우 계속 코드2 실행 & 입력 새로 받음
# # 최초로 10 이상의 값이 입력으로 들어오면 코드1 수행 & 반복문 탈출 & 코드3 수행


# sum_val = 0
# while True:
#     n = int(input())
#     print(f"current val is {n}")
#     if n > 10:
#         print("val is greater than or equal to 10")
#         break
#     print("val is smaller than 10")
#     sum_val += n
# print(sum_val)


# 문제
while True:
    n = int(input())
    if n == 0:
        break
    print(n)