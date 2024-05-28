# # 문자열 내 문자 제거

# # 방법 1: 문자열 s ('baknana')의 3번째 원소를 제거하는 코드
# # 지워져야 할 문자의 양쪽 문자열들만 slicing을 통해 살려두는 식으로 구현 가능
# s = 'baknana'
# s = s[:2] + s[3:]
# print(s)
# # >> banana

# # 방법 2: 문자열을 list로 변환한 뒤, pop 함수를 이용해 해당 문자를 제거하고 다시 문자열로 변환하기
# # pop(i) 함수: list에서의 pop(i) 함수는 i번째 index를 지워주는 함수
# s = 'baknana'
# arr = list(s)
# arr.pop(2)
# arr = ''.join(arr)
# print(s)


# 문제

given_str = input()

given_str = given_str[:1] + given_str[2:-2] + given_str[-1:]

print(given_str)