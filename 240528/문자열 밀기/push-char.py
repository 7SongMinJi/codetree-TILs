# # 문자열 밀기

# # 문자열 s ('baaana')를 우측으로 한 칸 밀어주는 코드 작성하기
# # 단, 이때 가장 우측에 있던 문자는 가장 왼쪽으로 밀려와야 함

# # 가장 끝에 있는 문자를 떼어 맨 앞으로 보내고, 첫 번째 문자부터 마지막으로부터 두 번째 문자까지 해당하는 부분문자열을 뒤에 붙이면 됨 *****
# s = 'baaana'
# s = s[-1] + s[:-1]
# print(s)
# # >> abaaan


# 문제

given_str = input()

given_str = given_str[1:] + given_str[0]

print(given_str)