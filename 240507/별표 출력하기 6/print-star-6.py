# # 모양의 규칙을 찾는 법

# # 지금까지 배운 대로라면, i에 따라 출력해야 하는 별의 개수가 어떻게 바뀌는지 알아내야 함
# # 이를 쉽게 계산하는 방법은!! *** 행이 1 증가함에 따라 변화하는 별의 개수에 집중하기 ***

# # 다음 행에 3 증가 -> i * 3
# # i에 0을 넣었을 때 * 1개 -> + 1

# for i in range(3):
#     for j in range(3 * i  + 1):
#         print("*", end="")
#     print()


# 문제
n = int(input())

for i in range(n):
    for _ in range(i):
        print(" ", end=" ")
    for _ in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()

for i in range(n - 2, -1, -1):
    for _ in range(i):
        print(" ", end=" ")
    for _ in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()