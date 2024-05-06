arr = list(map(int, input().split()))

i = 0

while (arr[i] != 0):
    i += 1
    
print(arr[i - 3] + arr[i - 2] + arr[i - 1])