# n = int(input())
# arr = list(map(int, input().split()))

# temp = -1
# max_val = arr[0]
# overlap = list()

# for i in range(1, n):
#     if max_val < arr[i] and arr[i] not in overlap:
#         temp, max_val = max_val, arr[i]
#     elif max_val == arr[i]:
#         max_val = temp
#         overlap.append(arr[i])

# if max_val > 0:
#     print(max_val)
# else:
#     print(-1)

# // 틀림.
# GPT 힌트 - 일단 먼저 개수를 세서 각 숫자가 몇 번 나왔는지 확인하기 - .count() 함수 이용!!!

n = int(input())
arr = list(map(int, input().split()))

duplicates=[]

for elem in arr:
    if arr.count(elem) > 1 and elem not in duplicates:
        duplicates.append(elem)

max_val = -1
for elem in arr:
    if max_val < elem and elem not in duplicates:
        max_val = elem

print(max_val)