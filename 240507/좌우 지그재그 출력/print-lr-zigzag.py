n = int(input())

# for i in range(n):
#     for j in range(n):
#         if i % 2 == 0:
#             print(i * n + cnt, end=" ")
#             cnt += 1
#         else:
#             print(n * (i + 1) - cnt, end=" ")
#             cnt -= 1
#     print()

# 틀렸고 다시

for i in range(n):
    if i % 2 == 0:
        cnt = 1 + i * n
        for j in range(n):
            print(cnt, end=" ")
            cnt += 1
    else:
        cnt = n * (i + 1)
        for j in range(n):
            print(cnt, end=" ")
            cnt -= 1
    print()