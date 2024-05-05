# # and 기호

# # 2개 이상의 조건을 동시에 만족하는지 확인하려면 and 기호 사용
# if 조건1 and 조건2:
#     코드1

# a = int(input())
# if a % 2 == 0 and a >= 10:
#     print("special")
# else:
#     print("normal")

# # 3개의 조건을 만족시키는지에 대한 여부도 and 2개 사용해서 표현 가능. 그 이상도 가능
# if 조건1 and 조건2 and 조건3:
#     코드1


# 문제
a_score = input().split()
b_score = input().split()
a_math, a_eng = int(a_score[0]), int(a_score[1])
b_math, b_eng = int(b_score[0]), int(b_score[1])

if a_math > b_math and a_eng > b_eng:
    print(1)
else:
    print(0)