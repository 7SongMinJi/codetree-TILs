arr = input().split()
str, q = arr[0], int(arr[1])

for _ in range(q):
    x = int(input())
    if x == 1:
        str = str[1:] + str[0]
    elif x == 2:
        str = str[-1] + str[:-1]
    elif x == 3:
        # str = str[len(str)-1:-1:-1] 처음에 이렇게 썼는데 틀림...
        str = str[::-1]
    print(str)

# // str 거꾸로: str[::-1]