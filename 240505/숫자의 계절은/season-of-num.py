# if 조건 나열 순서의 중요성

# a = 5
# if a % 2 == 0:
#     print('C')
# elif a >= 5:
#     print('B')
# else:
#     print('A')

# 조건의 순서를 잘 배열하면 코드의 복잡도가 감소함!
# if-elif-else 잘 조합하여 활용하기


# 문제
month = int(input())

if month >= 3 and month <= 5:
    print("Spring")
elif month >= 6 and month <= 8:
    print("Summer")
elif month >= 9 and month <= 11:
    print("Fall")
else:
    print("Winter")