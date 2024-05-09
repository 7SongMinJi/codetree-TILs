# # n개의 숫자 입력받기

# # 1. 파이썬에서는 한 줄을 한 번에 받아야 함 -> 기존에 입력 받던 방식대로 split하여 arr에 저장
# n = int(input())
# arr = list(map(int, input().split()))
# sum_val = 0
# for i in range(n):
#     sum_val += arr[i]
# # for elem in arr:
# #     sum_val += elem
# print(sum_val)

# # 2. sum() 함수: 리스트 안의 원소의 합 계산 가능
# n = int(input())
# arr = list(map(int, input().split()))
# sum_val = sum(arr)
# print(sum_val)

# # 3. slicing() 함수 + sum() 함수: 두 번째 원소부터 끝 원소까지의 합 계산 가능
# n = int(input())
# arr = list(map(int, input().split()))
# sum_val = sum(arr[1:])
# print(sum_val)


# 문제
n = int(input())
score = list(map(float, input().split()))
avg_score = sum(score) / n

print(f"{avg_score:.1f}")

if avg_score >= 4.0:
    print("Perfect")
elif avg_score >= 3.0:
    print("Good")
else:
    print("Poor")