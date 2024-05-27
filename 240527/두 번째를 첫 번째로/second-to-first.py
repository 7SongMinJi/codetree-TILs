given_str = input()
given_arr = list(given_str)

first_chr, second_chr = given_str[0], given_str[1]

for i in range(len(given_arr)):
    if given_arr[i] == second_chr:
        given_arr[i] = first_chr

given_str = ''.join(given_arr)

print(given_str)