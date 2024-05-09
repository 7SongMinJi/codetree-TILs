arr = list(map(int, input().split()))

sum_val, cnt = 0, 0

for elem in arr:
    if elem == 0:
        break
    if elem % 2 == 0:
        sum_val += elem
        cnt += 1

print(cnt, sum_val)