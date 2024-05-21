# # 문자열 리스트 관리

# # 문자열들의 목록을 관리하기 위해서는, 각 문자열들을 원소로 갖는 리스트를 정의하면 됨

# # 하나의 문자열의 쓰임은 마치 1차원 배열과 같고,
# # 문자열 리스트의 경우에는 마치 2차원 배열과 같이 동작함

# arr = ["banana", "apple", "pizza"]

# print(arr[0]) # 첫 번째 문자열 banana 출력
# print(len(arr[0])) # 첫 번째 문자열의 길이 6 출력

# print(arr[0][0]) # b <- 첫 번째 문자열의 첫 번째 문자 출력
# print(arr[0][1]) # a <- 첫 번째 문자열의 두 번째 문자 출력
# print(arr[0][2]) # n <- 첫 번째 문자열의 세 번째 문자 출력


# 문제

arr = ["apple", "banana", "grape", "blueberry", "orange"]

x = input()
cnt = 0

for i in range(5):
    if arr[i][2] == x or arr[i][3] == x:
        print(arr[i])
        cnt += 1

print(cnt)