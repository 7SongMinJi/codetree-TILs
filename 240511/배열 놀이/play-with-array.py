n, q = tuple(list(map(int, input().split())))
arr = list(map(int, input().split())) # n개의 원소를 arr에 저장
# print(arr)

# q개의 질의가 한 줄에 하나씩 주어짐
for i in range(q):
    arr2 = list(map(int, input().split()))
    if arr2[0] == 1:
        print(arr[arr2[1] - 1])
    elif arr2[0] == 2:
        if arr.count(arr2[1]) == 0:
            print(0)
        else:
            for j in range(n):
                if arr[j] == arr2[1]:
                    print(j + 1)
                    break
    elif arr2[0] == 3:
        for j in range(arr2[1] - 1, arr2[2]):
            print(arr[j], end=" ")
        print()