# # 특정 문자열 포함 여부

# # 문자열 s에 특정 문자열 'ab'가 포함되어 있는지의 여부를 알 수 있는 방법

# # 논리적으로 접근한다면, 각각의 위치에 대해 조사하며 그 중 정확히 'ab'와 일치하는 위치가 있었는지 확인해야 함
# # 이때 주의: for loop을 [0, length - 2]에서만 돌아야 함 ***
# s = 'applebanana'
# length = len(s)
# exists = False
# for i in range(length - 1):
#     if s[i] == 'a' and s[i + 1] == 'b':
#         exists = True
# print(exsits)

# # python: 문자열에 slicing을 이용하여 직접 문자열끼리 비교 가능
# s = 'applebanana'
# length = len(s)
# exists = False
# for i in range(length - 1):
#     if s[i:i + 2] == 'ab':
#         exists = True
# print(exists)

# # python: 키워드 in 제공
# s = 'applebanana'
# print('ab' in s)

# # 판단하고자 하는 부분 문자열이 'ab'와 같이 2자리가 아닌 input으로 주어졌을 때 이를 문자열 t라 하면
# # 해당 부분 문자열이 존재하는지 알 수 있는 방법
# # in 키워드를 사용하지 않고도 구현 가능
# # 문자열 t의 길이를 len_t라 했을 때, 결국 s[i]와 t[0] / s[i + 1]과 t[1] / s[i + 2]와 t[2] / ... / s[i + len_t - 1]과 t[len_t - 1]이 전부 일치해야 함
# # 이 역시도 boolean 값을 만들어 전부 일치하는지에 대한 여부 판단 가능
# # i 01234567891011
# s = 'applebanana'
# t = 'abbaba'
# n = len(s)
# exsits = False
# len_t = len(t)
# for i in range(n - len_t + 1):
#     all_same = True
#     for j in range(len_t):
#         if s[i + j] != t[j]:
#             all_same = False
#     # if s[i] == t[0] / s[i + 1] == t[1] / ...
#     # s[i + len_t - 1] == t[len_t - 1]
#     if all_same == True:
#         exists = True
# print(exists)


# 문제

given_str = input()

if 'ee' in given_str:
    print("Yes", end=" ")
else:
    print("No", end=" ")

if 'ab' in given_str:
    print("Yes")
else:
    print("No")