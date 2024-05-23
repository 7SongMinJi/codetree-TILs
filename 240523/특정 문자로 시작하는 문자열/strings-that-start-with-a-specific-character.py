n = int(input())

arr_2d = [
    input()
    for _ in range(n)
]

x = input()
cnt, str_len = 0, 0

for elem in arr_2d:
    if elem[0] == x:
        cnt += 1
        str_len += len(elem)

print(f"{cnt} {str_len / cnt:.2f}")