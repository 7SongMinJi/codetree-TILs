arr = input().split()

a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

mid_val = a
if (b > a and b < c or b > c and b < a):
    mid_val = b
elif (c > a and c < b or c > b and c < a):
    mid_val = c

print(mid_val)