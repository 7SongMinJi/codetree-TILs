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


# # 문제

# given_str = input()
# given_str = given_str[:1] + given_str[2:-2] + given_str[-1:]
# print(given_str)

# # // 내 방식대로 하면 실행 시간 엄청 오래 걸림


# 정답 코드

# 문자열을 입력받습니다.
string = input()

# 문자열의 길이를 구합니다.
leng = len(string)

# pop 함수를 사용하기 위해 문자열을 list로 전환합니다.
arr = list(string)
	
# 앞에서 2번째 원소를 제거합니다. (이때 문자열의 길이가 1 감소하는것을 반드시 기억합니다 *****)
arr.pop(1)
leng -= 1 # *****
	
# 뒤에서 2번째 원소를 제거합니다.
arr.pop(leng - 2)
leng -= 1 # *****

# list를 문자열로 변환합니다.
string = ''.join(arr)
	
# 앞에서 2번째, 뒤에서 2번째 원소가 제거된 문자열을 출력합니다.
print(string)