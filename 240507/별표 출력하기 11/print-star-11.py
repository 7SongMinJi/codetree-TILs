# # 행, 열에 대한 규칙이 있는 경우

# for i in range(5):
#     for j in range(5):
#         if i == 0 or i == 4 or j == 0 or j == 4:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# 문제
n = int(input())

for i in range(n * 2 + 1):
    for j in range(n * 2 + 1):
        if i % 2 == 0:
            print("*", end=" ")
        else:
            if j % 2 == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()