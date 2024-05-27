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

# given_str = input()
# given_arr = list(given_str)

# first_chr, second_chr = given_str[0], given_str[1]

# for i in range(len(given_arr)):
#     if given_arr[i] == first_chr:
#         given_arr[i] = second_chr
#     elif given_arr[i] == second_chr:
#         given_arr[i] = first_chr

# given_str = ''.join(given_arr)

# print(given_str)


# 정답 코드 - 오 이 방법도 괜찮겠다 [:i] 기준으로 slicing *****

# 문자열을 입력받습니다.
string = input()
	
# 문자열의 첫 번째 문자와 두 번째 문자를 저장합니다.
a = string[0]
b = string[1]
	
# 문자열을 순회하면서 첫 번째 문자와 두 번째 문자를 교환합니다.
for i in range(len(string)):
	if string[i] == a:
		string = string[:i] + b + string[i + 1:]
	elif string[i] == b:
		string = string[:i] + a + string[i + 1:]
	
# 교환된 이후의 문자열을 출력합니다.
print(string)