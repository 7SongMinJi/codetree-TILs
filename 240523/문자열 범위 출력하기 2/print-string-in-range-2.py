given_str = input()
x = int(input())
cnt = 0
for elem in given_str[::-1]:
    print(elem, end="")
    cnt += 1
    if cnt == x:
        break