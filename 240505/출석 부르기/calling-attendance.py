# # if elif elif else 조건문

# # elif는 여러 번 사용 가능

# if 조건1:
#     코드1
# elif 조건2:
#     코드2
# elif 조건3:
#     코드3
# else:
#     코드4
# 코드5

# # 조건1 거짓 & 조건2 거짓 & 조건3 참 -> 코드3, 코드5 수행

# a = int(input())
# if a >= 10:
#     print("A")
# elif a >= 8:
#     print("B")
# elif a >= 6:
#     print("C")
# else:
#     print("D")
# print("E")


# 문제
num = int(input())
if num == 1:
    print("John")
elif num == 2:
    print("Tom")
elif num == 3:
    print("Paul")
else:
    print("Vacancy")