# 주어진 숫자들 중 최댓값 구하기

# 최댓값: max_val라는 변수 사용하기!
# 만약 지금까지 구한 최댓값인 max_val이라는 값보다 현재 값인 elem이 더 큰 경우, 최댓값을 갱신해주기
# arr = [1, 5, 2, 5, 3, 9]
# max_val = 0
# for elem in arr:
#     if elem > max_val:
#         max_val = elem
# print(max_val)

# BUT 만약 주어진 원소들이 모두 음수라면, 예상과는 다르게 최댓값이 0으로 구해지게 됨
# 왜냐하면 초기값이 0으로 세팅되어있어 의도와는 달리 갱신이 전혀 일어나지 않기 때문

# # 해결책 1. 파이썬 -sys.maxsize 이용: 주어지는 숫자들 값보다 더 작은 숫자를 초기값으로 설정 가능
# # sys.maxsize: 파이썬에서 사용 가능한 가장 큰 정수!!
# # 그러니까 -sys.maxsize를 초기값으로 설정하면 당연히 그보다 더 큰 값이 나올 수밖에 없음!
# # import sys 해줘야 되나봄!
# import sys
# arr = [-1, -5, -2, -5, -3, -9]
# max_val = -sys.maxsize
# for elem in arr:
#     if elem > max_val:
#         max_val = elem
# print(max_val)

# # 해결책 2. max_val의 초기값을 첫 번째 원소로 하고, 원소 비교는 두 번째 원소부터 진행
# # *** 두 번째 원소부터 비교를 진행하기 위해서 arr[1:]로 비교해야 할 원소들을 재정의해주기!! ***
# arr = [-1, -5, -2, -5, -3, -9]
# max_val = arr[0]
# for elem in arr[1:]:
#     if elem > max_val:
#         max_val = elem
# print(max_val)

# # 해결책 3. 파이썬 max() 함수 이용: arr의 가장 큰 값 반환하나봐! min(arr)도 존재
# arr = [-1, -5, -2, -5, -3, -9]
# print(max(arr))


# 문제
arr = list(map(int, input().split()))
max_val = arr[0]
for elem in arr[1:]:
    if elem > max_val:
        max_val = elem
print(max_val)