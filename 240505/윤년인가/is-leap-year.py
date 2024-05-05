# # 조건을 최대한 잘 묶기

# if a % 2 == 1:
#     if a >= 10:
#         print('A')
#     else:
#         print('B')
# else:
#     if a >= 15:
#         print('A')
#     else:
#         print('B')

# # 위의 식 대신 아래처럼 하면 코드의 복잡성이 감소함 -> if-elif-else 잘 활용하기
# a = 10
# if a % 2 == 1 and a >= 10 or a % 2 == 0 and a >= 15:
#     print('A')
# else:
#     print('B')


# 문제
y = int(input())
# if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
#     print('false')
# else:
#     print('true')

if y % 4 == 0 and not(y % 100 == 0 and y % 400 != 0):
    print('true')
else:
    print('false')


# # *** 파이썬에선 논리적 부정을 표현할  ! 대신 not을 사용함. 아래처럼!
# if not x > 10:
#     print("x는 10 이하입니다.")