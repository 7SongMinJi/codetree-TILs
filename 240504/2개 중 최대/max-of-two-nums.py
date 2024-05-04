# 삼항 연산자 - if else로만 이루어진 구문일 때 사용 가능

# if 조건:
#     a = v1
# else:
#     a = v2

# => a = v1 if 조건 else v2

# a = int(input())
# b = 50 if a > 10 else 3
# print(b)

# n = 8
# a = 2 + 6 + 5 if n > 10 else 6
# print(a)
# # *** 이 경우 답은 14가 아닌 6!! 난 14라 생각했음ㅠ***
# # 2 + 6 + 5 부분이 하나로 묶여서 처리됨!!! 오호
# # 오히려 나의 생각대로 하려면 뒷부분을 괄호로 묶어줘야 함
# a = 2 + 6 + (5 if n > 10 else 6)


# 문제
arr = input().split()

a = int(arr[0])
b = int(arr[1])

print(a if a >= b else b)