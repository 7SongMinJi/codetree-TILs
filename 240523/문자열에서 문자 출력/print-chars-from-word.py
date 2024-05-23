# # 문자열 순회하기

# # 문자열을 이루고 있는 각 문자들을 순서대로 순회하기 = 리스트 내의 원소들을 순회하는 방법과 동일

# # 가장 직관적인 방법은 해당 문자열의 길이를 구한 뒤, for loop을 이용해 index 단위로 순회하는 것
# given_str = input()
# length = len(given_str)
# for i in range(length):
#     print(given_str[i])

# # BUT 리스트에서처럼, 문자열 역시 길이를 구하지 않고 바로 원소에 접근 가능
# given_str = input()
# for elem in given_str:
#     print(elem)


# 문제

given_str = input()

for elem in given_str:
    print(elem)