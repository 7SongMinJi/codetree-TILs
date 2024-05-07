# # 숫자 모양 출력

# for i in range(3):
#     for j in range(i + 1):
#         print(j + 1, end="")
#     print()


# 문제
n = int(input())

for i in range(n):
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()