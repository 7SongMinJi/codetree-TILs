n = int(input())

arr = input().split()
tot_str = ""
cnt = 0

for elem in arr:
    tot_str += elem

for i in range(len(tot_str)):
    print(tot_str[i], end="")
    if (i + 1) % 5 == 0:
        print()