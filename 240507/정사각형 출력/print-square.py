# # cnt를 이용하여 숫자 모양 채우기

# # cnt라는 변수를 이용!
# # i, j에 대한 규칙이 아닌, for loop이 진행됨에 따라 cnt 값을 계속 1씩 증가시킴

# # *****
# cnt = 1
# for i in range(2):
#     for j in range(4):
#         print(cnt, end="")
#         cnt += 1
#     print()


# 문제
n = int(input())
cnt = 1

for i in range(n):
    for j in range(n):
        print(cnt, end=" ")
        cnt += 1
    print()