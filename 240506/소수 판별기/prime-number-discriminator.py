# 소수: 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수

n = int(input())
bool_val = True

for i in range(2, n):
    if n % i == 0:
        bool_val = False

if bool_val == True:
    print("P")
else:
    print("C")