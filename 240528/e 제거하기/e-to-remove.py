string = input()

arr = list(string)

for i in range(len(arr)):
    if arr[i] == 'e':
        arr.pop(i)
        break

print(''.join(arr))


# 정답 코드