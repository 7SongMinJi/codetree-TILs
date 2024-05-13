arr = list(map(int, input().split()))

maxUnder500, minOver500 = 0, 1001

for elem in arr:
    if maxUnder500 < elem and elem < 500:
        maxUnder500 = elem
    elif minOver500 > elem and elem > 500:
        minOver500 = elem

print(maxUnder500, minOver500)