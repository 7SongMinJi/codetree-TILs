str1 = input()
str2 = input()

str1_num = []
str2_num = []

for elem in str1:
    if elem.isdigit() == True:
        str1_num.append(elem)
    else:
        continue

for elem in str2:
    if elem.isdigit() == True:
        str2_num.append(elem)
    else:
        continue

str1_num = int(''.join(str1_num))
str2_num = int(''.join(str2_num))

print(str1_num + str2_num)