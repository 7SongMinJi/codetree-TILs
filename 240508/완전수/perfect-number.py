# 완전수: 자기 자신을 제외한 약수의 합이 자기 자신과 같은 수

arr = input().split()

start, end = int(arr[0]), int(arr[1])
cnt = 0

for i in range(start, end + 1):
    sum_val = 0
    for j in range(1, i):
        if i % j == 0:
            sum_val += j
    if i == sum_val:
        cnt += 1

print(cnt)