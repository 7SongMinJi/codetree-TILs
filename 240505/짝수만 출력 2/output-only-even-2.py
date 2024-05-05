arr = input().split()

b = int(arr[0])
a = int(arr[1])

i = b
while i >= a:
    print(i, end=" ")
    i -= 2