# for i in range(3):
#     string_value = input()
#     string_len = len(string_value)
#     if i == 0:
#         max_len = string_len
#         min_len = string_len
#     else:
#         if max_len < string_len:
#             max_len = string_len
#         if min_len > string_len:
#             min_len = string_len

# print(max_len - min_len)


# 정답 코드 - 아하 맞다 파이썬에서 max() min() 함수 쓰면 됐구나...
# max([len1, len2, len3]) min([len1, len2, len3]) 이렇게 값 넣어주면 되나봐

# 문자열을 입력받습니다.
str1 = input()
str2 = input()
str3 = input()
	
# 문자열의 길이를 구합니다.
len1 = len(str1)
len2 = len(str2)
len3 = len(str3)
	
# 세 문자열 중 가장 긴 길이와 가장 짧은 길이를 구합니다.
mx = max([len1, len2, len3])
mn = min([len1, len2, len3])

# 문제에서 구하고자 하는 값을 출력합니다.
print(mx - mn)