a_arr = input().split()
b_arr = input().split()

a_age, a_sex = int(a_arr[0]), a_arr[1]
b_age, b_sex = int(b_arr[0]), b_arr[1]

if a_age >= 19 and a_sex == 'M' or b_age >= 19 and b_sex == 'M':
    print(1)
else:
    print(0)