# # 범위 내 숫자인지 판별하기

# # 2개 이상의 조건을 동시에 만족하는지 알고 싶은 경우 and 사용
# if 2 <= a and a <= 10:
#     코드1

# # 근데!! 파이썬에선 위의 식을 아래와 같이 한 번에 표현하는 것도 가능함!!
# if 2 <= a <= 10:
#     코드1
# # but 이건 다른 언어에서는 지원하지 않는 방식이므로 조건이 2개 이상이라면 그냥 and를 사용하여 2개로 나눠 작성하자

# a = int(input())
# if 2 <= a and a <= 10:
#     print("in range")
# else:
#     print("out of range")


# 문제
a = int(input())

if a >= 10 and a <= 20:
    print("yes")
else:
    print("no")