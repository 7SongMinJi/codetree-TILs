arr = list(map(int, input().split()))

sum_even, sum_multiple_3, cnt = 0, 0, 0

for i in range(10):
    if (i + 1) % 2 == 0:
        sum_even += arr[i]
    if (i + 1) % 3 == 0:
        sum_multiple_3 += arr[i]
        cnt += 1

print(f"{sum_even} {sum_multiple_3 / cnt:.1f}")