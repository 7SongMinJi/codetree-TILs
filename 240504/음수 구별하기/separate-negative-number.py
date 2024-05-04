# 조건문

# if 조건문 - if문 뒤에는 반드시 : 를 적어줘야만 함!

# if 조건:
#         조건이 참일 경우 수행되는 코드

# if 조건문의 내부 범위 파악은 들여쓰기(indentation) 단위로!!!
# 들여쓰기는 보통 공백 4칸(tab)으로 함!

# a = int(input())

# if a > 10:
#     a += 5
#     print(a)
#     a -= 6

# print(a)

# 50 입력
# 55
# 49 출력

# => 파이썬에서 가장 중요한 건 들여쓰기!! 같은 위계에 놓인 코드끼리 서로 다른 indent를 갖게 된다면 에러 발생함

# print(1)
#     print(2)
#         print(3)
# # 에러 발생!

# 조건문에 사용되는 비교 연산자

# >, >=, <, <=, ==, !=

# ==의 경우, 값 뿐만 아니라 type도 일치해야 함
# => 1 == '1'은 false

# # 홀/짝 판단
# a = int(input())

# if a % 2 == 0:
#     print("even")

# # 배수(multiple) 판단
# a = int(input())

# if a % 5 == 0:
#     print("multiple of 5")


# 문제
a = int(input())

print(a)

if a < 0:
    print("minus")