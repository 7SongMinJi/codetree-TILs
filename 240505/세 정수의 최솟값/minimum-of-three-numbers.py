arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

# min = a
# if b < min:
#     min = b
#     if c < min:
#         min = c
# elif c < min:
#     min = c

# 그냥 이렇게 하자
min_val = a

if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
    
print(min_val)