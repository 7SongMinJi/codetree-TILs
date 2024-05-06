# # 반복문에서의 break

# # break: for, while에서만 사용 가능
# # if 조건: break - 해당 조건이 만족하는 경우 *** 가장 가까이에 있는 *** for loop을 완전히 탈출함
# # break는 조건문과 같이 쓰여야 함!!

# for i in range(6, 101):
#     코드1
#     if i % 5 == 0:
#         코드2
#         break
#     코드3
# 코드4
# # i가 6, 7, 8, 9인 경우 코드1, 코드3 수행되다가
# # i가 10이 되는 순간 코드1, 코드2 수행 & for loop 탈출 -> 코드4 수행

# a, b = 3, 101
# prod = 1
# for i in range(a, b + 1):
#     print(f"current val is {i}")
#     if i % 5 == 0:
#         print("val is multiple of 5")
#         break
#     print("val is not a multiple of 5")
#     prod *= i
# print(prod)


# 문제
n = int(input())

sum_val = 0

for i in range(1, 101):
    sum_val += i
    if sum_val >= n:
        print(i)
        break