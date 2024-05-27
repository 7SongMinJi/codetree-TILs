# # 문자열 내 문자 수정

# # 문자열 s ('baaana')의 3번째 원소를 n으로 바꿔보는 코드 작성하기
# s = 'baaana'
# s[2] = 'n'
# print(s)
# # BUT 에러 발생!!!
# # TypeError: 'str' object does not support item assignment

# # Python에서 문자열은 immutable(불변), 즉 변할 수 없는 타입이기 때문에 *** 내부 문자를 절대 변경할 수 없음 ***

# # 문자열 내 문자 수정 방법 1: 아예 새로운 문자열을 만들어 주는 것
# # 문자열 역시 리스트와 마찬가지로 부분 문자열을 뽑아내는 것이 slicing을 통해 가능
# # 바뀌어야 하는 문자 양옆으로 slicing을 적용하여 해당 문자를 제외하고는 그대로 유지가 되도록 새로운 문자열을 만들어주는 방식
# s = 'baaana'
# s = s[:2] + 'n' + s[3:]
# print(s)
# # >> banana

# # 문자열 내 문자 수정 방법 2: 각 문자를 원소로 갖는 리스트로 변환하여 해결
# # BUT 이 방법은 매우 복잡해서 이해 안 가면 그냥 넘어가도 됨

# # ***** 문자열을 list()라는 함수로 감싸면, 각 문자를 원소로 갖는 리스트가 만들어짐 *****
# s = 'baaana'
# arr = list(s)
# print(arr)
# # >> ['b', 'a', 'a', 'a', 'n', 'a']

# # 이 경우 각각이 리스트 내 원소이기 때문에, 세 번째 원소를 'n'으로 바꾸는 것이 가능해짐
# s = 'baaana'
# arr = list(s)
# print(arr)
# arr[2] = 'n'
# print(arr)
# # >>['b', 'a', 'a', 'a', 'n', 'a']
#     ['b', 'a', 'n', 'a', 'n', 'a']

# # 문자들로만 이루어진 리스트는 join() 함수를 이용하여 다시 문자열로 합칠 수 있음!! *****
# # list(), joint() 함수를 이용하여 세 번째 문자를 'n'으로 바꾸는 게 가능!
# s = 'baaana'
# arr = list(s)
# arr[2] = 'n'
# s = ''.join(arr)
# print(s)
# # >> 'banana'


# 문제

given_str = input()

given_str = given_str[:1] + 'a' + given_str[2:-2] + 'a' + given_str[-1:]

print(given_str)