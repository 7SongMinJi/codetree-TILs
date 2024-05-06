while True:
    arr = input().split()
    width = int(arr[0])
    height = int(arr[1])
    x = arr[2]
    
    print(width * height)
    
    if x == 'C':
        break