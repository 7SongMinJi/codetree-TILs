A = input()
B = input()
minN = -1
cnt = 0

while A != B:
    A = A[-1] + A[:-1]
    cnt += 1
    if cnt > len(A):
        minN = -1
        break
    minN = cnt

print(minN)