arr_2d = [input().split() for _ in range(5)]

for i in range(len(arr_2d)):
    for j in range(len(arr_2d[i])):
        print(chr(ord(arr_2d[i][j]) + ord('A') - ord('a')), end=" ")
    print()