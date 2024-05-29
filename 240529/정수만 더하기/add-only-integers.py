A = input()

sum = 0

for elem in A:
    if elem.isdigit() == True:
        sum += int(elem)

print(sum)

# // 문자열 속에 있는 숫자는 int가 아님!! int()로 감싸주어야 더할 수 있음 ***