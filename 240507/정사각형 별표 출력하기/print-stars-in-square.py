# # 이중 for문

# for _ in range(3):
#     for _ in range(5):
#         print(1, end="")
#     print()

# # 바깥 for문(i)은 행(세로줄 방향)에 관여 & 안쪽 for문(j)은 열(가로줄 방향)에 관여함
# # 주로 2중 for문을 사용하게 되는 경우 변수를 i, j 이렇게 2개를 사용함


# 문제
n = int(input())

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()