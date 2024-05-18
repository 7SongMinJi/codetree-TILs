# n, m = map(int, input().split())

# arr_2d = [
#     [0] * m
#     for _ in range(n)
# ]

# i, j, cnt = 0, 0, 1

# while 0 <= i <= n-1 and 0 <= j <= m-1:
#     arr_2d[i][j] = cnt
#     cnt += 1
#     if i < j:
#         i += 1
#         j -= 1
#     elif i >= j and j != 0:
#         i -= 1
#         j += 1
#     else:
#         j = i + 1
#         i = 0

# for row in arr_2d:
#     for elem in row:
#         print(elem, end=" ")
#     print()

# [i][j]
# [0][0]

# [0][1]
# [1][0]

# [0][2]
# [1][1]
# [2][0]

# [0][3]
# [1][2]
# [2][1]
# [3][0]

# // 결국 못 품... 정답 코드를 보자


# 정답 방법 1: 
# 정답 방법 2: 


# 정답 코드 1

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
answer = [
    [0 for _ in range(m)]
    for _ in range(n)
]
count = 1

        
# Step 1:
for start_col in range(m):
    curr_row = 0
    curr_col = start_col

    while 0 <= curr_col and curr_row < n:
        answer[curr_row][curr_col] = count
        
        # 변수 업데이트
        curr_row += 1
        curr_col -= 1
        count += 1

# Step 2:
for start_row in range(1, n):
    curr_row = start_row
    curr_col = m - 1

    while 0 <= curr_col and curr_row < n:
        answer[curr_row][curr_col] = count
        
        # 변수 업데이트
        curr_row += 1
        curr_col -= 1
        count += 1

# 출력:
for row in range(n):
    for col in range(m):
        print(answer[row][col], end = ' ')
    print()


# # 정답 코드 2

# # 변수 선언 및 입력
# n, m = tuple(map(int, input().split()))
# answer = [
#     [0 for _ in range(m)]
#     for _ in range(n)
# ]
# count = 1
        
# # Step 1:
# for start_col in range(m):
#     curr_row = 0
#     curr_col = start_col

#     while 0 <= curr_col and curr_row < n:
#         answer[curr_row][curr_col] = count
        
#         # 변수 업데이트
#         curr_row += 1
#         curr_col -= 1
#         count += 1

# # Step 2:
# for start_row in range(1, n):
#     curr_row = start_row
#     curr_col = m - 1

#     while 0 <= curr_col and curr_row < n:
#         answer[curr_row][curr_col] = count
        
#         # 변수 업데이트
#         curr_row += 1
#         curr_col -= 1
#         count += 1

# # 출력:
# for row in range(n):
#     for col in range(m):
#         print(answer[row][col], end = ' ')
#     print()