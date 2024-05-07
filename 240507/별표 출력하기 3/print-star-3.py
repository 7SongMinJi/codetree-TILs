# 앞에 공백이 붇는 경우

# 앞에 공백이 출력되어야 하는 문제의 경우에는,
# 행이 증가함에 따라 공백의 개수가 어떻게 변하는지 파악하여
# 별을 출력하기 이전에 공백을 해당 개수만큼 출력해줘야만 함
# 뒤에 있는 공백은 굳이 출력해주지 않아도 됨!!
# 별의 개수에 대한 식을 쉽게 구하기 위해서는 행이 1 증가함에 따라 변화하는 별의 개수에 집중하면 됨

# vv*
# v***
# *****

# for i in range(3):
#     for j in range(2 - i):
#         print(" ", end="")
#     for k in range(i * 2 + 1):
#         print("*", end="")
#     print()


# 문제
n = int(input())

for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()