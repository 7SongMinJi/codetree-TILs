# 10번째 피보나치 수 구하기

# 피보나치 수열: 첫 번째 원소가 1, 두 번째 원소가 1, 세 번째 원소부터는 해당 원소의 값이 바로 직전 두 원소의 합과 동일한 수열
# 1, 1, 2, 3, 5, 8, 13, ...

# # ***** arr[-1]: 맨 뒤 원소 & arr[-2]: 전전 원소 활용!!
# arr = [0, 1, 1]
# # 세 번째 항부터 10번째 항까지 추가
# for i in range(3, 11):
#     arr.append(arr[-1] + arr[-2])
# # 10번째 항 출력
# print(arr[10])

# # 또는 다음과 같이 미리 10번째 항까지의 값을 담을 배열을 만들어 놓고 답을 구하기
# # *** 총 0을 11개를 적어야, 1번째 항부터 10번째 항까지를 올바로 나타낼 수 있음 ***
# arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# arr[1] = arr[2] = 1
# # 세 번째 항부터 10번째 항까지 추가
# for i in range(3, 11):
#     arr[i] = arr[i - 1] + arr[i - 2]
# # 10번째 항 출력
# print(arr[10])

# # *** 피보나치 문제의 경우 배열을 사용하지 않고도 구할 수 있음
# # 그 전전항을 pp, 전 항을 p라 했을 때 현재 항은 pp + p
# pp, p = 1, 1
# for _ in range(3, 11):
#     pp, p = p, pp + p
# print(p)


# 문제

# arr = list(map(int, input().split()))
# for i in range(2, 10):
#     arr[i] = (arr[i - 2] + arr[i - 1]) % 10
# for elem in arr:
#     print(elem, end=" ")
# 위처럼 코드 짜면 list index out of range라 뜸
# 미리 만들어 놓지 않은 이상 이렇게 하면 안 됨

# # 1. 미리 만들어 놓고 값 바꾸기
# arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# arr[0], arr[1] = tuple(list(map(int, input().split())))

# for i in range(2, 10):
#     arr[i] = (arr[i - 2] + arr[i - 1]) % 10

# for elem in arr:
#     print(elem, end=" ")

# 2. append 이용하기
arr = list(map(int, input().split()))

for i in range(8):
    arr.append((arr[-2] + arr[-1]) % 10)

for elem in arr:
    print(elem, end=" ")