n = int(input())

sum = 0

for _ in range(n):
    sum += int(input())

sum = str(sum)

print(sum[1:] + sum[0])