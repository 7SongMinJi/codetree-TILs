# # 새로운 2차원 배열 선언과 활용

# # 전부 0으로 초기화된 2차원 배열 만들기

# # List Comprehension을 이용하면 n * n 크기의, 전부 0으로 채워진 2차원 배열을 선언할 수 있음
# n = 4
# arr_2d = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]
# print(arr_2d)
# # 출력 결과 [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# # 만약 n * m 크기의 격자라면 다음과 같이 초기화 가능. 단, List Comprehension 사용시 n, m 위치에 유의할 것!!! *****
# n, m = 4, 5
# arr_2d = [
#     [0 for _ in range(m)]
#     for _ in range(n)
# ]
# print(arr_2d)
# # 출력 결과 [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# # 2차원 배열 출력시 중첩 반복문을 활용하여 range 함수를 사용할 수 있음
# n = 4
# arr_2d = [[1, 2, 3, 4], [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]
# for i in range(n):
#     for j in range(n):
#         print(arr_2d[i][j], end=" ")
#     print()

# # range 없이 리스트 내 각 원소를 접근하는 식으로 표현 가능
# # 2차원 배열의 원소는 각 행이 되며, 각 행에 있는 원소들을 조회하며 값을 출력해주는 식으로 진행이 됨 *****
# n = 4
# arr_2d = [[1, 2, 3, 4], [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]
# for row in arr_2d:
#     for elem in row:
#         print(elem, end=" ")
#     print()

# # 2차원 배열과 규칙
# # n * n 크기의 격자에 특정 규칙에 맞춰 숫자를 출력하는 문제
# n = 3
# arr_2d = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]
# num = 1
# for i in range(n):
#     for j in range(n):
#         arr_2d[i][j] = num
#         num += 2
# # 출력
# for row in arr_2d:
#     for elem in row:
#         print(elem, end=" ")
#     print()


# 문제
n, m = map(int, input().split())
# n, m = tuple(list(map(int, input().split())))
# n, m = arr[0], arr[1]

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 1
for i in range(n):
    for j in range(m):
        arr_2d[i][j] = num
        num += 1

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()

# # GPT 코드
# n, m = map(int, input().split())
# arr = [[0] * m for _ in range(n)]

# num = 1
# for i in range(n):
#     for j in range(m):
#         arr[i][j] = num
#         num += 1

# for row in arr:
#     print(' '.join(map(str, row)))