# # if문 안의 for문

# # 들여쓰기 조심!

# if n % 2 == 0:
#     for i in range(a, b + 1):
#         print(i)

# a, b = 3, 5
# n = int(input())

# if n % 2 == 0:
#     for i in range(a, b + 1):
#         print(i)
# print("Done")


# 문제
arr = input().split()
x = arr[0]
n = int(arr[1])

if x == 'A':
    for i in range(1, n + 1):
        print(i, end=" ")
elif x == 'D':
    for i in range(n, 0, -1):
        print(i, end=" ")