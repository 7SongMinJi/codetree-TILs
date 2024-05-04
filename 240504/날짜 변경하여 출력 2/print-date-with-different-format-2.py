# 특정 문자를 사이에 두고 3개 이상의 값을 입력

# 파이썬 split() 함수 - ("") 안의 문자를 기준으로 문자열을 잘라주는데
# 이때 리스트를 이루는 원소의 수가 3개 이상이더라도 그대로 작동함

# a = input()
# print(a.split("-"))


# 문제
date = input().split("-")

yyyy = int(date[2])
mm = int(date[0])
dd = int(date[1])

print(f"{yyyy}.{mm}.{dd}")