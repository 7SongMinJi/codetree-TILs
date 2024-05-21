# # 문자열 리스트의 필요성

# # 문자열이 한 줄에 하나씩 총 n개 주어졌을 때, 끝에 있는 3개의 문자열만 순서대로 출력하는 코드 작성하기

# # 가장 간단한 방법은 입력받은 n개의 문자열을 저장한 뒤, 그 중 끝에 있는 3개의 문자열을 출력하는 방식
# n = 5
# arr = []
# for _ in range(n):
#     given_str = input()
#     arr.append(given_str)
# for string in arr[-3:]: # 끝 3개 문자열 출력: arr[-3:] *****
#     print(string)

# # 이때, 문자열 리스트를 만드는 과정은 배열을 선언하고 for loop을 돌며 append하는 과정 뿐이므로 list comprehension을 통해 더 간결하게 구현 가능
# n = 5
# arr = [
#     input()
#     for _ in range(n)
# ]
# for string in arr[-3:]:
#     print(string)


# 문제 

n = 4
arr = [
    input()
    for _ in range(n)
]

for string in arr[::-1]:
    print(string)