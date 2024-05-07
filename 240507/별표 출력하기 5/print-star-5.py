n = int(input())

for i in range(n):
    for j in range(n - i):
        for k in range(n - i):
            print("*", end="")
        print("", end=" ")
    print()


# 정답 코드

# 변수 선언 및 입력
n = int(input())

# i는 각 행마다 *을 몇 묶음씩 출력 할 것인지를 의미합니다.
for i in range(n, 0, -1):
    # j는 각 행마다 *묶음을 i번 출력하는 역할을 합니다.
    for _ in range(i):
        # k는 *묶음을 출력해주는 역할을 합니다.
        # *묶음은 항상 i개의 *로 이루어져 있습니다.
        for _ in range(i):
            print("*", end="")

        # *묶음을 만든 이후에는 꼭 공백을 띄워줘야 합니다.
        print(" ", end="")

    # 행마다 한 줄씩 띄워줍니다.
    print()