# 숫자 규칙 찾기

# for i in range(2):
#     for j in range(4):
#         print((j + 1) * (i + 1), end="")
#     print()

# for i in range(1, 3):
#     for j in range(1, 5):
#         print(i * j, end="")
#     print()


# 문제
arr = input().split()

a, b = int(arr[0]), int(arr[1])

for i in range(1, a + 1):
    for j in range(1, b + 1):
        print(i * j, end=" ")
    print()