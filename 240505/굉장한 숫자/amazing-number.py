# # and와 or 혼합

# # 나: if a % 2 == 0 or (a % 2 != 0 and a > 10)

# # 아래와 같이 소괄호를 사용해 우선순위를 강제!
# if a % 2 == 0 or (a % 2 == 1 and a >= 10)

# # ??? 10보다 크면 = 10 이상 ??? 아니지 않나

# a = int(input())

# if a % 2 == 0 or (a % 2 == 1 and a >= 10):
#     print("special")
# else:
#     print("normal")

# # and와 or 연산자의 우선순위 ***
# # and는 or보다 연산자 우선순위가 높음!! 먼저 식을 계산하게 됨 *** and > or

# a = int(input())
# if a % 2 == 0 and a % 5 == 0 or a % 7 == 0:
#     print("special")
# else:
#     print("normal")


# 문제
n = int(input())

# print(n % 2 == 1 and n % 3 == 0 or n % 2 == 0 and a % 5 == 0) # 앗 이렇게 하면 true가 아닌 True로 출력돼서 틀린 거임 주의하기!!

if n % 2 == 1 and n % 3 == 0 or n % 2 == 0 and n % 5 == 0:
    print('true')
else:
    print('false')