arr = input().split()

a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
# a, b, c = int(arr[0], arr[1], arr[2]) #는 안 되나봐

print(a + b + c, int((a + b + c) / 3), sep="\n")