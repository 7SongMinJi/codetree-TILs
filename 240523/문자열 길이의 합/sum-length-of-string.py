n = int(input())

arr_2d = [
    input()
    for _ in range(n)
]

string_len, cnt_a = 0, 0
for i in range(n):
    string_len += len(arr_2d[i])
    if 'a' == arr_2d[i][0]:
        cnt_a += 1

print(string_len, cnt_a)