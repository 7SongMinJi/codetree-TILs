arr = input().split()

mid, final = int(arr[0]), int(arr[1])

if mid < 90 or final < 90:
    print(0)
elif final >= 95:
    print(100000)
elif final >= 90:
    print(50000)