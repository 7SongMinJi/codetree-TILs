# # 공백 단위로 문자열 입력 받기

# # 공백을 사이에 두고 문자열들이 주어졌을 때, 이러한 문자열 리스트를 만들어 내는 방법
# # python: 한 줄 단위로만 입력받을 수 있기 때문에, 통째로 입력을 받은 뒤 공백 단위로 잘라서 리스트를 만들어야 함
# # split() 함수: 공백 단위로 쪼개져 리스트가 만들어짐 -> 이를 이용하여 간단히 문자열 리스트를 만들어낼 수 있음
# arr = input().split()
# print(arr)

# # 여기서 arr는 1차원 리스트이기 때문에, len(arr)를 출력하면 문자열의 개수가 나옴
# arr = input().split()
# print(len(arr))
# # >> apple banana candy
# # 3 출력

# # 공백 단위로 정확히 2개의 문자열을 입력 받을 때는 굳이 map 함수를 사용하지 않고 tuple만 사용하여 쉽게 구현 가능 *****
# # 이는 map 함수의 역할이 해당 원소들을 전부 원하는 type으로 변경하는 것이었기 때문 *****
# # 그니까 원래는 내가 tuple(list(map(int, input().split())))로 했는데... tuple(input().split())만으로 가능한가봐
# # tuple, list, map의 역할
# a, b = tuple(input().split())
# print(a)
# print(b)
# # >> banana apple
# # banana
# # apple


# 문제

input_val = input()
cnt = 0

for elem in input_val:
    if elem != " ":
        cnt += 1

print(cnt)