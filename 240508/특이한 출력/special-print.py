# # 조건에 맞게 띄워주기

# for i in range(1, 4):
#     for j in range(1, 4):
#         if i % 2 == 1:
#             print(f"({i}, {j})", end=" ")
#         else:
#             print(f"({i}, {j})")


# for i in range(1, 4): 
#     for j in range(1, 4):
#         if i % 2 == 0:
#             print(f"({i}, {j})", end="\n")
#         else:
#             print(f"({i}, {j})", end=" ")
    

# 문제
n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"({i}, {j})", end=" ")
        if (i + j) % 4 == 0:
            print()