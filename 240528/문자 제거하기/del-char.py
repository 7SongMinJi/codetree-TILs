# string = input()
# arr = list(string)

# while True:
#     x = int(input())
#     if len(arr) <= x:
#         arr.pop(len(arr) - 1)
#     else:
#         arr.pop(x)
#     print(''.join(arr))
#     if len(arr) == 1:
#         break

# # // 처음에 틀렸는데 그 이유가 string 문자열일 경우 pop 할 수 없기 때문 ***
# # 그래서 string을 list로 바꾼 다음 pop해줘야 함!! ***


# 정답 코드 - 아하 그냥 while의 조건을 leng > 1로 해도 되겠구나?!

# 문자열을 입력받습니다.
string = input()

# 문자열의 길이를 구합니다.
leng = len(string)

# pop 함수를 사용하기 위해 문자열을 list로 전환합니다.
arr = list(string)

# 문자가 하나 남을 때까지 반복합니다.
while leng > 1:
	# 정수를 입력받습니다.
	a = int(input())
		
	# 정수가 문자열의 길이 이상이면 마지막 문자를 가리키게 변경합니다.
	if a >= leng:
		a = leng - 1
		
	# a번 자리의 원소를 제거합니다.
	arr.pop(a)
	leng -= 1
	
	# list를 문자열로 변환합니다.
	string = ''.join(arr)
	
	# 현재 문자열을 출력합니다.
	print(string)