n = int(input())

cnt = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(2 * cnt, end=" ")
        cnt += 1
        if cnt == 5:
            cnt = 1
    print()