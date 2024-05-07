# # 행에 대하여 대칭인 경우

# # 바깥 for문 - 크게크게 몇 줄~
# # 안쪽 for문 - 각 행에 대해 출력되어야 하는 코드

# for i in range(3):
#     for j in range(3 - i):
#         print("*", end="")
#     print()

# # for i in range(2):
# #     for j in range(i + 2):
# #         print("*", end="")
# #     print()
# # // 이건 내가 써본 거고 아래 걸 참고하면 될 듯!

# # 4번째, 5번째 행 = 2번째, 1번째 행과 동일
# # => i값이 1->0 순서로 감소하는 코드를 작성해주면 됨
# # 그러면 i에 대한 for문만 수정해주면, j에 대한 코드를 고칠 필요가 없어짐
# for i in range(1, -1, -1):
#     for j in range(3 - i):
#         print("*", end="")
#     print()

# # 합치면
# for i in range(3):
#     for j in range(3 - i):
#         print("*", end="")
#     print()
# for i in range(1, -1, -1):
#     for j in range(3 - i):
#         print("*", end="")
#     print()

# Side Note
# 만약 j가 i에 따라 몇 번 돌아야 하는지 안 보인다면, *** 출력할 *의 개수를 나타내는 cnt 변수***를 이용할 수 있음!

# 아래처럼 코드를 적어도 됨! *****
# cnt = 3
# for i in range(5): # 5줄
#     for j in range(cnt): # 한 줄당 3개
#         print("*", end="")
#     print()

#     if i < 2:
#         cnt -= 1
#     else:
#         cnt += 1

# i = 0 3개
# i = 1 2개
# i = 2 1개
# i = 3 2개
# i = 4 3개


# 문제
n = int(input())

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        print("*", end=" ")
    print()