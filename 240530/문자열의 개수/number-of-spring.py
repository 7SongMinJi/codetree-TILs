str = ""
str_list = []

while True:
    str = input()
    if str != "0":
        str_list.append(str)
    else:
        break

print(len(str_list))

for i in range(len(str_list)):
    if i % 2 == 0:
        print(str_list[i])