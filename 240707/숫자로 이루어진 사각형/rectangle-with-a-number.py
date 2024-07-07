# 숫자로 이루어진 사각형

n = int(input())

def print_square(n):
    cnt = 1
    for _ in range(n):
        for _ in range(n):
            print(cnt, end=" ")
            cnt += 1
            if cnt > 9:
                cnt = 1
        print("")

print_square(n)


# 해설