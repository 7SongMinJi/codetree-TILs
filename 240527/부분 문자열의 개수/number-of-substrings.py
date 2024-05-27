strA = input()
strB = input()

lenA = len(strA)
cnt = 0

for i in range(lenA - 1):
    if strA[i] == strB[0] and strA[i + 1] == strB[1]:
        cnt += 1
    
print(cnt)