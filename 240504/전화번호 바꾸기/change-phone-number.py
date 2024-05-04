phone_num = input().split("-")

front = phone_num[1]
back = phone_num[2]

# print(010, back, front, sep="-")
# 위에서처럼 하면 오류임!! 왜냐하면 파이썬3에서는 0으로 시작하는 숫자 처리 X
# 그래서 010을 써주려면 문자열로 취급해줘야 함! "010" ***

print("010", back, front, sep="-")