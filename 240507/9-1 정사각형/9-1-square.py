n = int(input())

cnt = 9

for i in range(4):
    for j in range(4):
        print(cnt, end="")
        cnt -= 1
        if cnt == 0:
            cnt = 9
    print()