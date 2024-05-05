# # 중첩 조건문

# # 외부 조건문 / 내부 조건문의 구분은 들여쓰기(indent)로 판단!! 보통 공백 4칸 (tab)

# if a % 2 == 1:
#     if a >= 10:
#         print('A')
#     else:
#         print('B')
# else:
#     if a >= 15:
#         print('C')
#     else:
#         print('D')

# a = int(input())
# if a % 2 == 1:
#     if a >= 10:
#         print('A')
#     else:
#         print('B')
# else:
#     if a >= 15:
#         print('C')
#     else:
#         print('D')


# 문제
sex = int(input())
age = int(input())

if sex == 0:
    if age >= 19:
        print("MAN")
    else:
        print("BOY")
else:
    if age >= 19:
        print("WOMAN")
    else:
        print("GIRL")