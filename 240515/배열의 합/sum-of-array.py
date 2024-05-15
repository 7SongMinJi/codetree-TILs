# # 2차원 배열

# # n개의 줄에 걸쳐 각 n개의 숫자를 공백을 사이에 두고 입력 받기

# # 지금까지 배웠던 거로는
# n = 4
# for _ in range(n):
#     arr = list(map(int, input().split()))
#     sum_val = sum(arr)
#     print(sum_val)
# # // 행 단위로 합을 구할 수 있지만, 열 단위로 구해야 하면 2차원 격자에 담아야 함 = 2차원 배열

# # 2차원 배열: 리스트(각 행)를 각 원소로 갖는 리스트
# n = 4
# arr_2d = []
# for _ in range(n):
#     arr_1d = list(map(int, input().split()))
#     arr_2d.append(arr_1d)
# print(arr_2d)

# # ***** 어떤 배열을 정의하고 for loop 안에 append만 사용하는 경우 => List Comprehension 이용 가능 *****
# n = 4
# arr_2d = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]
# print(arr_2d)

# # 2차원 배열에서 원소에 접근: arr_2d[i][j] 같은 형태로! arr_2d[i][j]: i+1행, j+1열을 의미
# arr_2d = [[1, 2, 3, 4], [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]
# print(arr_2d[0][0]) # 1행 1열 = 1
# print(arr_2d[1][2]) # 2행 3열 = 9

# # 2차원 배열 특정 위치의 원소 값 바꾸기: 1차원 배열에서와 마찬가지로 = 연산을 이용하여 표현 가능
# arr_2d = [[1, 2, 3, 4], [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]
# print(arr_2d[0][0]) # 1행 1열 = 1
# arr_2d[0][0] = 15
# print(arr_2d[0][0]) # 1행 1열 = 15

# # 1차원 배열에서 len() 함수 -> 리스트 내의 원소의 개수 반환
# arr = [1, 2, 3, 4, 5]
# print(len(arr)) # 원소의 개수 5 반환

# # 2차원 배열에서 len() 함수 -> 2차 격자를 표현한 배열 내의 행 수 반환
# arr_2d = [[1, 2, 3, 4], [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]
# print(len(arr_2d)) # 행의 개수 4 반환


# 문제
arr_2d = [list(map(int, input().split())) for _ in range(4)]
for i in range(len(arr_2d)):
    print(sum(arr_2d[i]))