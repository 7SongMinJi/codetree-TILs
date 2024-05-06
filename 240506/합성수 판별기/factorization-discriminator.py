# 합성수: 정수 n이 2 이상 (n - 1) 이하의 어떤 정수로 나누어 떨어지는 경우

n = int(input())

bool_val = False

for i in range(2, n):
    if n % i == 0:
        bool_val = True

if bool_val == True:
    print("C")
else:
    print("N")

# 나 자꾸만 ==을 =으로 씀! 이런 거 실수하지 말자!!