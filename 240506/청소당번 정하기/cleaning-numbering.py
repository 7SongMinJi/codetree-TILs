n = int(input())

cnt_a, cnt_b, cnt_c = 0, 0, 0

for i in range(1, n + 1):
    if i % 12 == 0:
        cnt_c += 1
    elif i % 3 == 0:
        cnt_b += 1
    elif i % 2 == 0:
        cnt_a += 1

print(cnt_a, cnt_b, cnt_c)