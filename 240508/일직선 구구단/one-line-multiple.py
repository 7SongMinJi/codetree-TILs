# # 둘둘단을 한 줄에 하나씩 출력

# for i in range(1, 3):
#     for j in range(1, 3):
#         print(f"{i} * {j} = {i * j}")


# 문제
n = int(input())

for i in range(n):
    for j in range(n):
        print(f"{i + 1} * {j + 1} = {(i + 1) * (j + 1)}")