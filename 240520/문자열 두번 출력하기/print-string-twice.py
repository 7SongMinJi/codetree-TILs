# # 공백 없는 문자열 입력받아 출력하기

# # 공백이 들어 있지 않은 문자열의 경우에는, input() 함수 이용
# given_input = input()
# print(given_input)

# # 문자열은 마치 1차원 배열과 같음.
# # 첫 번째 문자를 참조하기 위해서는 0번지를, 두 번째 문자를 참조하기 위해서는 1번지를 참조해야 함
# given_input = "banana"
# print(given_input[0]) # b <- 문자열의 첫 번째 문자
# print(given_input[1]) # a <- 문자열의 두 번째 문자
# print(given_input[2]) # n <- 문자열의 세 번째 문자

# # 문자열의 경우에는 for loop 없이 print 함수만을 이용하여 문자열을 출력할 수 있음
# given_input = "banana"
# print(given_input)

# # 하지만 일반 리스트의 경우에는 다름
# # 리스트를 그대로 출력하면 리스트 type 형태로 나오게 되기 때문에 꼭 for loop을 이용해 각 원소를 포맷에 맞춰 출력해줘야 함
# arr = [1, 2, 3]
# print(arr) # [1, 2, 3] 그 자체로 출력됨
# for elem in arr:
#     print(elem, end=" ") # 1 2 3 이렇게 출력됨


# 문제

given_input = input()

print(given_input)
print(given_input)