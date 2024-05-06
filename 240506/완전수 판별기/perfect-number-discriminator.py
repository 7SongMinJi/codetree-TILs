# *** 완전수란, 자기 자신을 제외한 약수의 합이 자신이 되는 수 ***
# 6 28 496 5128

n = int(input())

sum_val = 0

for i in range(1, n):
    if n % i == 0:
        sum_val += i

if sum_val == n:
    print("P")
else:
    print("N")