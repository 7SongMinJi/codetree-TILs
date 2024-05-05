# # or 기호

# # 2개 이상의 조건들 중 하나라도 만족하는지 확인하려면 or 기호 사용!
# if 조건1 or 조건2:
#     코드1

# a = int(input())
# if a % 2 == 0 or a > 10:
#     print("special")
# else:
#     print("normal")

# # and와 마찬가지로 or 여러 개 사용해서 3개 이상의 조건 표현 가능!
# if 조건1 or 조건2 or 조건3:
#     코드1


# 문제
a = int(input())

if a < 10 or a > 20:
    print("yes")
else:
    print("no")