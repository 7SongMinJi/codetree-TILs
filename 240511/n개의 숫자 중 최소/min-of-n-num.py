# 주어진 숫자들 중 최솟값 구하기

# 최솟값: min_val라는 변수를 사용하여 구함
# 지금까지 구한 최솟값인 min_val라는 값보다 현재 값인 elem이 더 작은 경우, 최솟값을 갱신함

# 최댓값 구하는 것과 마찬가지로...

# # 방법 1. min_val = sys.maxsize로 초기화한 뒤 시작
# import sys
# arr = [11, 15, 12, 15, 13, 19]
# min_val = sys.maxsize
# for elem in arr:
#     if min_val > elem:
#         min_val = elem
# print(min_val)

# # 방법 2. 첫 번째 원소를 min_val의 초기값으로 설정하고, 원소 비교는 두 번째 원소부터 진행!
# # *** 두 번째 원소부터 비교를 진행하기 위해서는 arr[1:]로 비교해야할 원소들을 재정의 해주기! ***
# arr = [11, 15, 12, 15, 13, 19]
# min_val = arr[0]
# for elem in arr[1:]:
#     if min_val > elem:
#         min_val = elem
# print(min_val)

# # 방법 3. 파이썬 - min() 함수 이용
# arr = [11, 15, 12, 15, 13, 19]
# print(min(arr))


# 문제
n = int(input())
arr = list(map(int, input().split()))
cnt = 1

min_val = arr[0]

for elem in arr[1:]:
    if min_val > elem:
        min_val = elem
        cnt = 1
    elif min_val == elem:
        cnt += 1
print(min_val, cnt)

# // 아! 처음에 틀렸는데 그 이유가 arr 첫 번째 요소를 min으로 설정했으니까 비교는 두 번째 원소부터 해야하자나!