# # if else if else 2번 이상 사용 = 앞 if-else와 뒤 if-else는 관련 없음!

# if 조건1:
#     코드1-1
# else:
#     코드1-2
# if 조건2:
#     코드2-1
# else:
#     코드2-2
# 코드3

# # 위의 경우에서 조건1 참 & 조건2 참 -> 코드1-1, 코드2-1, 코드3 수행
# # 조건1 참 & 조건2 거짓 -> 코드1-1, 코드2-2, 코드3 수행

# a = int(input())
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")
# if a >= 5:
#     print("normal")
# else:
#     print("small")
# print("done")


# 문제
arr = input().split()

a = int(arr[0])
b = int(arr[1])

if a % 2 == 0:
    print("even")
else:
    print("odd")

if b % 2 == 0:
    print("even")
else:
    print("odd")