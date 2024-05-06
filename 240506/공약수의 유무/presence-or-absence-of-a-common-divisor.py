# 범위 내 존재 여부 = Bool 함수 이용!!!

arr = input().split()

a, b = int(arr[0]), int(arr[1])

bool_val = False

for i in range(a, b + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        bool_val = True

if bool_val == True:
    print(1)
else:
    print(0)