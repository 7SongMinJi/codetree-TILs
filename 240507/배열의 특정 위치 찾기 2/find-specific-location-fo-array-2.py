arr = list(map(int, input().split()))
n = len(arr)
sum_odd, sum_even = 0, 0

for i in range(1, n + 1, 2):
    sum_odd += arr[i]

for i in range(0, n, 2):
    sum_even += arr[i]

if sum_even >= sum_odd:
    print(sum_even - sum_odd)
else:
    print(sum_odd - sum_even)