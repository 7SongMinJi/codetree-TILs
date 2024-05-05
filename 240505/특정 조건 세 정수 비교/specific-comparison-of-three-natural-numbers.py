arr = input().split()

a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

# min은 내장함수 이름이라 변수 이름으로 사용하지 않는 것을 권장!! ***
# min_val = a
# if b < min_val:
#     min_val = b
#     if c < min_val:
#         min_val = c
# elif c < min_val:
#     min_val = c

min_val = a

if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
    
print(int(a == min_val), end=" ")
print(int(a == b and b == c))