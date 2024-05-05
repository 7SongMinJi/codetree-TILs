# for문 안의 if문

# 반복문을 돌며 특정 조건을 만족할 때만 코드를 수행하도록 함

# for i in range(a, b + 1):
#     if i % 2 == 0:
#         print(1)
#     else:
#         print(0)

# a, b = 3, 5
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         print(1)
#     else:
#         print(0)
# print("Done")


# 문제
n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0 or i % 3 == 0:
        print(1, end=" ")
    else:
        print(0, end=" ")