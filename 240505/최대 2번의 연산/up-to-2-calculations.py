# # if if 2번 이상 사용 = 서로 관련 없음

# if 조건1:
#     코드1
# if 조건2:
#     코드2
# 코드3

# # 위의 경우에서 조건1 참 & 조건2 참 -> 코드1, 코드2, 코드3 수행
# # 조건1 참 & 조건2 거짓 -> 코드1, 코드3 수행

# a = int(input())
# if a % 2 == 0:
#     print("even")
# if a >= 5:
#     print("normal")
# print("done")


# 문제
a = int(input())
if a % 2 == 0:
    a /= 2
if a % 2 != 0:
    a = (a + 1) / 2
print(int(a))