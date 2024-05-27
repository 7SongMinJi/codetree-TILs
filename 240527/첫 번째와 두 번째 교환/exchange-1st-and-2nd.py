# given_str = input()
# given_arr = list(given_str)

# first_chr, second_chr = given_str[0], given_str[1]

# for elem in given_arr:
#     if elem == first_chr:
#         elem = second_chr
#     elif elem == second_chr:
#         elem = first_chr

# given_str = ''.join(given_arr)

# print(given_str)

# # 처음에 틀림. 그 이유는
# # for loop 돌 때 elem로 접근하면 값 변경이 안 됨 *****
# # 그래서 list의 값을 변경하고자 한다면 index로 접근해야 함 *****

given_str = input()
given_arr = list(given_str)

first_chr, second_chr = given_str[0], given_str[1]

for i in range(len(given_arr)):
    if given_arr[i] == first_chr:
        given_arr[i] = second_chr
    elif given_arr[i] == second_chr:
        given_arr[i] = first_chr

given_str = ''.join(given_arr)

print(given_str)