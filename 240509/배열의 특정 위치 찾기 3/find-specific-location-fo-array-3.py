# # 마지막 원소

# # 리스트 arr의 마지막 원소의 값 구하기: 리스트의 길이를 구해주는 len() 함수 활용
# arr = [1, 2, 3, 5]
# n = len(arr)
# print(arr[n - 1])

# 근데!!! 파이썬에서는 음수 index를 지원함!
# arr[-1]: 끝에서부터 첫 번째 원소
# arr[-2]: 끝에서부터 두 번째 원소
# arr = list(map(int, input().split()))
# print(arr[-1] + arr[-2])


# # 문제

# arr = list(map(int, input().split()))

# i = 0

# while (arr[i] != 0):
#     i += 1
    
# print(arr[i - 3] + arr[i - 2] + arr[i - 1])


# # 정답 코드

# # 배열에 주어진 수를 입력받아 저장합니다.
# arr = list(map(int, input().split()))

# # 0이 저장되어있는 인덱스를 찾습니다.
# for i in range(100):
# 	if arr[i] == 0:
# 		k = i
# 		break
		
# # 출력
# print(arr[k - 3] + arr[k - 2] + arr[k - 1])


# 다시 풀기
arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        break
print(arr[i - 3] + arr[i - 2] + arr[i - 1])