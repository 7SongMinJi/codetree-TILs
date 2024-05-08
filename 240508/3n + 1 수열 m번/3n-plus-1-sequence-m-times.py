n = int(input())

for _ in range(n):
    x = int(input())
    cnt = 0
    while True:
        if x == 1:
            break
        if x % 2 == 0:
            x //= 2
        else:
            x = x * 3 + 1
        cnt += 1
    print(cnt)