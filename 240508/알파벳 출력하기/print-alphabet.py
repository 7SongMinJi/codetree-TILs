n = int(input())

cnt = 'A'

for i in range(1, n + 1):
    for j in range(i):
        print(cnt, end="")
        cnt = chr(ord(cnt) + 1)
        if cnt == chr(ord('Z') + 1):
            cnt = 'A'
    print()