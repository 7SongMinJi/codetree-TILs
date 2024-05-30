# a, b = input().split()
# a_digit, b_digit = [], []
# for elem in a:
#     if elem.isdigit() == True:
#         a_digit.append(elem)
#     else:
#         break

# for elem in b:
#     if elem.isdigit() == True:
#         b_digit.append(elem)
#     else:
#         break

# print(int("".join(a_digit)) + int("".join(b_digit)))

# // 처음엔 계속 틀림. isdigit()을 digit()이라 씀 & string일 경우엔 append() 사용 불가능. list일 때만 가능!