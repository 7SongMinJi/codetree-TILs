n = int(input())

tot_str = ""

arr = [
    input()
    for _ in range(n)
]

for elem in arr:
    tot_str += elem

print(tot_str)