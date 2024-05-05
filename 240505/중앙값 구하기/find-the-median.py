arr = input().split()

a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

mid_val = a
if (b > a and b < c or b > c and b < a):
    mid_val = b
elif (c > a and c < b or c > b and c < a):
    mid_val = c

print(mid_val)

# 아래는 정답 코드
# # 변수 선언 및 입력
# inp = input()
# arr = inp.split()
# a = int(arr[0])
# b = int(arr[1])
# c = int(arr[2])

# # 출력
# if a > b:
#     if c > a:
#         # a > b, c > a 일때 (c > a > b)
#         print(a)
#     # a > b, a > c 일때 (a가 가장 크고, b와 c중 더 큰 수가 중앙값)
#     elif b > c:
#         print(b)
#     else:
#         print(c)
# else:
#     if c > b:
#         # b > a, c > b 일때 (c > b > a)
#         print(b)
#     # b > a, b > c 일때 (b가 가장 크고, a와 c중 더 큰 수가 중앙값)
#     elif a > c:
#         print(a)
#     else:
#         print(c)