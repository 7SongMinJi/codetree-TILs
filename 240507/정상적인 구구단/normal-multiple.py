# # 구구단 - 삼삼단

# # a * b = c의 형태에서 a는 행이 증가함에 따라 1씩 늘어나고 b는 열이 증가함에 따라 1씩 늘어남
# # 다만 ,의 경우 마지막 열을 제외한 경우에만 출력이 되어야 하므로, 다음과 같이 조건문을 이용하여 처리해야 함 ***

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} * {j} = {i * j}", end="")
#         if j < 3:
#             print(",", end = " ")
#     print()


# 문제
n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} * {j} = {i * j}", end="")
        if j < n:
            print(",", end=" ")
    print()