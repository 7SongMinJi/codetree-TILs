a, b = tuple(list(map(int, input().split())))

count_arr = [0] * b

while a > 1:
    count_arr[a % b] += 1
    a //= b

count_arr = [i ** 2 for i in count_arr]
print(sum(count_arr))