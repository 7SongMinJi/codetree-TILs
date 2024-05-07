# 행에 따라 패턴이 다른 이유

# 단순히! 홀수번째/짝수번째 행에 대해 for loop 따로 돌리면 됨!

# for i in range(4):
#     if i % 2 == 0:
#         for j in range(3):
#             print(j + 1, end="")
#         print()
#     else:
#         for j in range(3):
#             print(3 - j, end="")
#         print()


# 문제
n = int(input())

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            print(j + 1, end="")
        print()
    else:
        for j in range(n):
            print(n - j, end="")
        print()