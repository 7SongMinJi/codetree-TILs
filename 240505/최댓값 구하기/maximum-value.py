arr = input().split()

a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

max_val = a

if b > max_val:
    max_val = b
if c > max_val:
    max_val = c

print(max_val)