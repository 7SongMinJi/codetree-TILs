arr = input().split()
start, end = int(arr[0]), int(arr[1])
cnt = 0

for i in range(start, end + 1):
    cnt_j = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt_j += 1
    if cnt_j == 3:
        cnt += 1

print(cnt)