# # 문자를 원소로 갖는 배열

# # APPLE의 각 문자를 원소로 갖는 리스트는 숫자와 마찬가지로 각 원소의 위치에 문자를 적어주는 방식으로 선언하면 됨
# word = ['A', 'P', 'P', 'L', 'E']

# # 리스트 안에 특정 문자가 있는지 확인하고 몇 번째 index에 있는지 알아내 방법

# 1. 몇 번째 index에 있는지를 저장해줄 idx라는 변수 사용
# 이때, index를 구해야 하기 때문에 for loop에서 i를 사용해야 함

# word = ['A', 'P', 'P', 'L', 'E']
# # 해당 문자를 찾지 못했다면 -1
# idx = -1
# # 문자 탐색
# for i in range(len(word)):
#     if word[i] == 'L':
#         idx = i
# # 문자가 존재하지 않는 경우
# if idx == -1:
#     print("not exist")
# else:
#     print(idx)

# # enumerate() 함수: 리스트 내의 원소와 index가 동시에 필요한 경우 원소로 (index, 원소)를 동시에 받으며 진행할 수 있음
# # enumerate(): 낱낱이 세다
# word = ['A', 'P', 'P', 'L', 'E']
# # 해당 문자를 찾지 못했다면 -1
# idx = -1
# # 문자 탐색
# for i, char in enumerate(word):
#     if char == 'L':
#         idx = i
# # 문자가 존재하지 않는 경우
# if idx == -1:
#     print("not exist")
# else:
#     print(idx)

# # 특정 원소가 리스트 안에 있는지, 없는지에 대해서는 in, not in이라는 키워드를 사용하여 쉽게 판단 가능
# word = ['A', 'P', 'P', 'L', 'E']

# if 'L' in word:
#     print('L is in list')
# if 'L' not in word:
#     print('L is not in list')

# index() 함수: 이미 존재하는 원소가 list의 어느 index에 있는지 알 수 있음
# word = ['A', 'P', 'P', 'L', 'E']
# print(word.index('L'))

# # BUT, 존재하지 않는 원소에 대해 index 함수를 이용하면 Value Error가 발생
# # => index 함수 이용시 꼭 먼저 해당 원소가 리스트에 포함되는지를 확인한 이후에 진행할 것!!
# word = ['A', 'P', 'P', 'L', 'E']
# # print(word.index('K')) # ValueError: 'K' is not in list
# # 원소가 리스트에 들어있는지 확인 후 index 참조 *****
# if 'K' in word:
#     print(word.index('K'))

# # => in과 index를 활용하면, 문자 'L'이 list에 있는지에 대한 여부와 어느 index에 있는지를 쉽게 구할 수 있음
# word = ['A', 'P', 'P', 'L', 'E']
# # 해당 문자가 리스트에 없는 경우
# if 'L' not in word:
#     print("not exist")
# # 해당 문자가 리스트에 있는 경우
# else:
#     print(word.index('L'))


# 문제
arr = ['L', 'E', 'B', 'R', 'O', 'S']
x = input()

if x in arr:
    print(arr.index(x))
else:
    print("None")