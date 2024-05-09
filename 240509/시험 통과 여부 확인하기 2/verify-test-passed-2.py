n = int(input())
cnt = 0

for i in range(n):
    score = list(map(int, input().split()))
    sum_score = 0
    for elem in score:
        sum_score += elem
    if sum_score / 4 >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)