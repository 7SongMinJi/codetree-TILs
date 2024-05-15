# arr_2d = [list(map(int, input().split())) for _ in range(4)]

# for i in range(len(arr_2d)):
#     print(f"{sum(arr_2d[i]) / len(arr_2d[i])}:.1f)", end=" ")
# print()

# for i in range(len(arr_2d[0])):
#     sum_val = 0
#     for j in range(len(arr_2d)):
#         sum_val += arr_2d[j][i]
#     print(f"{sum_val / len(arr_2d)}:.1f", end=" ")
# print()

# sum_val = 0
# for i in range(len(arr_2d)):
#     for j in range(len(arr_2d[i])):
#         sum_val += arr_2d[i][j]
# print(f"{sum_val / (len(arr_2d) * len(arr_2d[0]))}:1f")

array = [list(map(int, input().split())) for _ in range(2)]

row_avg = [sum(row) / 4 for row in array]
col_avg = [sum(array[row][col] for row in range(2)) / 2 for col in range(4)]
total_avg = sum(sum(row) for row in array) / 8

print(" ".join(f"{avg:.1f}" for avg in row_avg))
print(" ".join(f"{avg:.1f}" for avg in col_avg))
print(f"{total_avg:.1f}")