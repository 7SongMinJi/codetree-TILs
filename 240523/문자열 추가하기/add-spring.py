# # 문자열 Concat

# # 문자열 붙이기

# # 두 문자열 a, b끼리 붙일 수 있는 방법
# # python - 문자열끼리 + 연산이 가능! 두 문자열을 붙여주는 역할을 함
# a, b = "apple", "banana"
# print(a + b)
# # >> applebanana

# # 두 문자열을 더한 결과를 다시 변수에 저장하는 것도 가능!
# a, b = "apple", "banana"
# a = a + b
# print(a)
# # >> applebanana

# # 만약 3개의 문자열을 더해야 하는 경우, 아예 새로운 문자열을 선언하여 초기 문자열을 빈 문자열인 ""로 선언하고 다 더해주는 식으로 진행
# a, b, c = "apple", "banana", "candy"
# tot_str=""
# tot_str += a
# tot_str += b
# tot_str += c
# print(tot_str)
# # >> applebananacandy

# # 리스트를 이용하면 더 간결하게 해결 가능 ***** [a, b, c]
# a, b, c = "apple", "banana", "candy"
# tot_str=""
# for target_str in [a, b, c]:
#     tot_str += target_str
# print(tot_str)
# # >> applebananacandy

# # join() 함수를 이용하면 여러 문자열을 하나로 합치는 과정을 더 쉽게 구현 가능
# # join 함수: 각 원소들을 특정 구분값(sep)을 기준으로 합쳐주는 함수
# sep.join(리스트)

# ','.join(['1', '2', '3']) # '1, 2, 3'
# ':'.join(['11', '22', '33']) # '11:22:33'
# ''.join(['a', 'b', 'c']) # 'abc'

# # 3개의 문자열을 합치는 코드
# a, b, c = "apple", "banana", "candy"
# tot_str = "".join([a, b, c])
# print(tot_str)
# # >> applebananacandy


# 문제

given_str = input()

print(given_str + "Hello")