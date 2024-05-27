arr = input().split()
s, q = arr[0], int(arr[1])
s = list(s)

for _ in range(q):
    arr2 = input().split()
    x = int(arr2[0])
    if x == 1:
        a, b = int(arr2[1]), int(arr2[2])
        temp = s[a - 1]
        s[a - 1] = s[b - 1]
        s[b - 1] = temp
        print(''.join(s))
    elif x == 2:
        a, b = arr2[1], arr2[2]
        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
        print(''.join(s))