a_score = input().split()
b_score = input().split()

a_math = int(a_score[0])
a_eng = int(a_score[1])

b_math = int(b_score[0])
b_eng = int(b_score[1])

if a_math > b_math:
    print('A')
elif a_math < b_math:
    print('B')
else:
    if a_eng > b_eng:
        print('A')
    else:
        print('B')