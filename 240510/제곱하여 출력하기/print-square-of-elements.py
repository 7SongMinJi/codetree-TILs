# # list comprehension

# # 리스트 arr의 각 원소들을 전부 2배씩 해주는 코드 작성하기

# # 1. 새로운 list를 만들어 append하기
# arr = [1, 2, 3, 5]
# new_arr = []
# for elem in arr:
#     new_arr.append(elem * 2)
# print(new_arr)

# 2. BUT 1번과 같이 새로운 리스트를 선언하고, for loop과 함께 append만 적용하는 경우에는 "list comprehension"을 이용하면 됨!
# list comprehension을 이용하면 선언과 동시에 for loop으로부터 나온 원소를 원하는 값으로 변경할 수 있음
# ***** [(append 안에 들어갈 내용) (for loop)] *****
# arr = [1, 2, 3, 5]
# new_arr = [elem * 2 for elem in arr]
# print(new_arr)

# # 3. 조건문을 포함하는 list comprehension
# # [(append 안에 들어갈 내용) (for loop) <조건문>]
# # <조건문>: 해당 조건문을 만족하면 그 값이 list에 들어가고, 만족하지 않을 경우 리스트에 들어가지 않음
# # arr = [1, 2, 3, 5]
# # list_ = [elem**2 for elem in arr if elem % 2 == 1]
# # print(list_)
# list_2 = [i ** 2 for i in range(1, 10) if i % 2 == 1] # list_2 = [i ** 2 for i in range(1, 10, 2)]와 같은 코드
# print(list_2)

# # 4. 변수가 두 개 이상인 list comprehension
# list_ = [(i + j) for i in range(3) for j in range(3)]
# # 결과: [0, 1, 2, 1, 2, 3, 2, 3, 4]
# list_ = []
# for i in range(3):
#     for j in range(3):
#         list_.append(i + j)
# # 코드 해석: 리스트에 i와 j를 더한 값을 저장할 건데 i의 범위는 range(3)에서 뽑히는 숫자들이고, j의 범위 또한 마찬가지
# # 다만, 두 변수를 다 움직이기는 힘드니까 for문처럼 하나의 문자부터 움직이게 하자!

# 5. n개의 원소가 주어졌을 때, 주어진 n개의 원소에 각각 제곱을 하여 출력하는 프로그램 작성
n = int(input())
arr = list(map(int, input().split()))
new_arr = [elem ** 2 for elem in arr]

for elem in new_arr:
    print(elem, end=" ")