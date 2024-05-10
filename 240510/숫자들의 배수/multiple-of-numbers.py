n = int(input())
arr = list()
cnt = 0

for i in range(1, 11):
    arr.append(n * i)
    if n * i % 5 == 0:
        cnt += 1
    if cnt == 2:
        break

for elem in arr:
    print(elem, end=" ")