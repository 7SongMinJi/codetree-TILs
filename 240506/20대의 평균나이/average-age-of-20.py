sum_val, cnt = 0, 0

while True:
    n = int(input())
    if n < 20 or n >= 30:
        break
    sum_val += n
    cnt += 1

print(f"{sum_val / cnt:.2f}")