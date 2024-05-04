# 특정 문자를 사이에 두고 2개의 값을 입력

# 파이썬 split() 함수: 공백(default)을 사이에 두고 문자열을 잘라줌

# 만약 공백이 아닌 특정 문자를 기준으로 문자열을 잘라주고 싶다면, split 함수 안에 해당 문자를 적어주기

# a = input()
# print(a.split(":"))


# 문제
time = input().split(":")

h = int(time[0])
m = int(time[1])

print(f"{h + 1}:{m}")