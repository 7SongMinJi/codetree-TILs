arr_2d = [
    input()
    for _ in range(10)
]

x = input()
cnt = 0

for i in range(10):
    string_len = len(arr_2d[i])
    if arr_2d[i][string_len - 1] == x:
        print(arr_2d[i])
        cnt += 1

if cnt == 0:
    print("None")