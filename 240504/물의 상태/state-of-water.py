# # if elif else 조건문

# # 상단 if 조건에 해당하지 않으면서 elif 조건에 해당한다면 특정 코드 수행하도록 함

# if 조건1:
#     코드1
# elif 조건2:
#     코드2
# else:
#     코드3
# 코드4
# # 조건1 참 -> 코드1, 코드4 수행
# # 조건1 거짓 & 조건2 참 -> 코드2, 코드4 수행
# # 조건1 거짓 & 조건2 거짓 -> 코드3, 코드4 수행

# a = int(input())
# if a >= 10:
#     print("A")
# elif a >= 5:
#     print("B")
# else:
#     print("C")
# print("E")

# # if, elif만 사용하고 else 굳이 쓰지 않아도 괜찮음!

# if 조건1:
#     코드1
# elif 조건2:
#     코드2
# 코드4

# a = int(input())
# if a >= 10:
#     print("A")
# elif a >= 5:
#     print("B")
# print("E")

# # 만약 if, if, elif를 사용하게 되면 if / if-elif 이렇게 쌍을 이루어 구분됨 (첫 번째 if문은 독립적인 것)

# if 조건1:
#     코드1

# if 조건2:
#     코드2
# elif 조건3:
#     코드3
# 코드4

# a = int(input())
# if a >= 10:
#     print("A")
# if a >= 15:
#     print("B")
# elif a >= 5:
#     print("C")
# print("E")

# # Side Note
# a = int(input())
# if a > 15:
#     print("A")
# elif a >= 10:
#     pass # pass라는 걸 꼭 써줘야 하나봐!! ***
# else:
#     print("B")
# print("Done")


# 문제
temp = int(input())

if temp < 0:
    print("ice")
elif temp >= 100:
    print("vapor")
else:
    print("water")